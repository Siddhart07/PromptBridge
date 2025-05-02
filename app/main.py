import sys
import os

# Add parent directory to Python Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.prompt_router import route_prompt
from backend.template_mapper import map_template
from backend.nlp_cleaner import clean_text_by_intent
from backend.keyword_extractor import extract_keywords, clean_keywords
from backend.logger_feedback import log_feedback_to_mysql
from app.ui_components import (
    render_user_input_area,
    render_generate_button,
    render_prompt_display_area,
    render_feedback_form
)

st.set_page_config(page_title="PromptBridge", layout="wide")
st.title("✨ PromptBridge - Smart Prompt Generator")

st.cache_data.clear()  # Optional: clear Streamlit cache if needed

# User Input Section
user_input = render_user_input_area()

# Generate Button
generate_button_clicked = render_generate_button()

# When Generate Prompt is Clicked
if generate_button_clicked and user_input.strip():
    with st.spinner("Processing..."):
        routing_info = route_prompt(user_input)
        cleaned_input = clean_text_by_intent(user_input, routing_info["intent"])
        keywords = extract_keywords(cleaned_input)
        keywords = clean_keywords(keywords)
        generated_prompt = map_template(routing_info, keywords)

        # Save in Session
        st.session_state["prompt_ready"] = True
        st.session_state["routing_info"] = routing_info
        st.session_state["generated_prompt"] = generated_prompt
        st.session_state["original_input"] = user_input

# Display Prompt if Ready
if st.session_state.get("prompt_ready", False):
    render_prompt_display_area(st.session_state["generated_prompt"])

    # Feedback Form
    submit_feedback, relevance_score, clarity_score, accuracy_score, edit_effort_score, satisfaction_score, seconds_spent, additional_comments = render_feedback_form()

    if submit_feedback:
        # Save Feedback into MySQL
        log_feedback_to_mysql(
            user_input=st.session_state["original_input"],
            generated_prompt=st.session_state["generated_prompt"],
            routing_info=st.session_state["routing_info"],
            relevance_score=relevance_score,
            clarity_score=clarity_score,
            accuracy_score=accuracy_score,
            edit_effort_score=edit_effort_score,
            satisfaction_score=satisfaction_score,
            seconds_spent=seconds_spent,
            additional_comments=additional_comments
        )
        st.success("✅ Feedback submitted successfully!")


# Run the Streamlit app with the command: streamlit run app/main.py
# Open the browser at: http://localhost:8501