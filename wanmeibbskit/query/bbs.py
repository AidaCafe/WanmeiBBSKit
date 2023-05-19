from typing import Union

from wanmeibbskit.basics.api.pwcg import PerfectWorldAPI
from wanmeibbskit.models.pwcgapi.user_unread_message import UnreadMessageData
from wanmeibbskit.utils.safely_getters import secure_json_retrieve
from wanmeibbskit.utils.decorators import method_need_login
from wanmeibbskit.models import CommonResponse
from wanmeibbskit.models.pwcgapi.role_list import RoleList
from wanmeibbskit.models.pwcgapi.user_detail import UserDetailData
from wanmeibbskit.models.pwcgapi.other_detail import OtherDetailData


class BBSApp(PerfectWorldAPI):
    @method_need_login
    async def getRoleList(self) -> Union[CommonResponse[RoleList], None]:
        """
        获取当前登录账号名下的所有游戏信息
        :return: 已序列化的、完整的返回值
        """
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

    @method_need_login
    async def getUserDetail(self) -> Union[CommonResponse[UserDetailData], None]:
        """
        获取自己的论坛用户信息
        :return: 已序列化的、完整的返回值
        """
        resp_ = await self.client.post(
            '/user/getDetail/v2',
            params={
                "uid": self.uid
            },
            headers={
                "token": self.token
            }
        )

        return CommonResponse[UserDetailData].parse_obj(secure_json_retrieve(resp_))

    @method_need_login
    async def getOtherDetail(self, other_uid: int) -> Union[CommonResponse[OtherDetailData], None]:
        """
        获取他人的论坛用户信息
        :param other_uid: 他人的论坛uid
        :return: 已序列化的、完整的返回值
        """
        resp_ = await self.client.post(
            '/user/getOtherDetail/v2',
            params={
                "uid": self.uid,
                "otherUid": other_uid
            },
            headers={
                "token": self.token
            }
        )

        return CommonResponse[OtherDetailData].parse_obj(secure_json_retrieve(resp_))

    @method_need_login
    async def getUnreadMessage(self) -> Union[CommonResponse[UnreadMessageData], None]:
        resp_ = await self.client.post(
            '/user/getUnreadMessage',
            params={
                "uid": self.uid
            },
            headers={
                "token": self.token
            }
        )

        return CommonResponse[UnreadMessageData].parse_obj(secure_json_retrieve(resp_))
