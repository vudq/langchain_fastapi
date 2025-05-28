from app.models.jd_generate import JDGenerateRequest, JDGenerateResponse
from app.utils.json_helpers import clean_and_parse_json
from app.core.llm_config import get_llm_model
from langchain.prompts import ChatPromptTemplate


class JDGenerateService:
    def __init__(self):
        with open("app/templates/jd_generate.txt", "r", encoding="utf-8") as f:
            prompt_template = f.read()
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.model = get_llm_model()
        self.chain = self.prompt | self.model

    async def jd_generate(self, request: JDGenerateRequest) -> JDGenerateResponse:
        try:
            input_data = {
                "jobTitle": request.jobTitle,
                "tone": request.tone,
                "comments": request.comments
            }
            response = await self.chain.ainvoke(input_data)
            content = response.content if hasattr(response, 'content') else str(response)
            result = clean_and_parse_json(content)

            return JDGenerateResponse(
                jobDescription=result.get("jobDescription"),
                jobRequirements=result.get("jobRequirements"),
                jobResponsibilities=result.get("jobResponsibilities"),
                isSuccessfull=True,
                httpResponseCode=200
            )
        except Exception as e:
            return JDGenerateResponse(
                jobDescription=None,
                jobRequirements=None,
                jobResponsibilities=None,
                isSuccessfull=False,
                httpResponseCode=500
            )
