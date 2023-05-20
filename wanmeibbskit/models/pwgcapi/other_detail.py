from typing import List, Optional, Any

from pydantic import BaseModel, Field, HttpUrl


class RoleItem(BaseModel):
    one_app_id: int = Field(..., alias='oneAppId')
    uid: int
    server_id: str = Field(..., alias='serverId')
    server_name: str = Field(..., alias='serverName')
    role_avatar: Optional[HttpUrl] = Field(..., alias='roleAvatar')
    role_id: str = Field(..., alias='roleId')
    role_name: str = Field(..., alias='roleName')
    level: int
    gender: int
    occupation: int
    race: str
    career: str
    is_bound: int = Field(..., alias='isBound')
    game_name: str = Field(..., alias='gameName')
    game_icon: str = Field(..., alias='gameIcon')


class ForumBadgesReachedItem(BaseModel):
    id: int
    name: str
    icon: str
    lighten_img: str = Field(..., alias='lightenImg')
    grey_img: str = Field(..., alias='greyImg')
    sort_no: int = Field(..., alias='sortNo')
    remark: str
    wear_status: int = Field(..., alias='wearStatus')
    reach_time: int = Field(..., alias='reachTime')
    ext: Optional[dict]


class CertifyTitle(BaseModel):
    name: str
    icon: str
    ext: Optional[dict]


class ForumLevelData(BaseModel):
    name: str
    level: int
    level_text: str = Field(..., alias='levelText')
    require_exp: int = Field(..., alias='requireExperiencePoints')
    icon: Optional[str]
    ext: Optional[dict]


class ForumUserInfoListItem(BaseModel):
    circle_id: int = Field(..., alias='circleId')
    auditing_article_count: int = Field(..., alias='auditingArticleCount')
    role_item: RoleItem = Field(..., alias='roleItem')
    forum_authority: Optional[str] = Field(..., alias='forumAuthority')
    forum_role_names: List[str] = Field(..., alias='forumRoleNames')
    forum_badges_reached: List[ForumBadgesReachedItem] = Field(
        ..., alias='forumBadgesReached'
    )
    forum_level: Optional[ForumLevelData] = Field(..., alias='forumLevel')
    forum_virtual_currency_balance: int = Field(
        ..., alias='forumVirtualCurrencyBalance'
    )
    forum_experience_points_balance: int = Field(
        ..., alias='forumExperiencePointsBalance'
    )
    forum_reached_achieve_stages: int = Field(..., alias='forumReachedAchieveStages')
    dress_up: Optional[bool] = Field(..., alias='dressUp')
    has_certify_creator_role: bool = Field(..., alias='hasCertifyCreatorRole')
    certify_titles: List[CertifyTitle] = Field(..., alias='certifyTitles')


class OtherDetailData(BaseModel):
    uid: int
    nickname: str
    avatar: str
    wm_uid: Optional[str] = Field(..., alias='wmUid')
    bg_img: Optional[HttpUrl] = Field(..., alias='bgImg')
    create_ip_attribution: str = Field(..., alias='createIpAttribution')
    desc: str
    gender: int
    birthday: int
    follower_count: int = Field(..., alias='followerCount')
    like_count: int = Field(..., alias='likeCount')
    follow_count: int = Field(..., alias='followCount')
    is_followed: bool = Field(..., alias='isFollowed')
    is_fan: bool = Field(..., alias='isFan')
    is_block: bool = Field(..., alias='isBlock')
    article_count: int = Field(..., alias='articleCount')
    article_view_count: int = Field(..., alias='articleViewCount')
    comment_count: int = Field(..., alias='commentCount')
    show_im_button: bool = Field(..., alias='showImButton')
    area_item: Optional[Any] = Field(..., alias='areaItem')
    avatar_frame: Optional[HttpUrl] = Field(..., alias='avatarFrame')
    forum_user_info_list: List[ForumUserInfoListItem] = Field(
        ..., alias='forumUserInfoList'
    )
    user_follow_forum_list: None = Field(..., alias='userFollowForumList')
