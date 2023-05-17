from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


__all__ = [
    'SexEnum',
    'SmsLoginResponse',
    'SmsLoginResult',
    'UserIdentify'
]


class SexEnum(int, Enum):
    FEMALE = 0
    MALE = 1

class UserIdentify(BaseModel):
    contactInfo: str = Field(..., description="联系方式")
    sex: SexEnum = Field(..., description="性别")
    updateTime: int = Field(..., description="更新时间")
    needCheck: bool = Field(..., description="是否需要重置")
    idNumber: str = Field(..., description="身份证号")
    userId: int = Field(..., description="通行证Id")
    realName: str = Field(..., description="姓名")
    times: int = Field(..., description="身份信息更新次数?")
    facialStatus: int = Field(..., description="人脸状态")
    passport: int = Field(..., description="是否为护照")
    createTime: int = Field(..., description="身份信息创建时间")
    pi: str = Field(..., description="?")
    civicType: int = Field(..., description="是否为公民")
    age: int = Field(..., description="年龄")
    status: int = Field(..., description="身份信息状态")


class SmsLoginResult(BaseModel):
    userId: int = Field(..., description="通行证id")
    username: str = Field(..., description="用户名")
    nickname: str = Field(..., description="昵称")
    cellphone: str = Field(..., description="手机号码")
    email: str = Field(..., description="绑定邮箱")
    showCellphone: str = Field(..., description="展示手机号码")
    showEmail: str = Field(..., description="展示邮箱")
    showContactInfo: str = Field(..., description="展示联系方式")
    idCardType: int = Field(..., description="身份证类型")
    isTempUser: bool = Field(..., description="是否为临时用户") 
    expireTips: str = Field(..., description="过期提示")
    token: str = Field(..., description="登录Token")
    havePwd: bool = Field(..., description="密码设置状态")
    isActive: bool = Field(..., description="是否为激活状态")
    adult: int = Field(..., description="是否成年")
    userIdentify: UserIdentify = Field(..., description="身份信息")
    secureScore: int = Field(..., description="安全评分")
    setPwd: bool = Field(..., description="是否需要设置密码")
    setThirdCellphone: bool = Field(..., description="是否需要绑定手机号码")
    source: int = Field(..., description="账号来源")
    specialAccount: int = Field(..., description="特殊账号")
    newLogin: bool = Field(..., description="首次登录")
    tradeTime: int = Field(..., description="交易时间")
    sex: Optional[SexEnum] = Field(..., description="性别")
    isHeadImgDefault: bool = Field(..., description="是否为默认头像")
    headImg: str = Field(..., description="头像Url")
    bindRelation: Dict[str, Any] = Field(..., description="绑定关系")
    userGames: List = Field(..., description="玩家游戏列表")
    iosReviewUrl: str = Field(..., description="iOS Url")


class SmsLoginResponse(BaseModel):
    code: int = Field(..., description="请求状态")
    message: str = Field(..., description="返回信息")
    result: SmsLoginResult = Field(..., description="返回结果")
