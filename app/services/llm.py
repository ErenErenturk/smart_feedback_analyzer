from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=api_key)

def summarize_review(review):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes user reviews."},
            {"role": "user", "content": f"Summarize this review in one sentence: {review}"}
        ]
    )
    return response.choices[0].message.content.strip()
