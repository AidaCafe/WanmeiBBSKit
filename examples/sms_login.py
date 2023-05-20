from wanmeibbskit.basics.login_session import SmsLoginSession
from wanmeibbskit.models.device_info import DeviceInfo


async def main(session: SmsLoginSession):
    if not await session.send_sms():
        print('发送失败!')
        return {}
    while not (cCode := 0):
        input_code = input('验证码: ')
        if not input_code.isdigit() or not len(input_code) != 0:
            print('验证码格式错误')
            return {}
        cCode = int(input_code)
        break
    if not await session.verify_code(captcha_code=cCode):
        print('验证码错误')
        return {}
    return await session.login()


async def send_only(session: SmsLoginSession):
    if not await session.send_sms():
        return '发送失败!'
    return '发送成功'


if __name__ == '__main__':
    import asyncio
    from pathlib import Path

    import orjson

    while not (PHONE_NUMBER := 0): # 获取手机号
        if (phone_number_ := input('输入手机号:')).isdigit():
            PHONE_NUMBER = int(phone_number_)
            break
        else:
            print('手机号格式错误')

    stored_device = Path(__file__).parent / 'device.json'  # 设备储存

    if not stored_device.exists():  # 如果没有本地设备，则让登录session自动生成并储存
        with open(stored_device, 'wb+') as f:
            session_ = SmsLoginSession(phone_number=PHONE_NUMBER)  # 短信登录session
            f.write(orjson.dumps(session_.device_info.dict(by_alias=True), option=orjson.OPT_INDENT_2))
    else:
        with open(stored_device, 'r', encoding='utf-8') as f:
            local_device = DeviceInfo.parse_obj(orjson.loads(f.read()))
            session_ = SmsLoginSession(phone_number=PHONE_NUMBER, device_info=local_device)

    data = asyncio.run(main(session_))
    print(data)
