from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
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
async def analyze_feedback(request: Request):
    data = await request.json()
    text = data.get("review")  # ← burada düzeltildi

    print("Gelen veri:", data)
    print("Text:", text)

    if not text:
        return {"error": "No 'review' field provided."}

    summary = summarize_review(text)
    sentiment = analyze_sentiment(text)

    print("Summary:", summary)
    print("Sentiment:", sentiment)

    return {
        "summary": summary,
        "sentiment": sentiment
    }
