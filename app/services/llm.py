from ai.processor import summary_tokenizer, summary_model
import torch

def summarize_review(text: str) -> str:
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        summary_model.to(device)

        prompt = "summarize: " + text  # ← kritik satır

        inputs = summary_tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True).to(device)
        summary_ids = summary_model.generate(
            inputs,
            max_length=100,
            min_length=20,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )

        return summary_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        return f"Özetleme hatası: {str(e)}"
