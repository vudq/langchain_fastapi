from app.core.llm_config import get_llm_model
from app.utils.json_helpers import clean_and_parse_json
from app.models.job_match import *
from langchain_core.prompts import ChatPromptTemplate
import json

# Temporary hardcoded job list for matching (replace with DB/Elasticsearch in real app)
JOB_POOL = [
    {"jobId": "job001", "title": "Senior Backend Developer",    "description": "Work with Python, FastAPI, Docker, PostgreSQL."},
    {"jobId": "job002", "title": "Frontend Developer",          "description": "ReactJS, Tailwind, UX/UI skills."},
    {"jobId": "job003", "title": "DevOps Engineer",             "description": "Kubernetes, Terraform, AWS."},
    {"jobId": "job004", "title": "Data Scientist",              "description": "Python, Pandas, Scikit-Learn, TensorFlow, data visualization."},
    {"jobId": "job005", "title": "Machine Learning Engineer",    "description": "PyTorch, TensorFlow, model deployment with Docker & Kubernetes."},
    {"jobId": "job006", "title": "Cloud Architect",             "description": "AWS/GCP/Azure design, IaC (Terraform), networking, security."},
    {"jobId": "job007", "title": "Site Reliability Engineer",   "description": "Monitoring (Prometheus/Grafana), CI/CD pipelines, Linux."},
    {"jobId": "job008", "title": "QA Automation Engineer",       "description": "Selenium, Cypress, Python/Java, test frameworks."},
    {"jobId": "job009", "title": "Security Engineer",           "description": "Vulnerability assessment, SIEM, VPN, firewalls."},
    {"jobId": "job010", "title": "Network Engineer",            "description": "Cisco, Juniper, routing & switching, LAN/WAN design."}
]



class JobMatchService:
    def __init__(self):
        with open("app/templates/job_match.txt", "r", encoding="utf-8") as f:
            prompt_template = f.read()
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.model = get_llm_model()
        self.chain = self.prompt | self.model

    async def job_match(self, request: JobMatchRequest) -> JobMatchResponse:
        try:
            if not request.parsedResume:
                raise ValueError("Resume not provided. (parsedResume required if no candidateId)")

            resume_json = json.dumps(request.parsedResume.dict(), ensure_ascii=False, indent=2)
            job_list_json = json.dumps(JOB_POOL, ensure_ascii=False, indent=2)

            inputs = {
                "resume": resume_json,
                "job_list": job_list_json
            }

            response = await self.chain.ainvoke(inputs)
            content = response.content if hasattr(response, "content") else str(response)
            result = clean_and_parse_json(content)

            return JobMatchResponse(
                status="success",
                isSuccessful=True,
                httpResponseCode=200,
                matches=result
            )
        except Exception as e:
            return JobMatchResponse(
                status="error",
                error_message=str(e),
                isSuccessful=False,
                httpResponseCode=500
            )
