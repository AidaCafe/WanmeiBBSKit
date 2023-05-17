from typing import Union, Protocol
from json import JSONDecodeError

__all__ = ['safety_response_json']


class Response(Protocol):
    status_code: int

    def json(self, **kwargs) -> dict:
        ...


def safety_response_json(
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
