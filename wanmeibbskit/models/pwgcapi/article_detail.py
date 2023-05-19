from typing import List

from pydantic import BaseModel, Field


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


class CertifyTitle(BaseModel):
    name: str
    icon: str
    ext: None


class UserInfo(BaseModel):
    uid: int
    nickname: str
    avatar: str
    vip_level: int = Field(..., alias='vipLevel')
    wm_uid: None = Field(..., alias='wmUid')
    points: None
    bg_img: str = Field(..., alias='bgImg')
    create_ip_attribution: str = Field(..., alias='createIpAttribution')
    badge_img: str = Field(..., alias='badgeImg')
    avatar_frame: None = Field(..., alias='avatarFrame')
    dress_up: None = Field(..., alias='dressUp')
    desc: str
    gender: int
    birthday: None
    role_item: None = Field(..., alias='roleItem')
    forum_role_items: None = Field(..., alias='forumRoleItems')
    forum_level: None = Field(..., alias='forumLevel')
    forum_badge: None = Field(..., alias='forumBadge')
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
    compression: None
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
    top_bg_color: str = Field(..., alias='topBgColor')
    score: int
    follower_count: int = Field(..., alias='followerCount')
    moment_count: int = Field(..., alias='momentCount')
    game_player_count: int = Field(..., alias='gamePlayerCount')
    article_unread_count: int = Field(..., alias='articleUnreadCount')
    is_recommend: int = Field(..., alias='isRecommend')
    is_followed: int = Field(..., alias='isFollowed')
    follow_day_num: None = Field(..., alias='followDayNum')


class SectionItem(BaseModel):
    section_id: int = Field(..., alias='sectionId')
    unique_code: int = Field(..., alias='uniqueCode')
    name: str
    icon: str
    bg_img: str = Field(..., alias='bgImg')
    rank: int
    type: int
    style_type: None = Field(..., alias='styleType')
    layout_type: None = Field(..., alias='layoutType')
    h5_link: None = Field(..., alias='h5Link')
    description: None
    discuss_count: int = Field(..., alias='discussCount')
    part_uid_count: int = Field(..., alias='partUidCount')
    can_publish: bool = Field(..., alias='canPublish')
    ext: None
    can_sort: bool = Field(..., alias='canSort')


class ArticleDetailData(BaseModel):
    uid: int
    article_id: int = Field(..., alias='articleId')
    title: str
    type: int
    content: str
    img_items: List[ImgItem] = Field(..., alias='imgItems')
    video: None
    snapshot: Snapshot
    snapshot_custom: None = Field(..., alias='snapshotCustom')
    user_info: UserInfo = Field(..., alias='userInfo')
    is_moment: int = Field(..., alias='isMoment')
    is_creator: int = Field(..., alias='isCreator')
    source: int
    user_ip_attribution: str = Field(..., alias='userIpAttribution')
    circle_item: CircleItem = Field(..., alias='circleItem')
    section_items: List[SectionItem] = Field(..., alias='sectionItems')
    tag_items: None = Field(..., alias='tagItems')
    content_tag_items: None = Field(..., alias='contentTagItems')
    topic_items: None = Field(..., alias='topicItems')
    at_info_items: None = Field(..., alias='atInfoItems')
    clock_in_info: None = Field(..., alias='clockInInfo')
    view_count: int = Field(..., alias='viewCount')
    like_count: int = Field(..., alias='likeCount')
    down_vote_count: int = Field(..., alias='downVoteCount')
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
    comment_mode: int = Field(..., alias='commentMode')
    can_comment: bool = Field(..., alias='canComment')
    ad_items: None = Field(..., alias='adItems')
    html: str
    complain_count: int = Field(..., alias='complainCount')
    collect_count: int = Field(..., alias='collectCount')
