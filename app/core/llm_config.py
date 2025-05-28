"""
LLM Configuration module for centralizing model initialization.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings


class LLMConfig:
    """Singleton class for managing LLM model configuration."""
    
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMConfig, cls).__new__(cls)
        return cls._instance
    
    def get_model(self) -> ChatGoogleGenerativeAI:
        """Get the configured LLM model instance.
        
        Returns:
            ChatGoogleGenerativeAI: The configured model instance
        """
        if self._model is None:
            self._model = ChatGoogleGenerativeAI(
                model=settings.MODEL_NAME,
                temperature=settings.MODEL_TEMPERATURE,
                google_api_key=settings.GOOGLE_API_KEY
            )
        return self._model
    
    def reset_model(self):
        """Reset the model instance (useful for testing or reconfiguration)."""
        self._model = None


# Convenience function to get model instance
def get_llm_model() -> ChatGoogleGenerativeAI:
    """Get the configured LLM model instance.
    
    Returns:
        ChatGoogleGenerativeAI: The configured model instance
    """
    llm_config = LLMConfig()
    return llm_config.get_model() 