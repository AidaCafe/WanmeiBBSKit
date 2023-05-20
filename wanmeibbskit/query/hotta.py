from typing import Optional

from wanmeibbskit.models import CommonResponse
from wanmeibbskit.models.hotta import RoleData
from wanmeibbskit.utils.decorators import method_need_login
from wanmeibbskit.utils.safely_getters import secure_json_retrieve
from .bbs import BBSApp
from ..exceptions import GameNotMatch


class HottaClient(BBSApp):
    @method_need_login
    async def getRoleData(
            self,
            uid: Optional[int] = None,
            role_id: Optional[int] = None
    ) -> CommonResponse[RoleData]:
        if not uid:
            uid = self.uid
        if not role_id:
            if uid == self.uid:
                role_data = (await self.getUserDetail()).result
            else:
                role_data = (await self.getOtherDetail(other_uid=uid)).result
            if role_data.forum_user_info_list[0].role_item.game_name != '幻塔':
                raise GameNotMatch('The game of default role does not match hotta.')
            role_id = role_data.forum_user_info_list[0].role_item.role_id
        resp_ = await self.client.post(
            '/doc/getRoleData',
            params={
                "uid": uid,
                "roleId": role_id,
                "circleId": 1,
            },
            headers={
                "token": self.token
            }
        )
        return CommonResponse[RoleData].parse_obj(secure_json_retrieve(resp_))

    @method_need_login
    async def getSignGifts(self):
        resp_ = await self.client.post(
            '/shop/item/signGiftByOneAppId',
            params={
                "uid": self.uid,
                "oneAppId": 1256,
                "storeId": 10
            },
            headers={
                "token": self.token
            }
        )

        return secure_json_retrieve(resp_)
