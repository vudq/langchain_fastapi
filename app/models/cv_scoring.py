from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Dict


class CVScoringStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class ParsedResume(BaseModel):
    name: str
    email: str
    phone: str
    experience: List[Dict]
    skills: List[str]
    education: List[Dict]
    certifications: List[Dict]


class CVScoringRequest(BaseModel):
    parsedResume: ParsedResume
    jobDescription: str = Field(..., description="Plain text JD")


class CVScoringResponse(BaseModel):
    status: CVScoringStatus
    score: Optional[float] = None
    keyMatch: Optional[List[str]] = None
    missingSkills: Optional[List[str]] = None
    isSuccessful: bool = False
    httpResponseCode: int = 500
    error_message: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "score": 0.85,
                "keyMatch": ["Python", "FastAPI"],
                "missingSkills": ["Docker", "Kubernetes"],
                "isSuccessful": True,
                "httpResponseCode": 200
            }
        }
