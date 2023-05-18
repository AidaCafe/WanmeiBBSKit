import asyncio
from functools import wraps

__all__ = [
    'enforce_implementation',
    'method_need_login'
]


def enforce_implementation(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        raise NotImplementedError

    return wrapper


def method_need_login(func):
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            if not self.isLogin:
                raise Exception("Login required!")
            return await func(self, *args, **kwargs)

        return async_wrapper

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.isLogin:
            raise Exception("Login required!")
        return func(self, *args, **kwargs)

    return wrapper
