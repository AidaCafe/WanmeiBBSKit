from typing import Union, Optional

from wanmeibbskit.basics.api.pwcg import PerfectWorldAPI
from wanmeibbskit.models.pwcgapi.article_detail import ArticleDetailData
from wanmeibbskit.models.pwcgapi.other_articles import OtherArticles
from wanmeibbskit.models.pwcgapi.user_unread_message import UnreadMessageData
from wanmeibbskit.utils.safely_getters import secure_json_retrieve
from wanmeibbskit.utils.decorators import method_need_login
from wanmeibbskit.models import CommonResponse
from wanmeibbskit.models.pwcgapi.role_list import RoleList
from wanmeibbskit.models.pwcgapi.user_detail import UserDetailData
from wanmeibbskit.models.pwcgapi.other_detail import OtherDetailData


class BBSApp(PerfectWorldAPI):
    @method_need_login
    async def getRoleList(self) -> CommonResponse[RoleList]:
        """
        获取当前登录账号名下的所有游戏信息
        :return: 已序列化的、完整的返回值, result是一个models.pwcgapi.RoleList对象
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
    async def getUserDetail(self) -> CommonResponse[UserDetailData]:
        """
        获取自己的论坛用户信息
        :return: 已序列化的、完整的返回值, result是一个models.pwcgapi.UserDetailData对象
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
    async def getOtherDetail(self, other_uid: int) -> CommonResponse[OtherDetailData]:
        """
        获取他人的论坛用户信息
        :param other_uid: 论坛用户id
        :return: 已序列化的、完整的返回值, result是一个models.pwcgapi.OtherDetailData对象
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
    async def getUnreadMessage(self) -> CommonResponse[UnreadMessageData]:
        """
        获取论坛未读消息
        :return: 已序列化的、完整的返回值, result是一个models.pwcgapi.UnreadMessageData对象
        """
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

    @method_need_login
    async def getArticleDetail(self, article_id: int) -> CommonResponse[ArticleDetailData]:
        """
        获取文章详情
        :param article_id: 社区文章id
        :return: 已序列化的、完整的返回值, result是一个models.pwcgapi.ArticleDetailData对象
        """
        resp_ = await self.client.post(
            '/article/viewDetail',
            params={
                "uid": self.uid,
                "articleId": article_id
            },
            headers={
                "token": self.token,
            }
        )

        return CommonResponse[ArticleDetailData].parse_obj(secure_json_retrieve(resp_))

    @method_need_login
    async def getOtherArticles(
            self,
            other_uid: int,
            page_size: Optional[int] = 10,
            page_num: Optional[int] = 1
    ) -> CommonResponse[OtherArticles]:
        """
        获取论坛用户的所有文章列表
        :param other_uid: 论坛用户id
        :param page_size: 每页的文章数量
        :param page_num: 页数
        :return: 已序列化的、完整的返回值, result是一个models.pwcgapi.OtherArticles对象
        """
        resp_ = await self.client.post(
            'article/pageOther',
            params={
                "uid": self.uid,
                "otherUid": other_uid,
                "pageSize": page_size,
                "pageNum": page_num
            }
        )

        return CommonResponse[OtherArticles].parse_obj(secure_json_retrieve(resp_))
