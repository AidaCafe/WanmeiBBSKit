from asyncio import run

import orjson

from wanmeibbskit.models.device_info import DeviceInfo
from wanmeibbskit.query.hotta import HottaClient


async def main():  # 请先运行sms_login.py 短信登录后再试。
    with open('device.json', 'r') as f:
        device = DeviceInfo.parse_obj(orjson.loads(f.read()))

    # 注意短信登录内的uid和token字段，将下面的LOGIN_UID和LOGIN_TOKEN 替换为其对应的值
    LOGIN_UID = 0
    LOGIN_TOKEN = "token"
    client = await HottaClient.from_token(uid=LOGIN_UID, token=LOGIN_TOKEN, device=device)
    resp_ = await client.getRoleData()
    role_data = resp_.result
    print(f"活跃天数{role_data.days}")
    for ach in role_data.achievements:
        print(f'{ach.name}: {ach.value}')


if __name__ == "__main__":
    run(main())
