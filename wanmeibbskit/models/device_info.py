from enum import Enum
from typing import Optional

from pydantic import Field

from wanmeibbs.consts import TigerAPPConsts
from wanmeibbs.models import AllStringCompactJsonModel

__all__ = [
    'DeviceBrands',
    'DeviceInfo',
    'OSType',
    'OSVersionRange',
]


class OSType(int, Enum):
    UNKNOWN = 0
    IOS = 1  # guess
    ANDROID = 2
    UNKNOWN2 = 3
    UNKNOWN3 = 4


class DeviceBrands:
    ANDROID = [
        'Acer', 'Alcatel', 'Allview', 'Amazon', 'Amoi', 'Archos', 'Asus', 'At&T', 'Benefon', 'Benq', 'Benq-Siemens',
        'Bird', 'Blackberry', 'Blackview', 'Blu', 'Bosch', 'Bq', 'Casio', 'Cat', 'Celkon', 'Chea', 'Coolpad', 'Dell',
        'Doogee', 'Emporia', 'Energizer', 'Ericsson', 'Eten', 'Fairphone', 'Fujitsu Siemens', 'Garmin-Asus', 'Gigabyte',
        'Gionee', 'Google', 'Haier', 'Honor', 'Hp', 'Htc', 'Huawei', 'I-Mate', 'I-Mobile', 'Icemobile', 'Infinix',
        'Innostream', 'Inq', 'Intex', 'Jolla', 'Karbonn', 'Kyocera', 'Lava', 'Leeco', 'Lenovo', 'Lg', 'Maxon',
        'Maxwest', 'Meizu', 'Micromax', 'Microsoft', 'Mitac', 'Mitsubishi', 'Modu', 'Motorola', 'Mwg', 'Nec', 'Neonode',
        'Niu', 'Nokia', 'Nothing', 'Nvidia', 'O2', 'Oneplus', 'Oppo', 'Orange', 'Palm', 'Panasonic', 'Pantech', 'Parla',
        'Philips', 'Plum', 'Posh', 'Prestigio', 'Qmobile', 'Qtek', 'Razer', 'Realme', 'Sagem', 'Samsung', 'Sendo',
        'Sewon', 'Sharp', 'Siemens', 'Sonim', 'Sony', 'Sony Ericsson', 'Spice', 'T-Mobile', 'Tcl', 'Tecno', 'Tel.Me.',
        'Telit', 'Thuraya', 'Toshiba', 'Ulefone', 'Unnecto', 'Vertu', 'Verykool', 'Vivo', 'Vk Mobile', 'Vodafone',
        'Wiko', 'Wnd', 'Xcute', 'Xiaomi', 'Xolo', 'Yezz', 'Yota', 'Yu', 'Zte'
    ]
    IOS = ['Apple']


class OSVersionRange:
    ANDROID = (2, 14)
    IOS = (6, 15)


class DeviceInfo(AllStringCompactJsonModel):
    build_version: Optional[str] = Field(TigerAPPConsts.BUILD_VERSION, alias="buildVersion", const=True,
                                         description="构建版本号")
    system_version: int = Field(..., alias="phoneSystemVersion", description="系统版本")
    model: str = Field(..., alias="device_model", description="设备型号")
    device_type: str = Field(..., description="设备生产厂商")
    version: Optional[int] = Field(TigerAPPConsts.VERSION, const=True, description="社区版本号")
    device_id: str = Field(..., alias="deviceId", description="设备Id")
    app_id: int = Field(..., alias="appId", description="应用Id")
    os: OSType = Field(..., alias="osType", description="系统类型")
    package: Optional[str] = Field(TigerAPPConsts.PACKAGE_NAME, alias="packageName", const=True, description="包名")
    channel_id: int = Field(..., alias="channelId", description="频道Id")
    sub_app_id: str = Field(..., alias="subAppId", description="子应用Id")
