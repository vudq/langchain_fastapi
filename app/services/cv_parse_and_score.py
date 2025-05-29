from app.models.cv_parse_and_score import *
from app.services.cv_parsing import CVParsingService
from app.services.cv_scoring import CVScoringService
from fastapi import UploadFile


class CVParseAndScoreService:
    def __init__(self):
        self.cv_parser = CVParsingService()
        self.cv_scorer = CVScoringService()

    async def cv_parse_and_score(self, file: UploadFile, jd: str) -> CVParseAndScoreResponse:
        try:
            # Step 1: Parse CV
            parse_result = await self.cv_parser.cv_parsing(file)
            if parse_result.status != "success":
                raise ValueError(f"Parsing failed: {parse_result.error_message}")

            # Step 2: Score CV
            from app.models.cv_scoring import CVScoringRequest, ParsedResume
            
            parsed_resume_data = {
                "name": parse_result.name,
                "email": parse_result.email,
                "phone": parse_result.phone,
                "experience": [e.dict() for e in parse_result.experience or []],
                "skills": parse_result.skills,
                "education": [e.dict() for e in parse_result.education or []],
                "certifications": [c.dict() for c in parse_result.certifications or []],
            }

            score_request = CVScoringRequest(
                parsedResume=ParsedResume(**parsed_resume_data),
                jobDescription=jd
            )
            score_result = await self.cv_scorer.cv_scoring(score_request)

            return CVParseAndScoreResponse(
                status="success",
                parsedResume=parse_result.dict(exclude={"status", "isSuccessful", "httpResponseCode", "error_message"}),
                score=score_result.score,
                keyMatch=score_result.keyMatch,
                missingSkills=score_result.missingSkills,
                isSuccessful=True,
                httpResponseCode=200
            )
        except Exception as e:
            return CVParseAndScoreResponse(
                status="error",
                error_message=str(e),
                isSuccessful=False,
                httpResponseCode=500
            )
