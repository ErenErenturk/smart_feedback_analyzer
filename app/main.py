from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.sentiment import analyze_sentiment
from app.services.llm import summarize_review

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production için spesifik domain ekleyin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
def analyze_feedback(request: FeedbackRequest):
    print(f"Gelen veri: {request.text}")
    summary = summarize_review(request.text)
    sentiment = analyze_sentiment(request.text)
    print(f"Özet: {summary}, Duygu: {sentiment}")
    return {"summary": summary, "sentiment": sentiment}

