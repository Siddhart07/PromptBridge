from backend.phrase_shaper import shape_phrases
from backend.grammar_polisher import polish_phrase
from backend.relationship_mapper import map_keyword_relationships, build_topic_with_bridges
import streamlit as st

def map_template(routing_info: dict, keywords: list[str]) -> str:
    st.write("🚥 ROUTING INFO DEBUG:")
    st.write(routing_info)

    intent = routing_info["intent"]
    sub_intent = routing_info["sub_intent"]
    learning_mode = routing_info["learning_mode"]

    if keywords:
        relationships = map_keyword_relationships(keywords)
        raw_topic = build_topic_with_bridges(relationships)
    else:
        raw_topic = "the topic"

    shaped_topic = shape_phrases([raw_topic]) if isinstance(raw_topic, str) else shape_phrases(raw_topic)
    polished_topic = polish_phrase(shaped_topic)
    topic = polished_topic

    normalized_sub_intent = sub_intent.lower().replace('_', ' ').strip()

    if intent == "Coding & Development":
        if any(key in normalized_sub_intent for key in ["execution task", "execution", "code implementation", "task"]):
            return (f"Write a well-commented code snippet that addresses {topic}. "
                    f"Focus on functionality, code clarity, and best practices.")
        elif learning_mode:
            return (f"Create a beginner-friendly guide that teaches users how to perform {topic}. "
                    f"Include simple code examples, break down each step clearly, and explain key concepts "
                    f"to ensure understanding for beginners.")
        else:
            return (f"Write a well-commented code snippet that addresses {topic}. "
                    f"Focus on functionality, code clarity, and best practices.")

    elif intent == "Data Analysis":
        if learning_mode:
            return (f"Outline the steps to perform a data analysis task involving {topic}. "
                    f"Highlight important techniques, metrics, and potential pitfalls beginners should watch for.")
        else:
            return (f"Perform a detailed analysis of {topic}, highlighting key trends, patterns, and actionable insights.")

    elif intent == "Research":
        return (f"Provide a comprehensive research summary or investigative framework for {topic}. "
                f"Include key questions, objectives, and a structured methodology.")

    elif intent == "Creative Ideation":
        return (f"Generate creative and clearly defined ideas or strategies related to {topic} that can drive engagement and visibility.")

    # Final Safety Fallback: Force Execution Mode for Coding intent if everything else misses
    if intent == "Coding & Development" and not learning_mode:
        return (f"Write a well-commented code snippet that addresses {topic}. "
                f"Focus on functionality, code clarity, and best practices.")

    return (f"Generate an informative and helpful prompt related to {topic}.")
