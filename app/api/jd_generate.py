from fastapi import APIRouter, HTTPException
from app.models.jd_generate import JDGenerateRequest, JDGenerateResponse
from app.services.jd_generate import JDGenerateService

router = APIRouter()

@router.post("/jd_generate", response_model=JDGenerateResponse)
async def jd_generate(request: JDGenerateRequest):
    try:
        service = JDGenerateService()
        result = await service.jd_generate(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
