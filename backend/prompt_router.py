from backend.intent_detector import detect_intent
from backend.context_classifier import classify_context
from backend.technicality_detector import detect_technicality

def route_prompt(user_input: str) -> dict:
    technical_override = detect_technicality(user_input)

    if technical_override:
        # Fully force new context if technicality is detected
        intent = "Coding & Development"
        context = {
            "sub_intent": "Execution Task",
            "confidence": 1.0,
        }
        learning_mode_final = False
    else:
        # Normal flow if not technical
        intent = detect_intent(user_input)
        context = classify_context(user_input)
        learning_mode_final = context["learning_mode"]

    routing_info = {
        "intent": intent,
        "sub_intent": context["sub_intent"],
        "learning_mode": learning_mode_final,
        "confidence": context.get("confidence", 1.0),
        "template_id": f"{intent.lower().replace(' ', '_')}_{context['sub_intent'].lower().replace(' ', '_')}"
    }

    return routing_info
