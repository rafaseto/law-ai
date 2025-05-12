import requests
from fastapi import HTTPException
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def fetch_doc(url: str) -> str:
    """
    Download the content of a web page as text.

    Args:
        url (str): The URL of the document to fetch.

    Returns:
        str: The raw text content of the HTTP response.

    Raises:
        HTTPException: If the request fails
                       with status code 400 and a detail 
                       message describing the error.
    """
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


def extract_text(html: str) -> str:
    """
    Extract text from HTML content.

    Args:
        html (str): HTML content as a string. 

    Returns:
        str: A stripped string containing the text from the HTML.
    """
    try:
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        return text.strip()
    except Exception as e:
        logger.exception(
            f"Failed to extract text from the HTML: {e}"
        )
        return ""