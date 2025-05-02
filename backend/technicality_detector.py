import re

TECHNICAL_TERMS = {
    # --- Coding & Development (Software, AI, ML, LLM) ---
    "python", "java", "c++", "javascript", "node.js", "sql", "api integration", "rest api", "graphql",
    "docker", "microservices", "kubernetes", "cloud deployment", "devops",
    "machine learning", "deep learning", "computer vision", "nlp", "natural language processing",
    "reinforcement learning", "supervised learning", "unsupervised learning", "transfer learning",
    "time series prediction", "anomaly detection", "fine-tuning", "few-shot learning", "zero-shot learning",
    "gpt", "bert", "transformer model", "attention mechanism", "prompt engineering", "rnn", "lstm", "cnn",
    "self-attention", "multi-head attention", "pytorch", "tensorflow", "keras", "huggingface",
    "openai api", "langchain", "embedding models", "retrieval augmented generation",

    # --- Finance ---
    "option pricing", "black-scholes model", "volatility forecasting", "garch models",
    "markowitz portfolio optimization", "risk parity", "value at risk", "monte carlo simulation",
    "statistical arbitrage", "regime switching", "derivatives", "swaps", "bonds", "structured products",
    "etf strategies", "multi-asset portfolios", "hedging strategies", "algorithmic trading",
    "backtesting frameworks", "quantitative factor modeling", "alpha generation", "execution strategies",
    "stress testing", "credit scoring", "loan default prediction", "credit risk modeling", "liquidity risk",

    # --- Data Analysis ---
    "exploratory data analysis", "statistical hypothesis testing", "a/b testing", "data wrangling",
    "feature engineering", "principal component analysis", "correlation analysis", "classification",
    "regression", "pandas", "numpy", "matplotlib", "seaborn", "power bi", "tableau", "looker studio",
    "time series decomposition", "seasonal adjustment", "outlier detection", "data imbalance handling",
    "data imputation",

    # --- Research ---
    "literature review", "systematic review", "hypothesis generation", "theoretical modeling",
    "computational simulation", "experimental design", "generative ai", "blockchain applications",
    "quantum machine learning", "neuro-symbolic ai", "explainable ai", "causal inference",
    "agent-based modeling"
}


def detect_technicality(text: str) -> bool:
    """
    Returns True if the text is highly technical and should override learning mode to False.
    Uses safer word-boundary based matching for technical terms.
    """
    text_lower = text.lower()

    for term in TECHNICAL_TERMS:
        pattern = r'\b' + re.escape(term.lower()) + r'\b'
        if re.search(pattern, text_lower):
            return True

    return False
