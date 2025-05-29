from fastapi import APIRouter

from app.api.jd_generate import router as jd_generate_router
from app.api.cv_parsing import router as cv_parsing_router
from app.api.cv_scoring import router as cv_scoring_router
from app.api.job_match import router as job_match_router
from app.api.interview_schedule import router as interview_schedule_router
from app.api.auto_offerletter import router as auto_offerletter_router
from app.api.cv_parse_and_score import router as cv_parse_and_score_router

router = APIRouter()

router.include_router(jd_generate_router, tags=["job-description"])
router.include_router(cv_parsing_router, tags=["cv-parsing"])
router.include_router(cv_scoring_router, tags=["cv-scoring"])
router.include_router(job_match_router, tags=["job-matching"])
router.include_router(interview_schedule_router, tags=["interview-scheduling"])
router.include_router(auto_offerletter_router, tags=["offer-letter"])
router.include_router(cv_parse_and_score_router, tags=["cv-parse-and-score"])