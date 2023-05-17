from typing import Any, List, Mapping, Optional, Sequence, Tuple, Union

import httpx
import orjson


PrimitiveData = Optional[Union[str, int, float, bool]]
QueryParamTypes = Union[
    "Params",
    httpx.QueryParams,
    Mapping[str, Union[PrimitiveData, Sequence[PrimitiveData]]],
    List[Tuple[str, PrimitiveData]],
    Tuple[Tuple[str, PrimitiveData], ...],
    str,
    bytes,
]


class URL(httpx.URL):
    def __truediv__(self, other):
        return super().join(other)


class Params(httpx.QueryParams):
    def __init__(self, *args: Optional[QueryParamTypes], **kwargs: Any):
        params_ = httpx.QueryParams(*args, **kwargs)
        params_dict_ = {}
        for param_k, param_v in params_.multi_items():
            if param_v.startswith('{') and param_v.endswith('}'):
                try:
                    param_v = orjson.dumps(orjson.loads(param_v)).decode()
                except orjson.JSONDecodeError:
                    pass
            params_dict_[param_k] = param_v
        super().__init__(**params_dict_)

    def add(self, key: str, value: Optional[Any] = None):
        if str(value).startswith('{') and str(value).endswith('}'):
            try:
                value = orjson.dumps(orjson.loads(value)).decode()
            except orjson.JSONDecodeError:
                pass
        return Params(super().add(key=key, value=value))

    def merge(self, params: Optional[QueryParamTypes] = None) -> "Params":
        q = Params(params)
        q._dict = {**self._dict, **q._dict}
        return q

    def __and__(self, other):
        if not (isinstance(other, httpx.QueryParams) or isinstance(other, Params)):
            other = Params(other)
        params_ = Params()
        for param_k, param_v in other.multi_items():
            params_ = params_.add(param_k, param_v)
        return params_

    @property
    def raw(self) -> str:
        return '&'.join([f'{k}={v}' for k, v in self.multi_items()])


if __name__ == '__main__':
    p = Params('foo={"foo": "bar"}')
    print(p.raw)
