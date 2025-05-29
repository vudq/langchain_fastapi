from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Dict


class CVParseAndScoreStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class CVParseAndScoreRequest(BaseModel):
    jobDescription: str = Field(..., description="Job description for scoring")


class CVParseAndScoreResponse(BaseModel):
    status: CVParseAndScoreStatus
    parsedResume: Optional[Dict] = None
    score: Optional[float] = None
    keyMatch: Optional[List[str]] = None
    missingSkills: Optional[List[str]] = None
    isSuccessful: bool = False
    httpResponseCode: int = 500
    error_message: Optional[str] = None
