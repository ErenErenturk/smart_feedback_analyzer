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
async def analyze_feedback(request: Request):
    data = await request.json()
    review = data.get("review")

    if not review:
        raise HTTPException(status_code=400, detail="Missing 'review' field.")

    try:
        sentiment = analyze_sentiment(review)
        summary = summarize_review(review)
    except Exception as e:
        print(f"Error in analyze_feedback: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"sentiment": sentiment, "summary": summary}
