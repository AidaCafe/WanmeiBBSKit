from json import JSONDecodeError
from typing import Optional, Union

from httpx import AsyncClient

from wanmeibbskit.basics import HYBRID_URL
from wanmeibbskit.utils import AsyncUserMgrTransport
from wanmeibbskit.utils import safety_response_json
from wanmeibbskit.models.sms_login import SmsLoginResponse

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
        self._client = AsyncClient(**client_kwargs)

        self._sent_count = 0

    @property
    def sent_count(self):
        return self._sent_count

    @property
    def has_sent(self) -> bool:
        return self._sent_count != 0

    async def send_sms(self) -> bool:
        resp_ = await self._client.post(
            '/m/newApi/sendPhoneCaptchaWithOutLogin',
            params={
                "type": self.login_type,
                "areaCodeId": self.area_code_id,
                "cellphone": self.phone_number
            }
        )
        if not (data := safety_response_json(resp_, restrict_status_code=True)):
            return False
        if data.get("code", -1) != 0:
            return False
        return True

    async def verify_code(self, captcha_code: int):
        resp_ = await self._client.post(
            '/m/newApi/checkPhoneCaptchaWithOutLogin',
            params={
                "cellphone": self.phone_number,
                "captcha": captcha_code
            }
        )
        if not (data := safety_response_json(resp_, restrict_status_code=True)):
            return False
        if data.get("code", -1) != 0:
            return False
        return True

    async def login(self) -> Union[SmsLoginResponse, None]:
        resp_ = await self._client.post(
            '/m/newApi/sms/login',
            params={
                "areaCodeId": self.area_code_id,
                "cellphone": self.phone_number,
            }
        )
        if not (data := safety_response_json(resp_, restrict_status_code=True)):
            return None
        if data.get("code", -1) != 0:
            return None
        return SmsLoginResponse(**data)
