from typing import List, Optional

from pydantic import BaseModel, Field


class UnreadMessageItem(BaseModel):
    message_type: int = Field(..., alias='messageType')
    unread_count: int = Field(..., alias='unreadCount')
    message: Optional[str]
    create_timestamp: Optional[int] = Field(..., alias='createTimestamp')


class UnreadMessageData(BaseModel):
    unread_total_count: int = Field(..., alias='unreadTotalCount')
    unread_message_items: List[UnreadMessageItem] = Field(
        ..., alias='unreadMessageItems'
    )
