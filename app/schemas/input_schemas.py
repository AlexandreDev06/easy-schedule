from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


@dataclass
class DefaultPagination:
    page: int = 1
    per_page: int = 20
    search: Optional[str] = None
    fields_to_search: Optional[str] = "email,name"
    order_by: Optional[str] = "id"
    order_type: Optional[str] = "asc"
