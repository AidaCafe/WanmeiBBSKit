from typing import Any, Mapping, Optional, Union

from httpx import AsyncClient
from httpx import Response

from wanmeibbskit.basics import HYBRID_URL
from wanmeibbskit.utils import AsyncTigerTransport, URL
from wanmeibbskit.utils.decorators import enforce_implementation


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
    def from_token(cls, token: str) -> "WanmeiBBSClient":
        instance_ = cls()
        instance_.login_data = ...
        return instance_

    async def request(
            self,
            url: Union[str, URL],
            method: str = 'GET',
            data: Optional[Mapping[str, Any]] = None,
            params: Optional[Mapping[str, Any]] = None
    ) -> Response:
        return await self.client.request(
            method=method,
            url=url,
            data=data,
            params=params
        )
