# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ResponseCreateParams",
    "Input",
    "InputUnionMember0",
    "InputUnionMember0Content",
    "InputUnionMember0ContentUnionMember0",
    "InputUnionMember0ContentUnionMember1",
    "InputUnionMember1",
    "InputUnionMember1Content",
    "InputUnionMember1ContentUnionMember0",
    "InputUnionMember1ContentUnionMember0Annotation",
    "InputUnionMember1ContentUnionMember1",
    "InputUnionMember2",
    "InputUnionMember2Summary",
]


class ResponseCreateParams(TypedDict, total=False):
    input: Required[Iterable[Input]]

    include: List[Literal["reasoning.encrypted_content"]]

    model: Literal["witan-alfred", "witan-alfred-mini", "witan-edward", "witan-edward-mini"]

    stream: bool


class InputUnionMember0ContentUnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["input_text"]]


class InputUnionMember0ContentUnionMember1(TypedDict, total=False):
    filename: Required[str]

    type: Required[Literal["input_file"]]

    file_data: str

    file_id: str


InputUnionMember0Content: TypeAlias = Union[InputUnionMember0ContentUnionMember0, InputUnionMember0ContentUnionMember1]


class InputUnionMember0(TypedDict, total=False):
    content: Required[Iterable[InputUnionMember0Content]]

    role: Required[Literal["user", "system", "developer"]]

    type: Literal["message"]


class InputUnionMember1ContentUnionMember0Annotation(TypedDict, total=False):
    type: Required[str]


class InputUnionMember1ContentUnionMember0(TypedDict, total=False):
    annotations: Required[Iterable[InputUnionMember1ContentUnionMember0Annotation]]

    text: Required[str]

    type: Required[Literal["output_text"]]


class InputUnionMember1ContentUnionMember1(TypedDict, total=False):
    refusal: Required[str]

    type: Required[Literal["refusal"]]


InputUnionMember1Content: TypeAlias = Union[InputUnionMember1ContentUnionMember0, InputUnionMember1ContentUnionMember1]


class InputUnionMember1(TypedDict, total=False):
    id: Required[str]

    content: Required[Iterable[InputUnionMember1Content]]

    role: Required[Literal["assistant"]]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["message"]]


class InputUnionMember2Summary(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["summary_text"]]


class InputUnionMember2(TypedDict, total=False):
    id: Required[str]

    summary: Required[Iterable[InputUnionMember2Summary]]

    type: Required[Literal["reasoning"]]

    encrypted_content: str

    status: Literal["in_progress", "completed", "incomplete"]


Input: TypeAlias = Union[InputUnionMember0, InputUnionMember1, InputUnionMember2]
