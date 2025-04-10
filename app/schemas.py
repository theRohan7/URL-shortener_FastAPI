from pydantic import BaseModel,  HttpUrl

class URLRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    short_url: str
    created_at: str