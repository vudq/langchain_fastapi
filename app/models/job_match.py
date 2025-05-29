from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Dict


class JobMatchStatus(str, Enum):
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


class JobMatchRequest(BaseModel):
    candidateId: Optional[str] = None
    parsedResume: Optional[ParsedResume] = None

    class Config:
        schema_extra = {
            "example": {
                "candidateId": "abc123"
            }
        }


class JobMatchItem(BaseModel):
    jobId: str
    title: str
    matchScore: float


class JobMatchResponse(BaseModel):
    status: JobMatchStatus
    matches: Optional[List[JobMatchItem]] = None
    isSuccessful: bool = False
    httpResponseCode: int = 500
    error_message: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "matches": [
                    {
                        "jobId": "job001",
                        "title": "Senior Backend Developer",
                        "matchScore": 0.92
                    },
                    {
                        "jobId": "job002",
                        "title": "Software Engineer",
                        "matchScore": 0.86
                    }
                ],
                "isSuccessful": True,
                "httpResponseCode": 200
            }
        }
