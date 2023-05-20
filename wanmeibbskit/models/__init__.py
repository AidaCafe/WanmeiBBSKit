from enum import Enum
from typing import (
    AbstractSet,
    Any,
    Callable,
    Generic,
    Mapping,
    Optional,
    TypeVar
)
from typing import cast

import orjson
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

__all__ = [
    'CommonResponse',
    'CompactJsonModel',
    'AllStringCompactJsonModel',
]

Result = TypeVar("Result", bound=BaseModel)


def compact_dumps(__obj: dict, default, **orjson_kwargs) -> str:
    return orjson.dumps(__obj, default=default, **orjson_kwargs).decode()


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


class CommonResponse(GenericModel, Generic[Result]):
    traceid: Optional[str] = Field(..., description='追踪Id')
    code: int = Field(..., description='请求状态Id')
    message: str = Field(..., description='请求状态信息')
    result: Optional[Result] = Field(..., description='请求结果')
    env: Optional[str] = Field(..., description='运行环境')
