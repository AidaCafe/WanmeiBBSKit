from time import time as get_time

__all__ = ['timestamp']


def timestamp() -> int:
    """
    获取Unix时间戳(秒)
    :return: Unix时间戳
    """
    return int(get_time())
