from typing import Union

from wanmeibbskit.basics.api.pwcg import PerfectWorldAPI
from wanmeibbskit.utils.safely_getters import secure_json_retrieve
from wanmeibbskit.utils.decorators import method_need_login
from wanmeibbskit.models import CommonResponse
from wanmeibbskit.models.pwcgapi.role_list import RoleList


class BBSApp(PerfectWorldAPI):
    @method_need_login
    async def roleList(self) -> Union[CommonResponse[RoleList], None]:
        resp_ = await self.client.post(
            '/game/roleList',
            params={
                "uid": self.uid,
                "oneAppId": 1256,
            },
            headers={
                "token": self.token
            }
        )
        return CommonResponse[RoleList].parse_obj(secure_json_retrieve(resp_, restrict_status_code=True))
