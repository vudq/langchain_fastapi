from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional


class OfferLetterStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class AutoOfferLetterRequest(BaseModel):
    candidateId: str
    jobId: str
    salary: float
    startDate: str
    benefits: List[str]


class AutoOfferLetterResponse(BaseModel):
    status: OfferLetterStatus
    offerLetter: Optional[str] = None
    isSuccessful: bool = False
    httpResponseCode: int = 500
    error_message: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "offerLetter": "<html>...</html>",
                "isSuccessful": True,
                "httpResponseCode": 200
            }
        }
