from typing import List, Optional

from pydantic import BaseModel, Field


class RoleItemItem(BaseModel):
    one_app_id: int = Field(..., alias='oneAppId')
    uid: int
    server_id: str = Field(..., alias='serverId')
    server_name: str = Field(..., alias='serverName')
    role_avatar: None = Field(..., alias='roleAvatar')
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


class ForumAuthority(BaseModel):
    can_forbid_im_channel: bool = Field(..., alias='canForbidImChannel')
    can_forbid_user: bool = Field(..., alias='canForbidUser')
    can_forbid_user_and_clear_content: bool = Field(
        ..., alias='canForbidUserAndClearContent'
    )
    can_show_im_channel: bool = Field(..., alias='canShowImChannel')
    can_show_dev_tools: bool = Field(..., alias='canShowDevTools')
    can_access_certified_writing_center: bool = Field(
        ..., alias='canAccessCertifiedWritingCenter'
    )


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


class ForumLevelItem(BaseModel):
    name: str
    level: int
    level_text: str = Field(..., alias='levelText')
    require_experience_points: int = Field(..., alias='requireExperiencePoints')
    icon: str
    ext: Optional[dict]


class ForumUserInfoListItem(BaseModel):
    circle_id: int = Field(..., alias='circleId')
    auditing_article_count: int = Field(..., alias='auditingArticleCount')
    role_item: Optional[RoleItemItem] = Field(..., alias='roleItem')
    forum_authority: ForumAuthority = Field(..., alias='forumAuthority')
    forum_role_names: List = Field(..., alias='forumRoleNames')
    forum_badges_reached: List[ForumBadgesReachedItem] = Field(
        ..., alias='forumBadgesReached'
    )
    forum_level: Optional[ForumLevelItem] = Field(..., alias='forumLevel')
    forum_virtual_currency_balance: int = Field(
        ..., alias='forumVirtualCurrencyBalance'
    )
    forum_experience_points_balance: int = Field(
        ..., alias='forumExperiencePointsBalance'
    )
    forum_reached_achieve_stages: Optional[int] = Field(
        ..., alias='forumReachedAchieveStages'
    )
    dress_up: None = Field(..., alias='dressUp')
    has_certify_creator_role: bool = Field(..., alias='hasCertifyCreatorRole')
    certify_titles: None = Field(..., alias='certifyTitles')


class UserFollowForumListItem(BaseModel):
    circle_id: int = Field(..., alias='circleId')
    game_id: int = Field(..., alias='gameId')
    forum_id: int = Field(..., alias='forumId')
    forum_name: str = Field(..., alias='forumName')
    level: int
    level_text: str = Field(..., alias='levelText')
    level_name: str = Field(..., alias='levelName')


class Watermark(BaseModel):
    thumbnail: None
    url: str
    compression: None
    width: int
    height: int


class UserDetailData(BaseModel):
    uid: int
    nickname: str
    avatar: str
    wm_uid: Optional[int] = Field(..., alias='wmUid')
    bg_img: Optional[str] = Field(..., alias='bgImg')
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
    show_im_button: None = Field(..., alias='showImButton')
    area_item: None = Field(..., alias='areaItem')
    avatar_frame: None = Field(..., alias='avatarFrame')
    forum_user_info_list: List[ForumUserInfoListItem] = Field(
        ..., alias='forumUserInfoList'
    )
    user_follow_forum_list: List[UserFollowForumListItem] = Field(
        ..., alias='userFollowForumList'
    )
    watermark_status: int = Field(..., alias='watermarkStatus')
    article_sync_im_status: int = Field(..., alias='articleSyncImStatus')
    gender_show_status: int = Field(..., alias='genderShowStatus')
    birthday_show_status: int = Field(..., alias='birthdayShowStatus')
    area_show_status: int = Field(..., alias='areaShowStatus')
    watermark: Watermark
    total_cash: int = Field(..., alias='totalCash')
    vip_level: int = Field(..., alias='vipLevel')
