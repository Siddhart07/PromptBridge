def map_keyword_relationships(keywords: list[str]) -> dict:
    """
    Categorizes extracted keywords into action, primary object, and method/modifier buckets.
    Returns a structured dictionary for smooth sentence assembly.
    """
    if not keywords:
        return {"action": "", "object": "", "method": ""}

    action_keywords = {"refactor", "adjust", "optimize", "modify", "calibrate", "improve", "enhance", "update", "implement"}
    method_indicators = {"using", "based on", "through", "via", "leveraging"}

    action = ""
    primary_objects = []
    methods = []

    for kw in keywords:
        kw_lower = kw.lower()
        if any(action_word in kw_lower for action_word in action_keywords):
            action = kw.capitalize()
        elif any(mod_word in kw_lower for mod_word in method_indicators):
            methods.append(kw)
        else:
            primary_objects.append(kw)

    return {
        "action": action,
        "object": ", ".join(primary_objects) if primary_objects else "",
        "method": ", ".join(methods) if methods else ""
    }


def build_topic_with_bridges(relationships: dict) -> str:
    """
    Constructs a natural flowing topic phrase using dynamic bridge words.
    """
    action = relationships.get("action", "").strip()
    obj = relationships.get("object", "").strip()
    method = relationships.get("method", "").strip()

    topic_parts = []

    if action and obj:
        topic_parts.append(f"{action} the {obj}")
    elif action:
        topic_parts.append(f"{action}")

    if method:
        topic_parts.append(f"based on {method}")

    return " ".join(topic_parts)
