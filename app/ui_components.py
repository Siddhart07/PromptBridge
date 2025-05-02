import streamlit as st
import json

# Load UI Texts from JSON Config
with open("config/ui_texts.json", "r", encoding="utf-8") as f:
    UI_TEXTS = json.load(f)


def render_user_input_area():
    user_input = st.text_area(
        label=UI_TEXTS.get("input_label", "Describe your task or idea:"),
        placeholder=UI_TEXTS.get("input_placeholder", "e.g., Refactor a volatility forecasting engine using LSTM"),
        height=200
    )
    return user_input


def render_generate_button():
    return st.button(UI_TEXTS.get("generate_button", "🚀 Generate Prompt"))


def render_prompt_display_area(generated_prompt: str):
    st.subheader(UI_TEXTS.get("generated_prompt_label", "📝 Generated Prompt"))
    st.text_area(label="", value=generated_prompt, height=200)


def render_feedback_form():
    st.subheader(UI_TEXTS.get("feedback_label", "📊 Feedback"))

    relevance_score = st.slider(UI_TEXTS.get("relevance_label", "How relevant was the prompt?"), 1, 5, 3)
    clarity_score = st.slider(UI_TEXTS.get("clarity_label", "How clear was the language?"), 1, 5, 3)
    accuracy_score = st.slider(UI_TEXTS.get("accuracy_label", "How accurately did the prompt capture your intent?"), 1, 5, 3)
    edit_effort_score = st.slider(UI_TEXTS.get("edit_effort_label", "How much editing did you need?"), 1, 5, 3)
    satisfaction_score = st.slider(UI_TEXTS.get("satisfaction_label", "How satisfied are you?"), 1, 5, 3)
    seconds_spent = st.number_input(UI_TEXTS.get("seconds_spent_label", "Approx. seconds spent editing"), min_value=0, max_value=600, value=0)
    additional_comments = st.text_area(UI_TEXTS.get("additional_comments_label", "Any additional comments?"), height=100)

    submit_feedback = st.button(UI_TEXTS.get("submit_feedback_button", "Submit Feedback"))

    return submit_feedback, relevance_score, clarity_score, accuracy_score, edit_effort_score, satisfaction_score, seconds_spent, additional_comments
