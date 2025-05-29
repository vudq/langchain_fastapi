from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from app.models.cv_parse_and_score import CVParseAndScoreResponse
from app.services.cv_parse_and_score import CVParseAndScoreService

router = APIRouter()

@router.post("/cv_parse_and_score", response_model=CVParseAndScoreResponse)
async def cv_parse_and_score(file: UploadFile = File(...), jobDescription: str = Form(...)):
    try:
        service = CVParseAndScoreService()
        result = await service.cv_parse_and_score(file, jobDescription)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
    Example input
    jobDescription: "Mô tả công việc Phát triển và tinh chỉnh các mô hình ngôn ngữ: Sử dụng các công cụ và framework như TensorFlow, PyTorch, và Hugging Face Transformers để xây dựng các mô hình ngôn ngữ. Phân tích và xử lý dữ liệu ngôn ngữ: Sử dụng các kỹ thuật NLP để phân tích, trích xuất thông tin từ văn bản, và xử lý ngôn ngữ tự nhiên. Thiết kế hệ thống truy xuất thông tin: Phát triển các hệ thống truy xuất thông tin từ cơ sở dữ liệu để hỗ trợ quá trình tạo ra câu trả lời chính xác và đầy đủ. Kết hợp truy xuất và sinh văn bản: Sử dụng các kỹ thuật RAG để kết hợp thông tin truy xuất từ các nguồn dữ liệu với khả năng sinh văn bản của mô hình. Nghiên cứu các kỹ thuật mới: Theo dõi và nghiên cứu các xu hướng và công nghệ mới trong lĩnh vực NLP, Chatbot và RAG. Tối ưu hóa hiệu suất hệ thống: Tối ưu hóa thời gian phản hồi và hiệu suất của hệ thống truy xuất thông tin.   Yêu cầu ứng viên Kinh nghiệm: Tối thiểu 10 tháng ở vị trí tương đương. Trình độ học vấn: Tốt nghiệp Cao đẳng/Đại học các chuyên ngành Công nghệ Thông tin, Toán Tin, Điện tử Viễn thông, Điều khiển Tự động, hoặc các ngành liên quan. Kiến thức chuyên môn: Có hiểu biết về Machine Learning và Deep Learning. Kinh nghiệm làm việc với các mô hình ngôn ngữ lớn (LLM) như BERT, T5, Mistral, LLaMa, GPT, v.v. Có kinh nghiệm làm việc với RESTAPI, Langchain, llamaindex, … Kỹ năng nghiên cứu và nền tảng: Khả năng nghiên cứu và áp dụng các công nghệ mới. Nền tảng vững chắc về cấu trúc dữ liệu và thuật toán. Kỹ năng lập trình: Hiểu biết và kinh nghiệm lập trình với các ngôn ngữ như C++ và Python. Kinh nghiệm cơ sở dữ liệu: Có kinh nghiệm làm việc với SQL."
"""