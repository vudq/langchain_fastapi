from app.core.llm_config import get_llm_model
from app.utils.json_helpers import clean_and_parse_json
from app.models.interview_schedule import *
from langchain_core.prompts import ChatPromptTemplate
import json

# Mock availability data
PANEL_AVAILABILITY = {
    "interviewer1@example.com": [
        "2025-06-10T10:00:00+07:00",
        "2025-06-11T15:00:00+07:00",
        "2025-06-12T09:00:00+07:00"
    ],
    "interviewer2@example.com": [
        "2025-06-11T14:00:00+07:00",
        "2025-06-12T10:00:00+07:00",
        "2025-06-13T16:00:00+07:00"
    ],
    "interviewer3@example.com": [
        "2025-06-10T11:00:00+07:00",
        "2025-06-11T13:00:00+07:00",
        "2025-06-14T09:30:00+07:00"
    ],
    "interviewer4@example.com": [
        "2025-06-12T15:00:00+07:00",
        "2025-06-13T10:00:00+07:00",
        "2025-06-14T14:00:00+07:00"
    ],
    "interviewer5@example.com": [
        "2025-06-10T14:00:00+07:00",
        "2025-06-11T09:00:00+07:00",
        "2025-06-13T11:30:00+07:00"
    ]
}



class InterviewScheduleService:
    def __init__(self):
        with open("app/templates/interview_schedule.txt", "r", encoding="utf-8") as f:
            prompt_template = f.read()
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.model = get_llm_model()
        self.chain = self.prompt | self.model

    async def interview_schedule(self, request: InterviewScheduleRequest) -> InterviewScheduleResponse:
        try:
            # Get panel availability
            panel_avail = {
                pid: PANEL_AVAILABILITY.get(pid, []) for pid in request.panel
            }

            inputs = {
                "preferred_slots": json.dumps(request.preferredSlots, ensure_ascii=False),
                "panel_availability": json.dumps(panel_avail, ensure_ascii=False, indent=2)
            }

            response = await self.chain.ainvoke(inputs)
            content = response.content if hasattr(response, "content") else str(response)
            result = clean_and_parse_json(content)

            return InterviewScheduleResponse(
                status="success",
                confirmedSlot=result.get("confirmedSlot"),
                suggestedSlots=result.get("suggestedSlots", []),
                isSuccessful=True,
                httpResponseCode=200
            )
        except Exception as e:
            return InterviewScheduleResponse(
                status="error",
                error_message=str(e),
                isSuccessful=False,
                httpResponseCode=500
            )
