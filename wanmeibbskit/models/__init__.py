import json
from enum import Enum
from typing import cast
from typing import (
    AbstractSet,
    Any,
    Callable,
    Mapping,
    Optional
)

from pydantic import BaseModel


__all__ = [
    'CompactJsonModel',
    'AllStringCompactJsonModel',
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


class AllStringCompactJsonModel(CompactJsonModel):
    def json(
            self,
            *,
            include: AbstractSet[int | str] | Mapping[int | str, Any] | None = None,
            exclude: AbstractSet[int | str] | Mapping[int | str, Any] | None = None,
            by_alias: bool = False,
            skip_defaults: bool | None = None,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
            encoder: Optional[Callable[[Any], Any]] = None,
            **dumps_kwargs
    ) -> str:
        dict_ = super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none
        )
        for k, v in dict_.items():
            if isinstance(v, int):
                if isinstance(v, Enum):
                    v = v.value
                dict_[k] = str(v)

        encoder = cast(Callable[[Any], Any], encoder or self.__json_encoder__)

        return self.__config__.json_dumps(
            dict_, default=encoder, **dumps_kwargs
        )
