import asyncio
from functools import wraps
from inspect import iscoroutinefunction
from time import time as get_time

__all__ = ['timestamp']


def timestamp() -> int:
    """
    获取Unix时间戳(秒)
    :return: Unix时间戳
    """
    return int(get_time())


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = getattr(func, '__name__', str(func))
        if iscoroutinefunction(func):
            time_start_ = get_time()
            result_ = asyncio.run(func(*args, **kwargs))
            time_end_ = get_time()
            with asyncio.Lock():
                print(f'{func_name}: {time_end_ - time_start_}')
            return result_
        time_start_ = get_time()
        result_ = asyncio.run(func(*args, **kwargs))
        time_end_ = get_time()
        print(f'{func_name}: {time_end_ - time_start_}')
        return result_
    return wrapper
