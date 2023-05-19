from typing import Optional

from httpx import AsyncHTTPTransport, HTTPTransport
from httpx import Request, Response

from wanmeibbskit.basics.sha1utils import Sha1Utils
from wanmeibbskit.consts import TigerAPPConsts
from wanmeibbskit.exceptions import DeviceInfoRequired
from wanmeibbskit.models.device_info import DeviceInfo
from wanmeibbskit.utils import timestamp, Params

__all__ = [
    'TigerTransport',
    'AsyncTigerTransport'
]


class AsyncTigerTransport(AsyncHTTPTransport):
    def __init__(
            self,
            device_info: DeviceInfo,
            user_agent: Optional[str] = None,
            **kwargs
    ):
        if not device_info:
            raise DeviceInfoRequired
        self.device_info = device_info

        self.user_agent = user_agent if user_agent else TigerAPPConsts.SDK_USERAGENT
        super().__init__(**kwargs)

    async def handle_async_request(self, request: Request) -> Response:
        params_ = Params(request.url.params)
        current_time = timestamp()
        params_ = params_.merge({
            "timestamp": current_time,
            "deviceInfo": self.device_info.json(by_alias=True),
        })

        request.url = request.url.copy_merge_params(
            params_.merge({
                "sign": Sha1Utils.signParamsString(
                    params=params_.raw,
                    b64_private_key=TigerAPPConsts.RSA_PRIVATE_KEY
                )
            })
        )

        if not request.headers.get('User-Agent'):
            request.headers['User-Agent'] = self.user_agent
        return await super().handle_async_request(request=request)


class TigerTransport(HTTPTransport):
    def __init__(
            self,
            device_info: DeviceInfo,
            user_agent: Optional[str] = None,
            **kwargs
    ):
        if not device_info:
            raise DeviceInfoRequired
        self.device_info = device_info

        self.user_agent = user_agent if user_agent else TigerAPPConsts.SDK_USERAGENT
        super().__init__(**kwargs)

    def handle_request(self, request: Request) -> Response:
        params_ = Params(request.url.params)
        current_time = timestamp()
        params_ = params_.merge({
            "timestamp": current_time,
            "deviceInfo": self.device_info.json(by_alias=True),
        })

        request.url = request.url.copy_merge_params(
            params_.merge({
                "sign": Sha1Utils.signParamsString(
                    params=params_.raw,
                    b64_private_key=TigerAPPConsts.RSA_PRIVATE_KEY
                )
            })
        )

        if not request.headers.get('User-Agent'):
            request.headers['User-Agent'] = self.user_agent
        return super().handle_request(request=request)
