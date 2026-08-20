from fastapi import FastAPI
from .models import BuildContextRequest, ContextPackage
from .service import build_context_package

app = FastAPI(
    title="ContextBridge AI",
    version="0.1.0",
    description="Provider-neutral conversation context portability API",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/context/build", response_model=ContextPackage)
def build_context(request: BuildContextRequest) -> ContextPackage:
    return build_context_package(request)
