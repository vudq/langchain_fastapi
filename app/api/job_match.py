from fastapi import APIRouter, HTTPException
from app.models.job_match import JobMatchRequest, JobMatchResponse
from app.services.job_match import JobMatchService

router = APIRouter()

@router.post("/job_match", response_model=JobMatchResponse)
async def job_match(request: JobMatchRequest):
    try:
        service = JobMatchService()
        result = await service.job_match(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
Example input:
{
  "candidateId": "string",
  "parsedResume": {
     "name": "LE MINH CHAU",
    "email": "minhchaule4w@gmail.com",
    "phone": "+84 858 040 403",
    "experience": [
      {
        "position": "AI Engineer",
        "company": "Techvify",
        "start_date": "Jul 2024",
        "end_date": "Oct 2024"
      },
      {
        "position": "Data Scientist Fresher",
        "company": "Viettel Network",
        "start_date": "Nov 2024",
        "end_date": "Feb 2025"
      }
    ],
    "skills": [
      "RAG",
      "LLMs",
      "Prompt Engineering",
      "FastAPI",
      "Streamlit",
      "GraphRAG",
      "LightRAG",
      "Federated Learning",
      "Knowledge Distillation",
      "Statistics",
      "Reinforcement Learning",
      "Knowledge Graphs",
      "Explainable AI in Healthcare",
      "Generative AI",
      "Data Processing",
      "Fine-tuning",
      "Scrapy",
      "XPath",
      "Data Labeling",
      "English",
      "Python",
      "C++",
      "Java",
      "R",
      "PyTorch",
      "Scikit-learn",
      "Machine Learning",
      "Deep Learning"
    ],
    "education": [
      {
        "degree": "Bachelor of Science in Information Technology",
        "institution": "University of Engineering and Technology (VNU - UET)",
        "start_date": "Aug 2021",
        "end_date": "May 2025"
      }
    ],
    "certifications": []  }
}
"""