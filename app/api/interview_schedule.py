from fastapi import APIRouter, HTTPException
from app.models.interview_schedule import InterviewScheduleRequest, InterviewScheduleResponse
from app.services.interview_schedule import InterviewScheduleService

router = APIRouter()

@router.post("/interview_schedule", response_model=InterviewScheduleResponse)
async def interview_schedule(request: InterviewScheduleRequest):
    try:
        service = InterviewScheduleService()
        result = await service.interview_schedule(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
Example input:
{
"candidateId": "CAND987654",
"panel": [
"interviewer2@example.com",
"interviewer4@example.com"
],
"preferredSlots": [
"2025-06-12T15:00:00+07:00",
"2025-06-13T10:00:00+07:00",
"2025-06-13T16:00:00+07:00"
]
}
"""