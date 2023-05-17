import time
from typing import Optional

from httpx import AsyncHTTPTransport, HTTPTransport
from httpx import Request, Response

from wanmeibbskit.basics import Sha1Utils
from wanmeibbskit.basics.device_generator import get_rand_device
from wanmeibbskit.consts import TigerAPPConsts
from wanmeibbskit.models.device_info import DeviceInfo
from wanmeibbskit.utils import timestamp, Params

__all__ = [
    'TigerTransport',
    'AsyncTigerTransport'
]


class AsyncTigerTransport(AsyncHTTPTransport):
    def __init__(
            self,
            device_info: Optional[DeviceInfo] = None,
            app_id: Optional[int] = None,
            channel_id: Optional[int] = None,
            sub_app_id: Optional[str] = None,
            user_agent: Optional[str] = None,
            **kwargs
    ):
        if not device_info:
            if not app_id:
                app_id = TigerAPPConsts.COMMON_APP_ID
            if not channel_id:
                channel_id = TigerAPPConsts.COMMON_CHANNEL_ID
            if not sub_app_id:
                sub_app_id = TigerAPPConsts.PACKAGE_NAME

            device_info = get_rand_device(
                app_id=app_id,
                channel_id=channel_id,
                sub_app_id=sub_app_id
            )
        self.device_info = device_info

        self.user_agent = user_agent if user_agent else TigerAPPConsts.SDK_USERAGENT
        super().__init__(**kwargs)

    async def handle_async_request(self, request: Request) -> Response:
        params_ = Params(request.url.params)
        current_time = timestamp()
        params_ = params_.merge({
            "timestamp": current_time,
            "deviceInfo": self.device_info,
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
            device_info: Optional[DeviceInfo] = None,
            app_id: Optional[int] = None,
            channel_id: Optional[int] = None,
            sub_app_id: Optional[str] = None,
            user_agent: Optional[str] = None,
            **kwargs
    ):
        if not device_info:
            if not app_id:
                app_id = TigerAPPConsts.COMMON_APP_ID
            if not channel_id:
                channel_id = TigerAPPConsts.COMMON_CHANNEL_ID
            if not sub_app_id:
                sub_app_id = TigerAPPConsts.PACKAGE_NAME

            device_info = get_rand_device(
                app_id=app_id,
                channel_id=channel_id,
                sub_app_id=sub_app_id
            )
        self.device_info = device_info

        self.user_agent = user_agent if user_agent else TigerAPPConsts.SDK_USERAGENT
        super().__init__(**kwargs)

    def handle_async_request(self, request: Request) -> Response:
        params_ = Params(request.url.params)
        current_time = timestamp()
        params_ = params_.merge({
            "timestamp": current_time,
            "deviceInfo": self.device_info,
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
