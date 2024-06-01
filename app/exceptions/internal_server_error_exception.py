import traceback
from typing import Any, Callable

from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


async def exceptions_middleware(request: Request, call_next: Callable):
    try:
        return await call_next(request)
    except Exception as e:
        exc = await get_http_exception(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
        is_detail_dict = isinstance(exc.detail, dict)
        traceback_str = traceback.format_exc()
        print("ERROR:", e, "\n\n\n--------------------\n\n\nTRACEBACK", traceback_str)
        return JSONResponse(
            {
                "error": {
                    "message": (
                        exc.detail.get("message") if is_detail_dict else exc.detail
                    ),
                    "code": exc.status_code,
                    "traceback": traceback_str,
                    "details": (
                        exc.detail.get("extra_details") if is_detail_dict else None
                    ),
                }
            },
            status_code=exc.status_code,
            headers=exc.headers,
        )


async def get_http_exception(
    message: str, status_code: int, extra_details: dict[str, Any] = None
) -> HTTPException:
    detail = {
        "message": message,
        "extra_details": extra_details,
    }
    return HTTPException(status_code=status_code, detail=detail)
