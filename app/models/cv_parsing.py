from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from typing import List, Optional, Dict


class CVParsingStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class ExperienceItem(BaseModel):
    position: str
    company: str
    start_date: str
    end_date: Optional[str]


class EducationItem(BaseModel):
    degree: str
    institution: str
    start_date: str
    end_date: str


class CertificationItem(BaseModel):
    name: str
    issuer: str
    date: str


class CVParsingRequest(BaseModel):
    file: str = Field(..., description="Base64-encoded CV PDF file")


class CVParsingResponse(BaseModel):
    status: CVParsingStatus
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    experience: Optional[List[ExperienceItem]] = None
    skills: Optional[List[str]] = None
    education: Optional[List[EducationItem]] = None
    certifications: Optional[List[CertificationItem]] = None
    isSuccessful: bool = False
    httpResponseCode: int = 500
    error_message: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "name": "Nguyen Van A",
                "email": "vana@gmail.com",
                "phone": "+84901234567",
                "experience": [
                    {
                        "position": "Backend Developer",
                        "company": "FPT Software",
                        "start_date": "2020-01-01",
                        "end_date": "2022-03-31"
                    }
                ],
                "skills": ["Python", "FastAPI", "PostgreSQL"],
                "education": [
                    {
                        "degree": "Bachelor of Computer Science",
                        "institution": "HCMUT",
                        "start_date": "2015-09-01",
                        "end_date": "2019-06-30"
                    }
                ],
                "certifications": [
                    {
                        "name": "AWS Certified Developer",
                        "issuer": "Amazon",
                        "date": "2021-11-01"
                    }
                ],
                "isSuccessful": True,
                "httpResponseCode": 200
            }
        }
