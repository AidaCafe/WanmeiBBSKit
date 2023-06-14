import subprocess
from asyncio import run
from pathlib import Path

import orjson

from wanmeibbskit.query.hotta import HottaClient
from wanmeibbskit.models.device_info import DeviceInfo
from sms_login import main as sms_login

FILE = Path(__file__).parent
DEVICE_INFO_PATH = FILE / 'device.json'
LOGIN_STATE_PATH = FILE / 'LOGIN_STATE'


async def main():  # 请先运行sms_login.py 短信登录后再试。
    if not DEVICE_INFO_PATH.exists() or not LOGIN_STATE_PATH.exists():
        print("暂无登录数据。启动登录流程...")
        await sms_login()

    with open('device.json', 'r') as f:
        device = DeviceInfo.parse_obj(orjson.loads(f.read()))

    # 注意短信登录内的uid和token字段，将下面的LOGIN_UID和LOGIN_TOKEN 替换为其对应的值
    with open('LOGIN_STATE', 'r') as f:
        uid, token = [_.split('=')[1] for _ in f.readlines()]

    client = await HottaClient.from_token(uid=uid, token=token, device=device)
    resp_ = await client.getRoleData()
    role_data = resp_.result
    print(f"活跃天数{role_data.days}")
    for ach in role_data.achievements:
        print(f'{ach.name}: {ach.value}')


if __name__ == "__main__":
    run(main())
