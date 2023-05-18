from typing import Optional

from httpx import AsyncHTTPTransport, HTTPTransport
from httpx import Request, Response

from wanmeibbskit.basics.md5utils import MD5Utils
from wanmeibbskit.basics.device_generator import get_rand_device
from wanmeibbskit.consts import TigerAPPConsts
from wanmeibbskit.utils import Params, timestamp
from wanmeibbskit.models.device_info import DeviceInfo

__all__ = [
    'UserMgrTransport',
    'AsyncUserMgrTransport'
]


class AsyncUserMgrTransport(AsyncHTTPTransport):
    def __init__(
            self,
            device_info: Optional[DeviceInfo] = None,
            app_id: Optional[int] = None,
            channel_id: Optional[int] = None,
            user_agent: Optional[str] = None,
            **kwargs
    ):
        if not device_info:
            if not app_id:
                app_id = TigerAPPConsts.COMMON_APP_ID
            if not channel_id:
                channel_id = TigerAPPConsts.COMMON_CHANNEL_ID

            device_info = get_rand_device(
                app_id=app_id,
                channel_id=channel_id
            )
        self.device_info = device_info

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
            device_info: Optional[DeviceInfo] = None,
            app_id: Optional[int] = None,
            channel_id: Optional[int] = None,
            user_agent: Optional[str] = None,
            **kwargs
    ):
        if not device_info:
            if not app_id:
                app_id = TigerAPPConsts.COMMON_APP_ID
            if not channel_id:
                channel_id = TigerAPPConsts.COMMON_CHANNEL_ID

            device_info = get_rand_device(
                app_id=app_id,
                channel_id=channel_id
            )
        self.device_info = device_info

        if not user_agent:
            user_agent = f'LaohuSDK/{TigerAPPConsts.SDK_VERSION} ' \
                         f'({self.device_info.os.name.lower()} os {self.device_info.system_version};' \
                         f'mobile  manufacturer {self.device_info.device_type}; model {self.device_info.model})'
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
