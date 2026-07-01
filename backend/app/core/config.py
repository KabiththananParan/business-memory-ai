from pydantic import BaseModel

class ApplicationConfig(BaseModel):
    app_name: str
    app_version: str
    debug: bool
    
class LLMConfig(BaseModel):
    provider: str
    model: str
    api_key: str
