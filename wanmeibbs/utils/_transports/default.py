import time
from typing import Optional

from httpx import AsyncHTTPTransport, HTTPTransport
from httpx import Request, Response

from wanmeibbs.basics import Sha1Utils
from wanmeibbs.basics.device_generator import get_rand_device
from wanmeibbs.consts import TigerAPPConsts
from wanmeibbs.utils import timestamp, Params

__all__ = [
    'TigerTransport',
    'AsyncTigerTransport'
]


class AsyncTigerTransport(AsyncHTTPTransport):
    def __init__(
            self,
            app_id: Optional[int] = 10021,
            channel_id: Optional[int] = 1991,
            sub_app_id: Optional[str] = TigerAPPConsts.PACKAGE_NAME,
            user_agent: Optional[str] = 'okhttp/4.9.0',
            **kwargs
    ):
        self.device_info = get_rand_device(
            app_id=app_id,
            channel_id=channel_id,
            sub_app_id=sub_app_id
        )
        self.user_agent = user_agent
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
            app_id: Optional[int] = 10021,
            channel_id: Optional[int] = 1991,
            sub_app_id: Optional[str] = TigerAPPConsts.PACKAGE_NAME,
            user_agent: Optional[str] = 'okhttp/4.9.0',
            **kwargs
    ):
        self.device_info = get_rand_device(
            app_id=app_id,
            channel_id=channel_id,
            sub_app_id=sub_app_id
        )
        self.user_agent = user_agent
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
