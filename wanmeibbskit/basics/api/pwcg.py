import asyncio
from typing import Any, Mapping, Optional, Union

from httpx import AsyncClient
from httpx import Response

from wanmeibbskit.basics import HYBRID_URL
from wanmeibbskit.basics.device_generator import get_rand_device
from wanmeibbskit.consts import TigerAPPConsts
from wanmeibbskit.utils import AsyncTigerTransport, URL
from wanmeibbskit.utils import secure_json_retrieve
from wanmeibbskit.models.device_info import DeviceInfo


class PerfectWorldAPI:
    _uid: Union[None, int] = None
    _token: Union[None, str] = None

    @property
    def isLogin(self) -> bool:
        return self._isLogin

    @property
    def device_info(self) -> Union[DeviceInfo, None]:
        return self._device_info

    @property
    def token(self) -> Union[str, None]:
        return self._token

    @property
    def uid(self) -> Union[int, None]:
        return self._uid

    def __init__(self, device: Optional[DeviceInfo] = None):
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
    def from_token(cls, uid: int, token: str, device: DeviceInfo) -> "PerfectWorldAPI":
        instance_ = cls(device=device)
        asyncio.run(instance_.login(uid=uid, token=token))
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

    async def login(self, uid: int, token: str):
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
        data_ = secure_json_retrieve(resp_)
        if data_ and data_.get('code', -1) == 0:
            self._isLogin = True
            self._uid = data_['result'].get('uid')
            self._token = token
            return data_
        raise ValueError('Not a valid login token!')
