from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_review(review: str) -> str:
    try:
        summary = summarizer(review, max_length=60, min_length=15, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return "Summarization failed: " + str(e)

