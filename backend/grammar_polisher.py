import re

def polish_phrase(phrase: str) -> str:
    """
    Lightly polishes a shaped phrase:
    - Cleans up awkward comma usage
    - Ensures proper "and" joining
    - Capitalizes recognized tool names properly
    """

    if not phrase:
        return phrase

    # Fix triple/multiple commas or spaces
    phrase = re.sub(r',\s*,+', ',', phrase)
    phrase = re.sub(r'\s+', ' ', phrase)

    # Fix trailing commas before "and"
    phrase = re.sub(r',\s*and', ' and', phrase)

    # Capitalize major tools if mentioned
    important_tools = ["python", "pandas", "numpy", "tensorflow", "keras", "scikit-learn", "sql", "power bi"]
    for tool in important_tools:
        pattern = re.compile(rf'\b{tool}\b', re.IGNORECASE)
        phrase = pattern.sub(tool.title(), phrase)

    # Minor stylistic fixes (optional)
    phrase = phrase.strip().capitalize()

    return phrase