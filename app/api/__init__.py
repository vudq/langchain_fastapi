from fastapi import APIRouter

from app.api.jd_generate import router as jd_generate_router


router = APIRouter()
# Include all routers without prefixes since they now have specific endpoints
router.include_router(jd_generate_router, tags=["job-description"])

