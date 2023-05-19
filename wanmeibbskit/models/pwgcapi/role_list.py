from typing import List

from pydantic import BaseModel, Field


class GameRole(BaseModel):
    one_app_id: int = Field(..., alias='oneAppId')
    client_game_id: None = Field(..., alias='clientGameId')
    server_id: str = Field(..., alias='serverId')
    server_name: str = Field(..., alias='serverName')
    game_name: str = Field(..., alias='gameName')
    game_icon: str = Field(..., alias='gameIcon')
    user_id: str = Field(..., alias='userId')
    role_id: str = Field(..., alias='roleId')
    role_name: str = Field(..., alias='roleName')
    lev: int
    last_login: str = Field(..., alias='lastLogin')
    wm_uid: str = Field(..., alias='wmUid')
    is_channel: int = Field(..., alias='isChannel')
    channel_user_id: None = Field(..., alias='channelUserId')


RoleList = List[GameRole]
