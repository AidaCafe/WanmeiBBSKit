from typing import Any, List, Optional

from pydantic import BaseModel, Field, HttpUrl


class ImgItem(BaseModel):
    thumbnail: str
    url: str
    compression: str
    width: int
    height: int


class Snapshot(BaseModel):
    thumbnail: str
    url: str
    compression: str
    width: int
    height: int


class RoleItem(BaseModel):
    one_app_id: Optional[int] = Field(..., alias='oneAppId')
    uid: int
    server_id: str = Field(..., alias='serverId')
    server_name: str = Field(..., alias='serverName')
    role_avatar: None = Field(..., alias='roleAvatar')
    role_id: str = Field(..., alias='roleId')
    role_name: str = Field(..., alias='roleName')
    level: int
    gender: Optional[int]
    occupation: Optional[Any]
    race: Optional[Any]
    career: Optional[Any]
    is_bound: Optional[bool] = Field(..., alias='isBound')
    game_name: str = Field(..., alias='gameName')
    game_icon: str = Field(..., alias='gameIcon')


class CertifyTitle(BaseModel):
    name: str
    icon: str
    ext: None


class UserInfo(BaseModel):
    uid: int
    nickname: str
    avatar: str
    vip_level: int = Field(..., alias='vipLevel')
    wm_uid: Optional[str] = Field(..., alias='wmUid')
    points: Optional[int]
    bg_img: Optional[HttpUrl] = Field(..., alias='bgImg')
    create_ip_attribution: str = Field(..., alias='createIpAttribution')
    badge_img: None = Field(..., alias='badgeImg')
    avatar_frame: None = Field(..., alias='avatarFrame')
    dress_up: None = Field(..., alias='dressUp')
    desc: str
    gender: int
    birthday: int
    role_item: RoleItem = Field(..., alias='roleItem')
    forum_role_items: None = Field(..., alias='forumRoleItems')
    forum_level: Optional[int] = Field(..., alias='forumLevel')
    forum_badge: Optional[HttpUrl] = Field(..., alias='forumBadge')
    forum_badges: List = Field(..., alias='forumBadges')
    certify_titles: List[CertifyTitle] = Field(..., alias='certifyTitles')
    is_followed: bool = Field(..., alias='isFollowed')
    is_follow_me: bool = Field(..., alias='isFollowMe')
    follower_count: int = Field(..., alias='followerCount')
    forum_role_names: List[str] = Field(..., alias='forumRoleNames')
    gender_show_status: int = Field(..., alias='genderShowStatus')


class BgVideoSnapshot(BaseModel):
    thumbnail: str
    url: str
    compression: Optional[str]
    width: int
    height: int


class CircleItem(BaseModel):
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
    top_bg_color: Optional[str] = Field(..., alias='topBgColor')
    score: int
    follower_count: int = Field(..., alias='followerCount')
    moment_count: int = Field(..., alias='momentCount')
    game_player_count: int = Field(..., alias='gamePlayerCount')
    article_unread_count: int = Field(..., alias='articleUnreadCount')
    is_recommend: int = Field(..., alias='isRecommend')
    is_followed: int = Field(..., alias='isFollowed')
    follow_day_num: Optional[int] = Field(..., alias='followDayNum')


class SectionItem(BaseModel):
    section_id: int = Field(..., alias='sectionId')
    unique_code: int = Field(..., alias='uniqueCode')
    name: str
    icon: str
    bg_img: str = Field(..., alias='bgImg')
    rank: int
    type: int
    style_type: int = Field(..., alias='styleType')
    layout_type: Optional[int] = Field(..., alias='layoutType')
    h5_link: Optional[HttpUrl] = Field(..., alias='h5Link')
    description: Optional[str]
    discuss_count: int = Field(..., alias='discussCount')
    part_uid_count: int = Field(..., alias='partUidCount')
    can_publish: bool = Field(..., alias='canPublish')
    ext: Optional[dict]
    can_sort: bool = Field(..., alias='canSort')


class TopicItem(BaseModel):
    topic_id: int = Field(..., alias='topicId')
    title: str
    desc: str
    icon: str
    bg_img: str = Field(..., alias='bgImg')
    type: int
    attr_type: int = Field(..., alias='attrType')
    status: int
    circle_id: int = Field(..., alias='circleId')
    circle_name: str = Field(..., alias='circleName')
    circle_icon: str = Field(..., alias='circleIcon')
    is_default: int = Field(..., alias='isDefault')
    topic_type: int = Field(..., alias='topicType')
    rule: None
    ext: Optional[dict]
    score: int


class Datum(BaseModel):
    uid: int
    article_id: int = Field(..., alias='articleId')
    title: str
    type: int
    content: str
    img_items: List[ImgItem] = Field(..., alias='imgItems')
    video: str
    snapshot: Snapshot
    snapshot_custom: None = Field(..., alias='snapshotCustom')
    user_info: UserInfo = Field(..., alias='userInfo')
    is_moment: int = Field(..., alias='isMoment')
    is_creator: int = Field(..., alias='isCreator')
    source: int
    user_ip_attribution: str = Field(..., alias='userIpAttribution')
    circle_item: CircleItem = Field(..., alias='circleItem')
    section_items: List[SectionItem] = Field(..., alias='sectionItems')
    tag_items: Optional[List[Any]] = Field(..., alias='tagItems')
    content_tag_items: None = Field(..., alias='contentTagItems')
    topic_items: List[TopicItem] = Field(..., alias='topicItems')
    at_info_items: Optional[List[Any]] = Field(..., alias='atInfoItems')
    clock_in_info: None = Field(..., alias='clockInInfo')
    view_count: int = Field(..., alias='viewCount')
    like_count: int = Field(..., alias='likeCount')
    down_vote_count: None = Field(..., alias='downVoteCount')
    share_count: int = Field(..., alias='shareCount')
    comment_count: int = Field(..., alias='commentCount')
    video_play_count: int = Field(..., alias='videoPlayCount')
    is_liked: bool = Field(..., alias='isLiked')
    is_down_voted: bool = Field(..., alias='isDownVoted')
    is_collected: bool = Field(..., alias='isCollected')
    is_high_quality: int = Field(..., alias='isHighQuality')
    is_top_author: int = Field(..., alias='isTopAuthor')
    is_forward: int = Field(..., alias='isForward')
    forward_id: None = Field(..., alias='forwardId')
    forward_orig_id: None = Field(..., alias='forwardOrigId')
    forward_orig_article: None = Field(..., alias='forwardOrigArticle')
    fake_alias: None = Field(..., alias='fakeAlias')
    create_time: str = Field(..., alias='createTime')
    create_date_time: int = Field(..., alias='createDateTime')
    update_time: str = Field(..., alias='updateTime')
    create_time_sec: int = Field(..., alias='createTimeSec')
    update_time_sec: int = Field(..., alias='updateTimeSec')
    vote_info: None = Field(..., alias='voteInfo')
    comment_mode: None = Field(..., alias='commentMode')
    can_comment: None = Field(..., alias='canComment')
    ad_items: None = Field(..., alias='adItems')
    hot_comment: None = Field(..., alias='hotComment')


class OtherArticles(BaseModel):
    page_num: int = Field(..., alias='pageNum')
    page_size: int = Field(..., alias='pageSize')
    total: int
    data: List[Datum]
    has_more: bool = Field(..., alias='hasMore')
