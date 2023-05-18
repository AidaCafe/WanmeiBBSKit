import orjson

from wanmeibbskit.basics.device_generator import get_rand_device
from wanmeibbskit.models.device_info import DeviceInfo


def test_json_dumping():
    device = get_rand_device(app_id=10021, channel_id=1991)
    assert isinstance(device.json(), str)


def test_load_device():
    device_ = get_rand_device(app_id=10021, channel_id=1991)
    device_raw = orjson.loads(device_.json(by_alias=True))
    device_raw_obj = DeviceInfo(**device_raw)
    assert device_raw_obj == device_
