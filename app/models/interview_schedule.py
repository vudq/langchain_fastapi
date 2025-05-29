from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional


class InterviewScheduleStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class InterviewScheduleRequest(BaseModel):
    candidateId: str
    panel: List[str] = Field(..., description="List of interviewer emails or IDs")
    preferredSlots: List[str] = Field(..., description="Preferred ISO 8601 time slots")


class InterviewScheduleResponse(BaseModel):
    status: InterviewScheduleStatus
    confirmedSlot: Optional[str] = None
    suggestedSlots: Optional[List[str]] = None
    isSuccessful: bool = False
    httpResponseCode: int = 500
    error_message: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "confirmedSlot": "2025-06-10T10:00:00+07:00",
                "suggestedSlots": [],
                "isSuccessful": True,
                "httpResponseCode": 200
            }
        }
