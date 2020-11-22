from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi import Query, Form
from uuid import UUID, uuid4

class DataSchema(BaseModel):
    name: str = Field(...)
    source: str = Field(...)
    link: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name":"Inception",
                "source":"Netflix",
                "link":"www.netflix.com",
            }
        }

class updateDataSchema(BaseModel):
    name: Optional[str] 
    source: Optional[str]
    link: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name":"The Man in the High Castle",
                "source":"Amazon Prime Video",
                "link":"www.amazon.com",
            }
        }

def ResponseModel(data, message):
    return {
        "data":[data],
        "message":message,
        "code":200,
    }

def ErrorResponseModel(error, code, message):
    return {
        "error":error,
        "code":code,
        "message":message,
    }