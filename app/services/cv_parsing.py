from app.models.cv_parsing import *
from app.core.llm_config import get_llm_model
from app.utils.json_helpers import clean_and_parse_json
from langchain_core.prompts import ChatPromptTemplate
import fitz  # PyMuPDF


class CVParsingService:
    def __init__(self):
        with open("app/templates/cv_parsing.txt", "r", encoding="utf-8") as f:
            self.prompt = ChatPromptTemplate.from_template(f.read())
        self.model = get_llm_model()
        self.chain = self.prompt | self.model

    def clean_items(self, items: list[dict], required_fields: list[str]) -> list[dict]:
        return [
            item for item in items
            if all(item.get(f) not in [None, "", "null"] for f in required_fields)
        ]

    async def cv_parsing(self, file) -> CVParsingResponse:
        try:
            content = await file.read()
            doc = fitz.open(stream=content, filetype="pdf")
            cv_text = "\n".join(page.get_text() for page in doc)

            response = await self.chain.ainvoke({"cv_text": cv_text})
            output = response.content if hasattr(response, "content") else str(response)
            result = clean_and_parse_json(output)

            # Sanitize lists before returning
            result["experience"] = self.clean_items(result.get("experience", []), ["position", "company"])
            result["education"] = self.clean_items(result.get("education", []), ["degree", "institution"])
            result["certifications"] = self.clean_items(result.get("certifications", []), ["name", "issuer"])

            return CVParsingResponse(
                status="success",
                isSuccessful=True,
                httpResponseCode=200,
                **result
            )
        except Exception as e:
            return CVParsingResponse(
                status="error",
                error_message=str(e),
                isSuccessful=False,
                httpResponseCode=500
            )
