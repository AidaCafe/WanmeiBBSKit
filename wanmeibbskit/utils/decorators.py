from functools import wraps


def enforce_implementation(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        raise NotImplementedError
    return wrapper
