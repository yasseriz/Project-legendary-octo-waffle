from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi import Query

class DataSchema(BaseModel):
    name: str = Field(...)
    source: List[str] = Field(...)
    link = str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name":"Inception",
                "source":"Netflix",
                "link":"www.netflix.com"
            }
        }

class updateDataSchema(BaseModel):
    name: Optional[str] 
    source: Optional[str]
    link = Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name":"Inception",
                "source":"Amazon Prime Video",
                "link":"www.amazon.com"
            }
        }

class ResponseModel(data, message):
    return {
        "data":[data],
        "message":message,
        "code":200
    }

class ErrorResponseModel(error, code, message):
    return {
        "error":error,
        "code":code,
        "message":message
    }