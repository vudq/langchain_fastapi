from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class JDGenerateStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class JDGenerateRequest(BaseModel):
    jobTitle: str = Field(..., description="Tên vị trí công việc", min_length=1)
    tone: str = Field(..., description="Phong cách viết nội dung")
    comments: str = Field(..., description="Ghi chú mô tả thêm")

    temperature: Optional[float] = Field(0.7, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(1000, ge=1, le=4000)


class JDGenerateResponse(BaseModel):
    jobDescription: Optional[str]
    jobRequirements: Optional[str]
    jobResponsibilities: Optional[str]
    isSuccessfull: bool
    httpResponseCode: int
