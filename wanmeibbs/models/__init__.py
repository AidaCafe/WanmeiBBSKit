import json

from pydantic import BaseModel

from .device_info import DeviceInfo

__all__ = [
    'CompactJsonModel',
    'DeviceInfo'
]


def compact_dumps(__obj: dict, default, **kwargs) -> str:
    # orjson不支持default，手动实现须两层嵌套循环，加之少量数据时速度对比不明显，故使用json
    kwargs.update({
        "separators": (',', ':')
    })
    return json.dumps(__obj, default=default, **kwargs)


class CompactJsonModel(BaseModel):
    class Config:
        json_dumps = compact_dumps
