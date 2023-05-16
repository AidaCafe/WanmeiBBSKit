from typing import Optional

from httpx import AsyncHTTPTransport, HTTPTransport
from httpx import Request, Response

from wanmeibbs.basics import MD5Utils
from wanmeibbs.basics.device_generator import get_rand_device
from wanmeibbs.consts import TigerAPPConsts
from wanmeibbs.utils import Params, timestamp

__all__ = [
    'UserMgrTransport',
    'AsyncUserMgrTransport'
]


class AsyncUserMgrTransport(AsyncHTTPTransport):
    def __init__(
            self,
            app_id: Optional[int] = 10021,
            channel_id: Optional[int] = 1991,
            user_agent: Optional[str] = None,
            **kwargs
    ):
        self.device_info = get_rand_device(
            app_id=app_id,
            channel_id=channel_id
        )
        if not user_agent:
            user_agent = f'LaohuSDK/{TigerAPPConsts.SDK_VERSION} ' \
                         f'({self.device_info.os.name.lower()} os {self.device_info.system_version};' \
                         f'mobile  manufacturer {self.device_info.device_type}; model {self.device_info.model})'
        self.user_agent = user_agent
        super().__init__(**kwargs)

    async def handle_async_request(self, request: Request) -> Response:
        params_ = Params(request.url.params)
        current_time = timestamp()
        params_ = params_.merge({
            "deviceType": self.device_info.model,
            "deviceId": self.device_info.device_id,
            "deviceName": self.device_info.model,
            "versionCode": TigerAPPConsts.VERSION,
            "t": current_time,
            "deviceSys": self.device_info.system_version,
            "deviceModel": self.device_info.model,
            "sdkVersion": TigerAPPConsts.SDK_VERSION,
            "bid": TigerAPPConsts.PACKAGE_NAME,
        })
        if not params_.get('appId'):
            params_ = params_ & f'appId={self.device_info.app_id}'
        if not params_.get('channelId'):
            params_ = params_ & f'channelId={self.device_info.channel_id}'

        request.url = request.url.copy_merge_params(
            params_.merge({
                "sign": MD5Utils.getParamsStringHash(
                    params_string=params_.raw
                )
            })
        )

        if not request.headers.get('User-Agent'):
            request.headers['User-Agent'] = self.user_agent
        return await super().handle_async_request(request=request)


class UserMgrTransport(HTTPTransport):
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
            "deviceType": self.device_info.model,
            "deviceId": self.device_info.device_id,
            "deviceName": self.device_info.model,
            "versionCode": TigerAPPConsts.VERSION,
            "t": current_time,
            "deviceSys": self.device_info.system_version,
            "deviceModel": self.device_info.model,
            "sdkVersion": TigerAPPConsts.SDK_VERSION,
            "bid": TigerAPPConsts.PACKAGE_NAME,
        })
        if not params_.get('appId'):
            params_ = params_ & f'appId={self.device_info.app_id}'
        if not params_.get('channelId'):
            params_ = params_ & f'channelId={self.device_info.channel_id}'

        request.url = request.url.copy_merge_params(
            params_.merge({
                "sign": MD5Utils.getParamsStringHash(
                    params_string=params_.raw
                )
            })
        )

        if not request.headers.get('User-Agent'):
            request.headers['User-Agent'] = self.user_agent
        return super().handle_request(request=request)
