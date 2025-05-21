from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Özetleme için mT5-base Türkçe modeli
summary_model_name = "mukayese/mt5-base-turkish-summarization"
summary_tokenizer = AutoTokenizer.from_pretrained(summary_model_name)
summary_model = AutoModelForSeq2SeqLM.from_pretrained(summary_model_name)

# Türkçe duygu analizi modeli (bu kaldı)
sentiment_analyzer = pipeline("sentiment-analysis", model="savasy/bert-base-turkish-sentiment-cased")
