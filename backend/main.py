from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(debug=True, title="LawAI")


class IngestRequest(BaseModel):
    url: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ingest")
def ingest_doc(req: IngestRequest):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(
            req.url,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error when downloading URL: {e}"
        )

    return {"doc": response.text}