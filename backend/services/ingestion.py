import requests
from fastapi import HTTPException

def fetch_doc(url: str):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(
            url=url,
            headers=headers,
            timeout=10
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error when downloading URL: {e}"
        )
    return response.text