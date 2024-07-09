from pydantic import BaseModel


class HTTPValidationError(BaseModel):
    """HTTP validation error"""

    success: bool = False
    description: str = "The format of the JSON sent is incorrect"


class DefaultResponse(BaseModel):
    """Default response"""

    success: bool = True
    data: dict = {}


class HTTPInternalServerError(BaseModel):
    """HTTP Internal Server Error"""

    success: bool = False
    error: str = "Internal Server Error"


# response_model to swagger
response_model = {
    422: {"model": HTTPValidationError},
    500: {"model": HTTPInternalServerError},
}
