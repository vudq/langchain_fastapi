from fastapi import APIRouter, HTTPException
from app.models.cv_scoring import CVScoringRequest, CVScoringResponse
from app.services.cv_scoring import CVScoringService

router = APIRouter()

@router.post("/cv_scoring", response_model=CVScoringResponse)
async def cv_scoring(request: CVScoringRequest):
    try:
        service = CVScoringService()
        result = await service.cv_scoring(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
Example input:
{
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
    "certifications": []

  },
    "jobDescription": "Phát triển và tinh chỉnh các mô hình ngôn ngữ: Sử dụng các công cụ và framework như TensorFlow, PyTorch, và Hugging Face Transformers để xây dựng các mô hình ngôn ngữ. Phân tích và xử lý dữ liệu ngôn ngữ: Sử dụng các kỹ thuật NLP để phân tích, trích xuất thông tin từ văn bản, và xử lý ngôn ngữ tự nhiên. Thiết kế hệ thống truy xuất thông tin: Phát triển các hệ thống truy xuất thông tin từ cơ sở dữ liệu để hỗ trợ quá trình tạo ra câu trả lời chính xác và đầy đủ. Kết hợp truy xuất và sinh văn bản: Sử dụng các kỹ thuật RAG để kết hợp thông tin truy xuất từ các nguồn dữ liệu với khả năng sinh văn bản của mô hình. Nghiên cứu các kỹ thuật mới: Theo dõi và nghiên cứu các xu hướng và công nghệ mới trong lĩnh vực NLP, Chatbot và RAG. Tối ưu hóa hiệu suất hệ thống: Tối ưu hóa thời gian phản hồi và hiệu suất của hệ thống truy xuất thông tin."

}
"""