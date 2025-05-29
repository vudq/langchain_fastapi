from app.core.llm_config import get_llm_model
from app.utils.json_helpers import clean_and_parse_json
from app.models.cv_scoring import *
from langchain_core.prompts import ChatPromptTemplate
import json


class CVScoringService:
    def __init__(self):
        with open("app/templates/cv_scoring.txt", "r", encoding="utf-8") as f:
            prompt_template = f.read()
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.model = get_llm_model()
        self.chain = self.prompt | self.model

    async def cv_scoring(self, request: CVScoringRequest) -> CVScoringResponse:
        try:
            resume_str = json.dumps(request.parsedResume.dict(), ensure_ascii=False, indent=2)
            inputs = {
                "resume": resume_str,
                "job_description": request.jobDescription
            }

            response = await self.chain.ainvoke(inputs)
            content = response.content if hasattr(response, "content") else str(response)
            result = clean_and_parse_json(content)

            return CVScoringResponse(
                status="success",
                isSuccessful=True,
                httpResponseCode=200,
                **result
            )
        except Exception as e:
            return CVScoringResponse(
                status="error",
                error_message=str(e),
                isSuccessful=False,
                httpResponseCode=500
            )
