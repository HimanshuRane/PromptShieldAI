import streamlit as st
from gemma import analyze_prompt

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="PromptShieldAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# Apple-inspired UI
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* ---------- Global ---------- */
    .stApp {
        background:
            radial-gradient(circle at 50% -10%, rgba(0,122,255,.13), transparent 32%),
            #f5f5f7;
        color: #1d1d1f;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* ---------- Hero ---------- */
    .hero {
        text-align: center;
        padding: 18px 20px 34px;
    }

    .shield {
        width: 68px;
        height: 68px;
        margin: 0 auto 18px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 34px;
        background: linear-gradient(145deg, #007aff, #5ac8fa);
        box-shadow: 0 16px 38px rgba(0,122,255,.22);
    }

    .hero h1 {
        margin: 0;
        color: #1d1d1f;
        font-size: 48px;
        line-height: 1.05;
        font-weight: 750;
        letter-spacing: -2.4px;
    }

    .hero p {
        margin: 12px auto 0;
        max-width: 700px;
        color: #6e6e73;
        font-size: 18px;
        line-height: 1.5;
    }

    /* ---------- Streamlit bordered containers ---------- */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,.78);
        border: 1px solid rgba(0,0,0,.07);
        border-radius: 22px;
        box-shadow: 0 10px 34px rgba(0,0,0,.055);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        padding: 4px 2px;
    }

    /* ---------- Text ---------- */
    .section-title {
        color: #1d1d1f;
        font-size: 21px;
        font-weight: 700;
        letter-spacing: -.45px;
        margin-bottom: 3px;
    }

    .section-subtitle {
        color: #6e6e73;
        font-size: 14px;
        margin-bottom: 12px;
    }

    /* ---------- Text area ---------- */
    textarea {
        border-radius: 15px !important;
        border: 1px solid #d2d2d7 !important;
        background: #fbfbfd !important;
        color: #1d1d1f !important;
        font-size: 15px !important;
        line-height: 1.55 !important;
        padding: 15px !important;
        box-shadow: inset 0 1px 2px rgba(0,0,0,.03);
    }

    textarea:focus {
        border-color: #007aff !important;
        box-shadow: 0 0 0 3px rgba(0,122,255,.12) !important;
    }

    /* ---------- Buttons ---------- */
    .stButton > button {
        width: 100%;
        min-height: 50px;
        border: 0;
        border-radius: 14px;
        background: #007aff;
        color: white;
        font-size: 16px;
        font-weight: 650;
        box-shadow: 0 8px 20px rgba(0,122,255,.20);
        transition: .18s ease;
    }

    .stButton > button:hover {
        background: #006fe6;
        transform: translateY(-1px);
        box-shadow: 0 11px 25px rgba(0,122,255,.24);
    }

    /* ---------- Metrics ---------- */
    [data-testid="stMetric"] {
        background: rgba(255,255,255,.82);
        border: 1px solid rgba(0,0,0,.065);
        border-radius: 18px;
        padding: 17px 19px;
        box-shadow: 0 8px 25px rgba(0,0,0,.04);
    }

    [data-testid="stMetricLabel"] {
        color: #6e6e73;
        font-size: 14px;
    }

    [data-testid="stMetricValue"] {
        color: #1d1d1f;
        font-weight: 600;
    }

    /* ---------- Status ---------- */
    .status {
        border-radius: 18px;
        padding: 20px 22px;
        margin: 18px 0 16px;
        border: 1px solid;
    }

    .status-safe {
        background: #ecfdf3;
        border-color: #b7ebc6;
        color: #146c2e;
    }

    .status-warning {
        background: #fff8e6;
        border-color: #f1d28a;
        color: #805600;
    }

    .status-danger {
        background: #fff0f0;
        border-color: #efb5b5;
        color: #a61b1b;
    }

    .status-title {
        font-size: 23px;
        font-weight: 750;
        letter-spacing: -.4px;
    }

    .status-text {
        margin-top: 4px;
        font-size: 14px;
    }

    /* ---------- Threat pills ---------- */
    .pill {
        display: inline-block;
        margin: 3px 5px 3px 0;
        padding: 7px 11px;
        border-radius: 999px;
        background: #f2f2f7;
        border: 1px solid #dedee3;
        color: #3a3a3c;
        font-size: 13px;
        font-weight: 600;
    }

    /* ---------- Code block ---------- */
    [data-testid="stCode"] {
        border-radius: 14px;
    }

    /* ---------- Footer ---------- */
    .footer {
        text-align: center;
        color: #86868b;
        font-size: 13px;
        padding: 28px 0 5px;
    }

    @media (max-width: 700px) {
        .block-container {
            padding-top: 1.2rem;
        }

        .hero h1 {
            font-size: 37px;
            letter-spacing: -1.7px;
        }

        .hero p {
            font-size: 16px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Hero
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="shield">🛡️</div>
        <h1>PromptShieldAI</h1>
        <p>
            A privacy-first security layer that checks your prompts
            before they reach an AI model.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Prompt input
# ---------------------------------------------------------
with st.container(border=True):
    st.markdown(
        '<div class="section-title">Analyze a prompt</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-subtitle">'
        'Detect prompt attacks, exposed credentials, PII, and other privacy risks.'
        '</div>',
        unsafe_allow_html=True,
    )

    prompt = st.text_area(
        "Prompt",
        height=220,
        placeholder="Paste the prompt or code you are about to send to an AI model...",
        label_visibility="collapsed",
    )

    analyze = st.button("🛡️  Shield My Prompt", use_container_width=True)

# ---------------------------------------------------------
# Analysis
# ---------------------------------------------------------
if analyze:
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
        st.stop()

    with st.spinner("Gemma is checking your prompt..."):
        result = analyze_prompt(prompt.strip())

    risk = str(result.get("risk_level", "Unknown"))
    privacy_score = result.get("privacy_score", 0)
    safe = result.get("safe_to_share", "Unknown")

    detected = result.get("detected_items", [])
    risks = result.get("privacy_risks", [])
    recommendations = result.get("recommendations", [])
    sanitized = result.get("sanitized_prompt", prompt)

    # Gemma currently returns a privacy/safety score where 100 is safer.
    # Display the inverse as an intuitive risk score.
    try:
        privacy_score_num = float(privacy_score)
        risk_score = round(max(0, min(100, 100 - privacy_score_num)))
    except (TypeError, ValueError):
        risk_score = 0

    risk_lower = risk.lower()

    if risk_lower in ("critical", "high"):
        decision = "BLOCK — DO NOT SEND"
        status_class = "status-danger"
        status_icon = "🚨"
        status_message = "Potentially dangerous or sensitive content was detected."
    elif risk_lower in ("medium", "moderate"):
        decision = "REVIEW BEFORE SENDING"
        status_class = "status-warning"
        status_icon = "⚠️"
        status_message = "The prompt contains content that should be reviewed before sharing."
    elif risk_lower == "low":
        decision = "SAFE TO SEND"
        status_class = "status-safe"
        status_icon = "✓"
        status_message = "No significant security or privacy risk was detected."
    else:
        decision = "REVIEW RESULT"
        status_class = "status-warning"
        status_icon = "ℹ️"
        status_message = "The model could not confidently classify the prompt."

    safe_text = str(safe)
    if safe_text.lower() == "true":
        safe_text = "Yes"
    elif safe_text.lower() == "false":
        safe_text = "No"

    # -----------------------------------------------------
    # Decision banner
    # -----------------------------------------------------
    st.markdown(
        f"""
        <div class="status {status_class}">
            <div class="status-title">{status_icon} {decision}</div>
            <div class="status-text">{risk} risk · {status_message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # Metrics
    # -----------------------------------------------------
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Risk Level", risk)

    with c2:
        st.metric("Risk Score", f"{risk_score}/100")

    with c3:
        st.metric("Safe to Share", safe_text)

    st.write("")

    # -----------------------------------------------------
    # Detected items
    # -----------------------------------------------------
    with st.container(border=True):
        st.markdown(
            '<div class="section-title">🔎 Detected threats & sensitive data</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="section-subtitle">'
            'Information and patterns identified in the prompt.'
            '</div>',
            unsafe_allow_html=True,
        )

        if detected:
            if isinstance(detected, list):
                pills = "".join(
                    f'<span class="pill">{str(item)}</span>' for item in detected
                )
                st.markdown(pills, unsafe_allow_html=True)
            else:
                st.markdown(
                    f'<span class="pill">{str(detected)}</span>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                '<span class="pill">No specific items detected</span>',
                unsafe_allow_html=True,
            )

    st.write("")

    # -----------------------------------------------------
    # Explanation and recommendations
    # -----------------------------------------------------
    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            st.markdown(
                '<div class="section-title">⚠️ Why it is risky</div>',
                unsafe_allow_html=True,
            )

            if risks:
                if isinstance(risks, list):
                    for item in risks:
                        st.markdown(f"• {item}")
                else:
                    st.write(risks)
            else:
                st.write("No major privacy risks were identified.")

    with right:
        with st.container(border=True):
            st.markdown(
                '<div class="section-title">💡 Recommended action</div>',
                unsafe_allow_html=True,
            )

            if recommendations:
                if isinstance(recommendations, list):
                    for item in recommendations:
                        st.markdown(f"• {item}")
                else:
                    st.write(recommendations)
            else:
                st.write("No additional recommendations.")

    st.write("")

    # -----------------------------------------------------
    # Sanitized prompt
    # -----------------------------------------------------
    with st.container(border=True):
        st.markdown(
            '<div class="section-title">✨ Sanitized prompt</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="section-subtitle">'
            'Sensitive values are masked so the prompt can be reviewed safely.'
            '</div>',
            unsafe_allow_html=True,
        )

        st.code(str(sanitized), language="text")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        PromptShieldAI · AI Prompt Security & Privacy Analyzer · Powered by Gemma
    </div>
    """,
    unsafe_allow_html=True,
)
