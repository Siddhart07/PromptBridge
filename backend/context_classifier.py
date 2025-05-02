from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

LABELS = [
    "Step-by-Step",
    "Getting Started",
    "How-To Guide",
    "Clarify Technology",
    "Idea Exploration",
    "Confused or Uncertain",
    "Problem-Solving"
]

def classify_context(text: str) -> dict:
    result = classifier(text, LABELS)

    top_label = result['labels'][0]
    top_score = result['scores'][0]

    learning_mode = top_label in ["Step-by-Step", "Getting Started", "How-To Guide", "Confused or Uncertain"]

    return {
        "sub_intent": top_label,
        "confidence": round(top_score, 3),
        "learning_mode": learning_mode
    }
