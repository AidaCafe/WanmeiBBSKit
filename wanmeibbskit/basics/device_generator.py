import random
from binascii import hexlify
from os import urandom
from string import ascii_uppercase, digits
from typing import Optional

from wanmeibbskit.consts import TigerAPPConsts
from wanmeibbskit.models.device_info import DeviceBrands
from wanmeibbskit.models.device_info import DeviceInfo
from wanmeibbskit.models.device_info import OSType, OSVersionRange

RAND_CHARS = f'{ascii_uppercase}{digits}'


class DeviceInfoGenerator:
    @staticmethod
    def device_id() -> str:
        return hexlify(urandom(16)).decode()

    @staticmethod
    def os_type() -> OSType:
        return random.choice(list(OSType))

    @staticmethod
    def device_type() -> str:
        return random.choice(DeviceBrands.ANDROID)

    @staticmethod
    def model() -> str:
        return ''.join(random.choices(RAND_CHARS, k=12))

    @staticmethod
    def generate() -> dict:
        os_type = DeviceInfoGenerator.os_type()
        device_type = 'Apple' if os_type is OSType.IOS else DeviceInfoGenerator.device_type()
        os_version = random.randint(*OSVersionRange.IOS) if os_type is OSType.IOS \
            else random.randint(*OSVersionRange.ANDROID)
        return {
            "phoneSystemVersion": os_version,
            "device_model": DeviceInfoGenerator.model(),
            "device_type": device_type,
            "deviceId": DeviceInfoGenerator.device_id(),
            "osType": os_type
        }


def get_rand_device(
        app_id: int,
        channel_id: int,
        sub_app_id: Optional[str] = None
) -> DeviceInfo:
    if not sub_app_id:
        sub_app_id = TigerAPPConsts.PACKAGE_NAME
    return DeviceInfo(
        **DeviceInfoGenerator.generate(),
        appId=app_id,
        channelId=channel_id,
        subAppId=sub_app_id
    )
