from typing import Optional, Union

from httpx import AsyncClient

from wanmeibbskit.basics import HYBRID_URL
from wanmeibbskit.basics.device_generator import get_rand_device
from wanmeibbskit.consts import DEFAULT_LOGIN_AREA
from wanmeibbskit.consts import DEFAULT_LOGIN_TYPE
from wanmeibbskit.consts import TigerAPPConsts
from wanmeibbskit.models.device_info import DeviceInfo
from wanmeibbskit.models.userapi.sms_login import SmsLoginResponse
from wanmeibbskit.utils import AsyncUserMgrTransport
from wanmeibbskit.utils import secure_json_retrieve

__all__ = ['SmsLoginSession']


class SmsLoginSession:
    def __init__(
            self,
            phone_number: int,
            device_info: Optional[DeviceInfo] = None,
            app_id: Optional[int] = None,
            channel_id: Optional[int] = None,
            login_type: Optional[int] = None,
            area_code_id: Optional[int] = 1,
            **client_kwargs
    ) -> None:
        if not device_info:
            if not app_id:
                app_id = TigerAPPConsts.COMMON_APP_ID
            if not channel_id:
                channel_id = TigerAPPConsts.COMMON_CHANNEL_ID

            device_info = get_rand_device(
                app_id=app_id,
                channel_id=channel_id
            )

        self._device_info = device_info
        self.phone_number = phone_number
        self.login_type = login_type if login_type else DEFAULT_LOGIN_TYPE
        self.area_code_id = area_code_id if area_code_id else DEFAULT_LOGIN_AREA

        client_kwargs.update({
            "base_url": HYBRID_URL.USERAPI,
            "transport": AsyncUserMgrTransport(
                device_info=self._device_info
            )
        })

        self._client = AsyncClient(**client_kwargs)
        self._sent_count = 0

    @property
    def device_info(self) -> DeviceInfo:
        return self._device_info

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
        if not (data := secure_json_retrieve(resp_, restrict_status_code=True)):
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
        if not (data := secure_json_retrieve(resp_, restrict_status_code=True)):
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
        if not (data := secure_json_retrieve(resp_, restrict_status_code=True)):
            return None
        if data.get("code", -1) != 0:
            return None
        return SmsLoginResponse(**data)
