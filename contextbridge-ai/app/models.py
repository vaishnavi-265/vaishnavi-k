from typing import Literal
from pydantic import BaseModel, Field

Role = Literal["system", "user", "assistant", "tool"]


class Message(BaseModel):
    role: Role
    content: str = Field(min_length=1)


class BuildContextRequest(BaseModel):
    source_provider: str = "unknown"
    target_provider: str = "unknown"
    max_chars: int = Field(default=4000, ge=500, le=20000)
    messages: list[Message] = Field(min_length=1)


class ContextPackage(BaseModel):
    format_version: str = "0.1"
    source_provider: str
    target_provider: str
    summary: str
    facts: list[str]
    decisions: list[str]
    requirements: list[str]
    open_tasks: list[str]
    selected_history: list[Message]
    original_message_count: int
    retained_message_count: int
