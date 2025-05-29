from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.cv_parsing import CVParsingResponse
from app.services.cv_parsing import CVParsingService

router = APIRouter()

@router.post("/cv_parsing", response_model=CVParsingResponse)
async def cv_parsing(file: UploadFile = File(...)):
    try:
        service = CVParsingService()
        result = await service.cv_parsing(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
    Example input
    file: CV file in PDF
"""