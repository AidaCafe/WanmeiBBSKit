from json import JSONDecodeError
from typing import Any, Optional, Union, Protocol

__all__ = [
    'secure_json_retrieve',
    'secure_int_retrieve'
]


class Response(Protocol):
    status_code: int

    def json(self, **kwargs) -> dict:
        ...


def secure_json_retrieve(
        __resp: Response,
        restrict_status_code: bool = False
) -> Union[dict, None]:
    """
    安全获得返回json
    :param __resp: 带有json()方法的类
    :param restrict_status_code: 严格限制返回结果的HTTP状态码
    :return: 成功返回dict对象，失败则返回None
    """
    if restrict_status_code and __resp.status_code != 200:
        return None
    try:
        response_data = __resp.json()
    except JSONDecodeError:
        return None
    return response_data


def secure_int_retrieve(value: Any, __default: Optional[int] = None) -> Union[int, None]:
    """
    安全获得int值
    :param value: 任何类型
    :param __default: 获取失败时的默认返回值
    :return: value的值或者None
    """
    if hasattr(value, 'value'):
        value = value.value
    if isinstance(value, int):
        return value
    try:
        return int(value)
    except TypeError:
        return __default
