from typing import List, Optional

from pydantic import BaseModel, Field

__all__ = [
    'Arena',
    'CommonItem',
    'ExplorationInfo',
    'RoleData',
    'SubExplorationInfo',
    'WeaponCate',
    'WeaponInfo',
]


class CommonItem(BaseModel):
    key: str = Field(..., description='类型Key')
    name: str = Field(..., description='名称')
    value: str = Field(..., description='值')
    img: Optional[str] = Field(..., description='图标Url')


class Arena(BaseModel):
    key: str = Field(..., description='爬塔类型Key')
    name: Optional[str] = Field(..., description='爬塔名称')
    value: str = Field(..., description='爬塔层数')
    img: Optional[str] = Field(..., description='爬塔图标')
    brief: Optional[str] = Field(..., description='展示短语')


class WeaponInfo(BaseModel):
    id: int = Field(..., description='武器Id')
    level: int = Field(..., alias='lev', description='武器等级')
    star: int = Field(..., description='武器星级')
    color: int = Field(..., description='武器颜色')
    name: Optional[str] = Field(..., description='武器名称')
    img: Optional[str] = Field(..., description='武器图标Url')
    cate_id: Optional[int] = Field(..., alias='cateId')


class WeaponCate(BaseModel):
    id: int = Field(..., description='武器属性Id')
    title: str = Field(..., description='属性名称')


class SubExplorationInfo(BaseModel):
    key: str = Field(..., description='地区Key')
    name: Optional[str] = Field(..., description='地区名称')
    value: str = Field(..., description='地区探索度百分比')
    img: Optional[str] = Field(..., description='地区图标')
    current: int = Field(..., description='当前探索度计数')
    total: int = Field(..., description='满探索度计数')
    children: List[Optional["SubExplorationInfo"]] = Field(..., description='子地区探索度')


class ExplorationInfo(BaseModel):
    key: str = Field(..., description='时空Key')
    name: Optional[str] = Field(..., description='时空名称')
    value: float = Field(..., description='时空探索度百分比')
    img: Optional[str] = Field(..., description='时空图标')
    current: int = Field(..., description='当前探索度计数')
    total: int = Field(..., description='满探索度计数')
    children: List[SubExplorationInfo] = Field(..., description='子地区探索度')


class RoleData(BaseModel):
    uid: int = Field(..., description='用户Id')
    game_uid: str = Field(..., alias='gameUid', description='游戏Id')
    name: str = Field(..., description='游戏内角色名称')
    level: int = Field(..., alias='lev', description="角色等级")
    server_id: int = Field(..., alias='serverId', description='服务器Id')
    gs: int = Field(..., description='战力')
    days: int = Field(..., description='活跃天数')
    role_id: int = Field(..., alias='roleId', description='角色Id')
    fight_info: List[CommonItem] = Field(..., alias='fightInfo', description='面板信息')
    achievements: List[CommonItem] = Field(..., alias='achInfo', description='成就信息')
    currency: List[CommonItem] = Field(..., description='货币信息')
    arena: List[Arena] = Field(..., description='爬塔信息')
    weapon_info: List[WeaponInfo] = Field(..., alias='weaponInfo', description='武器信息')
    weapon_cate: List[WeaponCate] = Field(..., alias='weaponCate', description='武器属性')
    explorations: List[ExplorationInfo] = Field(..., alias='towerInfo', description='探索度信息')
