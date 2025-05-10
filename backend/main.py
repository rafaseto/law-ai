from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from services.ingestion import fetch_doc

app = FastAPI(debug=True, title="LawAI")


class IngestRequest(BaseModel):
    url: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ingest")
def ingest_doc(req: IngestRequest):
    return fetch_doc(req.url)