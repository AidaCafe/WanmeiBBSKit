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
    _uid: Union[int, None] = None
    _login_data: Union[LoginData, None] = None

    @property
    def isLogin(self) -> bool:
        """
        是否登录
        :return: bool值
        """
        return not (self._token or self._uid)

    @property
    def device_info(self) -> DeviceInfo:
        """
        登录的设备信息
        :return: DeviceInfo对象
        """
        return self._device_info

    @property
    def token(self) -> Union[str, None]:
        """
        登录token
        :return: 一个token字符串
        """
        return self._token

    @property
    def uid(self) -> Union[int, None]:
        """
        登录uid
        :return: 逗留社区用户id，整数
        """
        return self._uid

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
        """
        登录并校验uid和token
        :param uid: 逗留用户id
        :param token: 逗留token
        :param device: 获得token时使用的设备信息
        :return: PerfectWorldAPI对象
        """
        instance_ = cls(device=device)
        login_data_ = await instance_.login(uid=uid, token=token)
        if login_data_.result:
            instance_._login_data = login_data_.result
            instance_._uid = login_data_.result.uid
            instance_._token = token
            return instance_
        raise InvalidToken('Not a valid login token!')

    @classmethod
    async def login_without_verify(cls, uid: int, token: str, device: DeviceInfo) -> "PerfectWorldAPI":
        """
        登录但不校验uid和token
        :param uid: 逗留用户id
        :param token: 逗留token
        :param device: 获得token时使用的设备信息
        :return: PerfectWorldAPI对象
        """
        instance_ = cls(device=device)
        instance_._uid = uid
        instance_._token = token
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
        """
        登录接口封装
        :param uid: 逗留uid
        :param token: 逗留token
        :return: 一个CommonResponse[LoginData]对象
        """
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
        return CommonResponse[LoginData].parse_obj(secure_json_retrieve(resp_))
