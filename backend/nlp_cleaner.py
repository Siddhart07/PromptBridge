import re

def clean_text_by_intent(text: str, intent: str) -> str:
    text = text.strip()

    if intent == "Coding & Development":
        # Only trim whitespace
        return re.sub(r"\s+", " ", text)

    elif intent == "Data Analysis":
        # Retain %,$,€,₹, time formats; remove unnecessary characters
        return re.sub(r"[^\w\s\$€₹%\.:\-]", "", text)

    elif intent == "Research":
        text = text.lower()
        return re.sub(r"[^\w\s\-]", "", text)

    elif intent == "Creative Ideation":
        cleaned = re.sub(r"[^\w\s]", "", text)
        cleaned = re.sub(r"\s+", " ", cleaned).capitalize()
        return cleaned

    else:
        return re.sub(r"[^\w\s]", "", text)