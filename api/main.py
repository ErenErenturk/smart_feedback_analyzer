from fastapi import FastAPI, Request
from app.services.sentiment import analyze_sentiment
from app.services.llm import summarize_review

app = FastAPI()

@app.post("/analyze/")
async def analyze_feedback(request: Request):
    data = await request.json()
    review = data.get("review")
    sentiment = analyze_sentiment(review)
    summary = summarize_review(review)
    return {"sentiment": sentiment, "summary": summary}
