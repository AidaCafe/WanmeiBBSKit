from typing import Any, Mapping, Optional, Union

from httpx import AsyncClient
from httpx import Response

from wanmeibbs.basics import HYBRID_URL
from wanmeibbs.utils import AsyncTigerTransport, URL
from wanmeibbs.utils.decorators import enforce_implementation


class WanmeiBBSClient:
    @property
    def isLogin(self):
        return self._isLogin

    def __init__(self):
        self.client = AsyncClient(
            base_url=HYBRID_URL.PWCGAPI,
            transport=AsyncTigerTransport(),
        )

        self._isLogin = False

    @classmethod
    @enforce_implementation
    def from_token(cls, user_id: int, token: str) -> "WanmeiBBSClient":
        instance_ = cls()
        return instance_

    async def request(
            self,
            url: Optional[Union[str, URL]],
            method: Optional[str] = 'GET',
            data: Optional[Mapping[str, Any]] = None,
            params: Optional[Mapping[str, Any]] = None
    ) -> Response:
        return await self.client.request(
            method=method,
            url=url,
            data=data,
            params=params
        )
