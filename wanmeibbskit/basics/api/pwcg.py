from typing import Any, Mapping, Optional, Union

from httpx import AsyncClient
from httpx import Response

from wanmeibbskit.basics import HYBRID_URL
from wanmeibbskit.basics.device_generator import get_rand_device
from wanmeibbskit.consts import TigerAPPConsts
from wanmeibbskit.exceptions import InvalidToken
from wanmeibbskit.models import CommonResponse
from wanmeibbskit.models.device_info import DeviceInfo
from wanmeibbskit.models.pwgcapi import LoginData
from wanmeibbskit.utils import AsyncTigerTransport, URL
from wanmeibbskit.utils import secure_json_retrieve


class PerfectWorldAPI:
    _token: Union[str, None] = None
    _login_data: Union[LoginData, None] = None

    @property
    def isLogin(self) -> bool:
        return self._login_data is not None

    @property
    def device_info(self) -> Union[DeviceInfo, None]:
        return self._device_info

    @property
    def token(self) -> Union[str, None]:
        return self._token

    @property
    def uid(self) -> Union[int, None]:
        return self._login_data.uid

    def __init__(self, device: Optional[DeviceInfo] = None):
        self._token = None
        if not device:
            device = get_rand_device(
                app_id=TigerAPPConsts.COMMON_APP_ID,
                channel_id=TigerAPPConsts.COMMON_CHANNEL_ID,
                sub_app_id=TigerAPPConsts.PACKAGE_NAME
            )
        self._device_info = device
        self.client = AsyncClient(
            base_url=HYBRID_URL.PWCGAPI,
            transport=AsyncTigerTransport(device_info=self._device_info),
        )

        self._isLogin = False

    @classmethod
    async def from_token(cls, uid: int, token: str, device: DeviceInfo) -> "PerfectWorldAPI":
        instance_ = cls(device=device)
        await instance_.login(uid=uid, token=token)
        return instance_

    async def request(
            self,
            url: Union[str, URL],
            method: str = 'GET',
            data: Optional[Mapping[str, Any]] = None,
            params: Optional[Mapping[str, Any]] = None
    ) -> Response:
        return await self.client.request(
            method=method,
            url=url,
            data=data,
            params=params
        )

    async def login(self, uid: int, token: str) -> CommonResponse[LoginData]:
        resp_ = await self.client.post(
            '/login/v2',
            params={
                "uid": uid,
                "username": None,
                "avatar": None,
            },
            headers={
                "token": token
            }
        )
        data_ = CommonResponse[LoginData].parse_obj(secure_json_retrieve(resp_))
        if data_.result:
            self._login_data = data_.result
            self._token = token
            return data_
        raise InvalidToken('Not a valid login token!')
