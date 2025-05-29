from app.core.llm_config import get_llm_model
from app.utils.json_helpers import clean_and_parse_json
from app.models.auto_offerletter import *
from langchain_core.prompts import ChatPromptTemplate
import json

# Mock candidate and job data
CANDIDATE_DB = {
    "abc123": {"name": "Nguyen Van A", "email": "vana@gmail.com"}
}

JOB_DB = {
    "job001": "Senior Backend Developer"
}


class AutoOfferLetterService:
    def __init__(self):
        with open("app/templates/auto_offerletter.txt", "r", encoding="utf-8") as f:
            prompt_template = f.read()
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.model = get_llm_model()
        self.chain = self.prompt | self.model

    async def auto_offerletter(self, request: AutoOfferLetterRequest) -> AutoOfferLetterResponse:
        try:
            candidate = CANDIDATE_DB.get(request.candidateId)
            job_title = JOB_DB.get(request.jobId)

            if not candidate or not job_title:
                raise ValueError("Invalid candidateId or jobId")

            inputs = {
                "candidate": json.dumps(candidate, ensure_ascii=False),
                "job_title": job_title,
                "salary": f"{request.salary:,.0f} VND",
                "start_date": request.startDate,
                "benefits": ", ".join(request.benefits)
            }

            response = await self.chain.ainvoke(inputs)
            content = response.content if hasattr(response, "content") else str(response)

            return AutoOfferLetterResponse(
                status="success",
                offerLetter=content,
                isSuccessful=True,
                httpResponseCode=200
            )
        except Exception as e:
            return AutoOfferLetterResponse(
                status="error",
                error_message=str(e),
                isSuccessful=False,
                httpResponseCode=500
            )
