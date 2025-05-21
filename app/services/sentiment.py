from ai.processor import sentiment_analyzer

def analyze_sentiment(text: str) -> str:
    try:
        result = sentiment_analyzer(text)
        return result[0]["label"]  # örn. LABEL_0 → negatif
    except Exception as e:
        return f"Duygu analizi başarısız: {str(e)}"
