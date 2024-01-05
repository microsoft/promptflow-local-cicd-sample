from promptflow import tool
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import summarizer


@tool
def test_summarize(text: str) -> str:
    return summarizer.summarize_text(text)