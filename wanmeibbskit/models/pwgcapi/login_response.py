from typing import List, Optional, Union

from pydantic import BaseModel, Field


class ImToken(BaseModel):
    im_app_id: str = Field(..., alias='imAppId')
    im_client_key: str = Field(..., alias='imClientKey')
    token: str
    refresh_token: str = Field(..., alias='refreshToken')
    expire: int


class WorldImToken(BaseModel):
    im_app_id: str = Field(..., alias='imAppId')
    im_client_key: str = Field(..., alias='imClientKey')
    token: str
    refresh_token: str = Field(..., alias='refreshToken')
    expire: int


class ZxqsjImToken(BaseModel):
    im_app_id: str = Field(..., alias='imAppId')
    im_client_key: str = Field(..., alias='imClientKey')
    token: str
    refresh_token: str = Field(..., alias='refreshToken')
    expire: int


class Zx2ImToken(BaseModel):
    im_app_id: str = Field(..., alias='imAppId')
    im_client_key: str = Field(..., alias='imClientKey')
    token: str
    refresh_token: str = Field(..., alias='refreshToken')
    expire: int


class BgVideoSnapshot(BaseModel):
    thumbnail: str
    url: str
    compression: None
    width: int
    height: int


class ExtItem(BaseModel):
    can_sort: Union[int, str] = Field(..., alias='canSort')
    ad_target_types: Optional[str] = Field(None, alias='adTargetTypes')


class SectionItem(BaseModel):
    section_id: int = Field(..., alias='sectionId')
    unique_code: int = Field(..., alias='uniqueCode')
    name: str
    icon: str
    bg_img: str = Field(..., alias='bgImg')
    rank: int
    type: int
    style_type: Optional[int] = Field(..., alias='styleType')
    layout_type: None = Field(..., alias='layoutType')
    h5_link: None = Field(..., alias='h5Link')
    description: None
    discuss_count: int = Field(..., alias='discussCount')
    part_uid_count: int = Field(..., alias='partUidCount')
    can_publish: bool = Field(..., alias='canPublish')
    ext: Optional[ExtItem]
    can_sort: bool = Field(..., alias='canSort')


class SectionItem1(BaseModel):
    section_id: int = Field(..., alias='sectionId')
    unique_code: int = Field(..., alias='uniqueCode')
    name: str
    icon: str
    bg_img: str = Field(..., alias='bgImg')
    rank: int
    type: int
    style_type: Optional[int] = Field(..., alias='styleType')
    layout_type: None = Field(..., alias='layoutType')
    h5_link: None = Field(..., alias='h5Link')
    description: None
    discuss_count: int = Field(..., alias='discussCount')
    part_uid_count: int = Field(..., alias='partUidCount')
    can_publish: bool = Field(..., alias='canPublish')
    ext: Optional[ExtItem]
    can_sort: bool = Field(..., alias='canSort')


class SectionCateItem(BaseModel):
    section_cate_id: int = Field(..., alias='sectionCateId')
    name: str
    section_items: List[SectionItem1] = Field(..., alias='sectionItems')


class CircleViewing(BaseModel):
    circle_id: int = Field(..., alias='circleId')
    type: int
    title: str
    game_id: int = Field(..., alias='gameId')
    game_type: int = Field(..., alias='gameType')
    attr_type: int = Field(..., alias='attrType')
    is_default: int = Field(..., alias='isDefault')
    rank: int
    icon: str
    bg_img: str = Field(..., alias='bgImg')
    pc_bg_img: str = Field(..., alias='pcBgImg')
    guide_bg_img: str = Field(..., alias='guideBgImg')
    bg_video: str = Field(..., alias='bgVideo')
    bg_video_snapshot: BgVideoSnapshot = Field(..., alias='bgVideoSnapshot')
    top_bg_color: str = Field(..., alias='topBgColor')
    score: int
    follower_count: int = Field(..., alias='followerCount')
    moment_count: int = Field(..., alias='momentCount')
    game_player_count: int = Field(..., alias='gamePlayerCount')
    article_unread_count: int = Field(..., alias='articleUnreadCount')
    is_recommend: int = Field(..., alias='isRecommend')
    is_followed: int = Field(..., alias='isFollowed')
    follow_day_num: int = Field(..., alias='followDayNum')
    section_items: List[SectionItem] = Field(..., alias='sectionItems')
    section_cate_items: List[SectionCateItem] = Field(..., alias='sectionCateItems')


class ZxqsjImChannelVo(BaseModel):
    channel_id: str = Field(..., alias='channelId')
    channel_name: str = Field(..., alias='channelName')
    type: int


class Zx2ImChannelVoListItem(BaseModel):
    channel_id: str = Field(..., alias='channelId')
    channel_name: str = Field(..., alias='channelName')
    type: int


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
    game_name: None = Field(..., alias='gameName')
    game_icon: None = Field(..., alias='gameIcon')


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
    ext: None


class ForumUserInfoListItem(BaseModel):
    circle_id: int = Field(..., alias='circleId')
    auditing_article_count: int = Field(..., alias='auditingArticleCount')
    role_item: Optional[RoleItemItem] = Field(..., alias='roleItem')
    forum_authority: ForumAuthority = Field(..., alias='forumAuthority')
    forum_role_names: List = Field(..., alias='forumRoleNames')
    forum_badges_reached: List[ForumBadgesReachedItem] = Field(
        ..., alias='forumBadgesReached'
    )
    forum_level: None = Field(..., alias='forumLevel')
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


class LoginData(BaseModel):
    """
    From PWCGAPI/login/v2
    """
    uid: int
    nickname: str
    avatar: str
    wm_uid: None = Field(..., alias='wmUid')
    bg_img: None = Field(..., alias='bgImg')
    create_ip_attribution: str = Field(..., alias='createIpAttribution')
    desc: str
    gender: None
    birthday: None
    im_token: ImToken = Field(..., alias='imToken')
    world_im_token: WorldImToken = Field(..., alias='worldImToken')
    zxqsj_im_token: ZxqsjImToken = Field(..., alias='zxqsjImToken')
    zx2_im_token: Zx2ImToken = Field(..., alias='zx2ImToken')
    is_new: bool = Field(..., alias='isNew')
    is_need_change_name: bool = Field(..., alias='isNeedChangeName')
    circle_viewing: CircleViewing = Field(..., alias='circleViewing')
    zxqsj_im_channel_vo: ZxqsjImChannelVo = Field(..., alias='zxqsjImChannelVo')
    zx2_im_channel_vo_list: List[Zx2ImChannelVoListItem] = Field(
        ..., alias='zx2ImChannelVoList'
    )
    forum_user_info_list: List[ForumUserInfoListItem] = Field(
        ..., alias='forumUserInfoList'
    )
