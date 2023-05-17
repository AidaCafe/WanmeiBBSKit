from json import JSONDecodeError
from typing import Optional

from httpx import AsyncClient

from wanmeibbskit.basics import HYBRID_URL
from wanmeibbskit.utils import AsyncUserMgrTransport

__all__ = ['SmsLoginSession']


class SmsLoginSession:
    def __init__(
            self,
            phone_number: int,
            app_id: Optional[int] = 10021,
            channel_id: Optional[int] = 1991,
            login_type: Optional[int] = 16,
            area_code_id: Optional[int] = 1,
            **client_kwargs
    ) -> None:
        client_kwargs.update({
            "base_url": HYBRID_URL.USERAPI,
            "transport": AsyncUserMgrTransport(
                app_id=app_id,
                channel_id=channel_id
            )
        })
        self.phone_number = phone_number
        self.login_type = login_type
        self.area_code_id = area_code_id
        self.client = AsyncClient(**client_kwargs)

    async def send_sms(self) -> bool:
        resp_ = await self.client.post(
            '/m/newApi/sendPhoneCaptchaWithOutLogin',
            params={
                "type": self.login_type,
                "areaCodeId": self.area_code_id,
                "cellphone": self.phone_number
            }
        )
        if not resp_.status_code == 200:
            return False
        try:
            return_data = resp_.json()
        except JSONDecodeError:
            return False
        if return_data.get("code", -1) != 0:
            return False
        return True

    async def verify_code(self, captcha_code: int):
        resp_ = await self.client.post(
            'm/newApi/checkPhoneCaptchaWithOutLogin',
            params={
                "cellphone": self.phone_number,
                "captcha": captcha_code
            }
        )
        if not resp_.status_code == 200:
            return False
        try:
            return_data = resp_.json()
        except JSONDecodeError:
            return False
        if return_data.get("code", -1) != 0:
            return False
        return True
