import re

def detect_intent(text: str) -> str:
    text = text.lower()

    coding_keywords = ["python", "sql", "query", "api", "script", "code", "function", "llm"]
    data_keywords = ["data", "analyze", "visualize", "chart", "metric", "dashboard"]
    research_keywords = ["research", "study", "paper", "analysis", "report", "explain"]
    creative_keywords = ["idea", "campaign", "story", "creative", "brand", "headline"]

    def match_keywords(keywords):
        return any(word in text for word in keywords)

    if match_keywords(coding_keywords):
        return "Coding & Development"
    elif match_keywords(data_keywords):
        return "Data Analysis"
    elif match_keywords(research_keywords):
        return "Research"
    elif match_keywords(creative_keywords):
        return "Creative Ideation"
    else:
        return "General"