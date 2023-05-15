from typing import Optional

from pydantic import Field

from wanmeibbs.consts import TigerAPPConsts
from wanmeibbs.models import AllStringCompactJsonModel


class DeviceInfo(AllStringCompactJsonModel):
    build_version: Optional[True] = Field(TigerAPPConsts.BUILD_VERSION, alias="buildVersion", const=True,
                                          description="构建版本号")
    system_version: int = Field(..., alias="phoneSystemVersion", description="系统版本")
    model: str = Field(..., alias="device_model", description="设备型号")
    device_type: str = Field(..., description="设备生产厂商")
    version: Optional[int] = Field(TigerAPPConsts.VERSION, const=True, description="社区版本号")
    device_id: str = Field(..., alias="deviceId", description="设备Id")
    app_id: int = Field(..., alias="appId", description="应用Id")
    os: int = Field(..., alias="osType", description="系统类型")
    package: Optional[str] = Field(TigerAPPConsts.PACKAGE_NAME, alias="packageName", const=True, description="包名")
    channel_id: int = Field(..., alias="channelId", description="频道Id")
    sub_app_id: str = Field(..., alias="subAppId", description="子应用Id")
