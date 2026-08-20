from .models import BuildContextRequest, ContextPackage, Message

DECISION_MARKERS = ("decided", "decision", "we will", "we'll", "use ")
REQUIREMENT_MARKERS = ("must", "need to", "should", "require", "requirement")
TASK_MARKERS = ("todo", "to do", "next", "need to", "will implement", "will add")
FACT_MARKERS = ("is ", "are ", "remember", "using", "works with")


def _collect(messages: list[Message], markers: tuple[str, ...], limit: int = 8) -> list[str]:
    results: list[str] = []
    for message in messages:
        text = " ".join(message.content.split())
        lowered = text.lower()
        if any(marker in lowered for marker in markers) and text not in results:
            results.append(text[:500])
        if len(results) >= limit:
            break
    return results


def _select_history(messages: list[Message], max_chars: int) -> list[Message]:
    selected: list[Message] = []
    used = 0
    for message in reversed(messages):
        cost = len(message.content)
        if selected and used + cost > max_chars:
            break
        if cost > max_chars and not selected:
            selected.append(Message(role=message.role, content=message.content[-max_chars:]))
            break
        selected.append(message)
        used += cost
    return list(reversed(selected))


def _summary(messages: list[Message], max_chars: int = 900) -> str:
    snippets = []
    for message in messages[-8:]:
        label = message.role.capitalize()
        clean = " ".join(message.content.split())
        snippets.append(f"{label}: {clean}")
    text = " | ".join(snippets)
    return text[:max_chars]


def build_context_package(request: BuildContextRequest) -> ContextPackage:
    history_budget = max(300, int(request.max_chars * 0.55))
    history = _select_history(request.messages, history_budget)

    return ContextPackage(
        source_provider=request.source_provider,
        target_provider=request.target_provider,
        summary=_summary(request.messages),
        facts=_collect(request.messages, FACT_MARKERS),
        decisions=_collect(request.messages, DECISION_MARKERS),
        requirements=_collect(request.messages, REQUIREMENT_MARKERS),
        open_tasks=_collect(request.messages, TASK_MARKERS),
        selected_history=history,
        original_message_count=len(request.messages),
        retained_message_count=len(history),
    )
