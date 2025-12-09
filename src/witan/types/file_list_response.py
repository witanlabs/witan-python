# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileListResponse", "Data"]


class Data(BaseModel):
    id: str

    bytes: float

    created_at: float

    filename: str

    object: Literal["file"]


class FileListResponse(BaseModel):
    data: List[Data]

    has_more: bool

    object: Literal["list"]

    first_id: Optional[str] = None

    last_id: Optional[str] = None
