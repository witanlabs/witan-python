# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ResponseCreateResponse",
    "Error",
    "Output",
    "OutputUnionMember0",
    "OutputUnionMember0Content",
    "OutputUnionMember0ContentUnionMember0",
    "OutputUnionMember0ContentUnionMember0Annotation",
    "OutputUnionMember0ContentUnionMember1",
    "OutputUnionMember1",
    "OutputUnionMember1Summary",
    "Tool",
]


class Error(BaseModel):
    code: Literal["server_error"]

    message: str


class OutputUnionMember0ContentUnionMember0Annotation(BaseModel):
    type: str


class OutputUnionMember0ContentUnionMember0(BaseModel):
    annotations: List[OutputUnionMember0ContentUnionMember0Annotation]

    text: str

    type: Literal["output_text"]


class OutputUnionMember0ContentUnionMember1(BaseModel):
    refusal: str

    type: Literal["refusal"]


OutputUnionMember0Content: TypeAlias = Union[
    OutputUnionMember0ContentUnionMember0, OutputUnionMember0ContentUnionMember1
]


class OutputUnionMember0(BaseModel):
    id: str

    content: List[OutputUnionMember0Content]

    role: Literal["assistant"]

    status: Literal["in_progress", "completed", "incomplete"]

    type: Literal["message"]


class OutputUnionMember1Summary(BaseModel):
    text: str

    type: Literal["summary_text"]


class OutputUnionMember1(BaseModel):
    id: str

    summary: List[OutputUnionMember1Summary]

    type: Literal["reasoning"]

    encrypted_content: Optional[str] = None

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None


Output: TypeAlias = Union[OutputUnionMember0, OutputUnionMember1]


class Tool(BaseModel):
    type: str


class ResponseCreateResponse(BaseModel):
    id: str

    created_at: int

    error: Optional[Error] = None

    incomplete_details: None = None

    instructions: None = None

    metadata: None = None

    model: Literal["witan-alfred", "witan-alfred-mini", "witan-edward", "witan-edward-mini"]

    object: Literal["response"]

    output: List[Output]

    output_text: str

    parallel_tool_calls: bool

    status: Literal["completed", "in_progress", "failed"]

    temperature: None = None

    tool_choice: Literal["none"]

    tools: List[Tool]

    top_p: None = None
