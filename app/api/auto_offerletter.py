from fastapi import APIRouter, HTTPException
from app.models.auto_offerletter import AutoOfferLetterRequest, AutoOfferLetterResponse
from app.services.auto_offerletter import AutoOfferLetterService

router = APIRouter()

@router.post("/auto_offerletter", response_model=AutoOfferLetterResponse)
async def auto_offerletter(request: AutoOfferLetterRequest):
    try:
        service = AutoOfferLetterService()
        result = await service.auto_offerletter(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
    Example input
{
  "candidateId": "abc123",
  "jobId": "job001",
  "salary": 35000000,
  "startDate": "2025-07-01",
  "benefits": [
    "Bảo hiểm y tế đầy đủ",
    "Làm việc hybrid",
    "Snack & cafe miễn phí tại văn phòng"
  ]
}
"""
