from time import time as timestamp

from httpx import Request, Response
from httpx import AsyncHTTPTransport, HTTPTransport

from wanmeibbs.utils import Params
from wanmeibbs.basics import Sha1Utils
from wanmeibbs.basics.device_generator import get_rand_device
from wanmeibbs.consts import TigerAPPConsts


__all__ = [
    'TigerTransport',
    'AsyncTigerTransport'
]


class AsyncTigerTransport(AsyncHTTPTransport):
    device_info = get_rand_device()

    async def handle_async_request(self, request: Request) -> Response:
        params_ = Params(request.url.params)
        current_time = timestamp()
        params_.update({
            "timestamp": current_time,
            "deviceInfo": self.device_info,
        })
        params_["sign"] = Sha1Utils.signParamsString(
            params=params_.raw,
            b64_private_key=TigerAPPConsts.RSA_PRIVATE_KEY
        )
        request.url.params = request.url.params.merge(params_)
        return await super().handle_async_request(request=request)


class TigerTransport(HTTPTransport):
    device_info = get_rand_device()

    def handle_async_request(self, request: Request) -> Response:
        params_ = Params(request.url.params)
        current_time = timestamp()
        params_.update({
            "timestamp": current_time,
            "deviceInfo": self.device_info,
        })
        params_["sign"] = Sha1Utils.signParamsString(
            params=params_.raw,
            b64_private_key=TigerAPPConsts.RSA_PRIVATE_KEY
        )
        request.url.params = request.url.params.merge(params_)
        return super().handle_request(request=request)
