import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text: str, top_n: int = 5) -> list:
    doc = nlp(text)
    keywords = []

    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip().lower()
        if phrase not in keywords and len(phrase) > 2:
            keywords.append(phrase)

    for ent in doc.ents:
        if ent.text.lower() not in keywords:
            keywords.append(ent.text.strip().lower())

    return keywords[:top_n]


def clean_keywords(keywords: list) -> list:
    """Filter out generic or irrelevant words like 'beginners', 'students', etc."""
    irrelevant_terms = {"beginner", "beginners", "student", "students", "guide", "tutorial", "introduction", "overview"}

    cleaned = []
    for word in keywords:
        if all(bad_word not in word.lower() for bad_word in irrelevant_terms):
            cleaned.append(word.strip().lower())

    return cleaned
