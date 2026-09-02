import streamlit as st
from gemma import analyze_prompt

st.set_page_config(page_title="PromptShieldAI", page_icon="🛡️", layout="wide", initial_sidebar_state="collapsed")

st.markdown(r'''
<style>
:root{--bg:#070b12;--panel:#0d131d;--border:#1d2938;--text:#f4f7fb;--muted:#8d9aad;--blue:#4f8cff}
.stApp{background:radial-gradient(circle at 50% -15%,rgba(79,140,255,.20),transparent 34%),radial-gradient(circle at 90% 25%,rgba(94,92,230,.08),transparent 25%),var(--bg);color:var(--text)}
.main .block-container{max-width:1120px;padding:34px 24px 52px}
#MainMenu,footer,header{visibility:hidden}
p,label,.stMarkdown,.stCaption{color:var(--text)}
.hero{text-align:center;padding:22px 10px 34px}.brand-mark{width:64px;height:64px;margin:0 auto 17px;display:flex;align-items:center;justify-content:center;border-radius:19px;font-size:31px;background:linear-gradient(145deg,#3d7cff,#6c9dff);box-shadow:0 0 0 7px rgba(79,140,255,.07),0 18px 50px rgba(55,112,255,.25)}
.hero h1{margin:0;color:#fff;font-size:clamp(36px,6vw,56px);line-height:1.02;font-weight:800;letter-spacing:-2.8px}.hero .tagline{max-width:700px;margin:14px auto 0;color:#9ba8b9;font-size:17px;line-height:1.55}.mini-badge{display:inline-block;margin-top:17px;padding:6px 11px;border:1px solid #20304a;border-radius:999px;background:rgba(79,140,255,.07);color:#9dbfff;font-size:12px;font-weight:650}
[data-testid="stVerticalBlockBorderWrapper"]{background:linear-gradient(145deg,rgba(17,25,37,.94),rgba(10,15,23,.94));border:1px solid var(--border);border-radius:20px;box-shadow:0 18px 55px rgba(0,0,0,.24);padding:5px 3px}
.section-title{color:#f7f9fc;font-size:19px;font-weight:750;letter-spacing:-.35px;margin-bottom:4px}.section-subtitle{color:var(--muted);font-size:13px;line-height:1.5;margin-bottom:13px}
textarea{background:#080d15!important;color:#edf3fb!important;border:1px solid #263447!important;border-radius:15px!important;font-size:15px!important;line-height:1.6!important;padding:15px!important;caret-color:#78a7ff!important;box-shadow:inset 0 1px 1px rgba(255,255,255,.02)!important}textarea::placeholder{color:#647286!important;opacity:1!important}textarea:focus{border-color:#4f8cff!important;box-shadow:0 0 0 3px rgba(79,140,255,.14),0 8px 25px rgba(0,0,0,.18)!important}
.stButton>button{min-height:52px;border:1px solid rgba(132,174,255,.25);border-radius:14px;background:linear-gradient(135deg,#4b86ff,#356fe8);color:#fff;font-size:15px;font-weight:750;box-shadow:0 12px 28px rgba(50,105,235,.22);transition:all .18s ease}.stButton>button:hover{border-color:rgba(155,190,255,.45);background:linear-gradient(135deg,#5b91ff,#4079ef);transform:translateY(-1px);box-shadow:0 15px 32px rgba(50,105,235,.30)}
[data-testid="stMetric"]{min-height:105px;background:#0d141f;border:1px solid #1d2938;border-radius:17px;padding:17px 18px;box-shadow:0 12px 32px rgba(0,0,0,.17)}[data-testid="stMetricLabel"]{color:#8290a3!important;font-size:12px!important;font-weight:650!important;text-transform:uppercase;letter-spacing:.55px}[data-testid="stMetricValue"]{color:#f5f8fc!important;font-size:25px!important;font-weight:760!important}
.status{border-radius:17px;padding:18px 20px;margin:18px 0 16px;border:1px solid}.status-safe{background:rgba(50,213,131,.08);border-color:rgba(50,213,131,.25);color:#71e8aa}.status-warning{background:rgba(245,196,81,.08);border-color:rgba(245,196,81,.25);color:#f6d578}.status-danger{background:rgba(255,92,103,.09);border-color:rgba(255,92,103,.28);color:#ff858d}.status-title{font-size:21px;font-weight:800;letter-spacing:-.35px}.status-text{margin-top:5px;color:#9aa8ba;font-size:13px;line-height:1.5}
.pill{display:inline-block;margin:3px 5px 3px 0;padding:7px 11px;border-radius:999px;background:#141e2c;border:1px solid #26364b;color:#b9c8dc;font-size:12px;font-weight:650}
[data-testid="stCode"]{border:1px solid #1f2c3d!important;border-radius:14px!important;overflow:hidden}[data-testid="stCode"] pre{background:#080d15!important}[data-testid="stAlert"]{border-radius:13px!important}.footer{text-align:center;color:#566477;font-size:12px;padding:28px 0 4px}
@media(max-width:700px){.main .block-container{padding:18px 13px 36px}.hero{padding:10px 4px 24px}.brand-mark{width:56px;height:56px;border-radius:17px;font-size:27px;margin-bottom:14px}.hero h1{font-size:38px;letter-spacing:-1.9px}.hero .tagline{font-size:14px;max-width:350px}[data-testid="stVerticalBlockBorderWrapper"]{border-radius:17px}textarea{font-size:14px!important}[data-testid="stMetric"]{min-height:88px;padding:13px 14px}[data-testid="stMetricValue"]{font-size:21px!important}.status-title{font-size:18px}}
</style>
''', unsafe_allow_html=True)

st.markdown('''<div class="hero"><div class="brand-mark">🛡️</div><h1>PromptShieldAI</h1><div class="tagline">Check your prompt before it reaches an AI model. Detect prompt attacks, exposed credentials, PII, and privacy risks.</div><div class="mini-badge">AI PROMPT SECURITY · PRIVACY FIRST</div></div>''', unsafe_allow_html=True)

with st.container(border=True):
    st.markdown('<div class="section-title">Analyze a prompt</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Paste the prompt or code you are about to send to an AI model.</div>', unsafe_allow_html=True)
    prompt=st.text_area("Prompt",height=220,placeholder="Paste your prompt here...",label_visibility="collapsed")
    analyze=st.button("🛡️  Shield My Prompt",use_container_width=True)

if analyze:
    if not prompt.strip(): st.warning("Please enter a prompt first."); st.stop()
    with st.spinner("Gemma is checking your prompt..."): result=analyze_prompt(prompt.strip())
    risk=str(result.get("risk_level","Unknown")); privacy_score=result.get("privacy_score",0); safe=result.get("safe_to_share","Unknown")
    detected=result.get("detected_items",[]); risks=result.get("privacy_risks",[]); recommendations=result.get("recommendations",[]); sanitized=result.get("sanitized_prompt",prompt)
    try: risk_score=round(max(0,min(100,100-float(privacy_score))))
    except (TypeError,ValueError): risk_score=0
    risk_lower=risk.lower()
    if risk_lower in ("critical","high"): decision="BLOCK — DO NOT SEND"; status_class="status-danger"; status_icon="🚨"; status_message="Potentially dangerous or sensitive content was detected."
    elif risk_lower in ("medium","moderate"): decision="REVIEW BEFORE SENDING"; status_class="status-warning"; status_icon="⚠️"; status_message="The prompt contains content that should be reviewed before sharing."
    elif risk_lower=="low": decision="SAFE TO SEND"; status_class="status-safe"; status_icon="✓"; status_message="No significant security or privacy risk was detected."
    else: decision="REVIEW RESULT"; status_class="status-warning"; status_icon="ℹ️"; status_message="The model could not confidently classify the prompt."
    safe_text=str(safe)
    if safe_text.lower()=="true": safe_text="Yes"
    elif safe_text.lower()=="false": safe_text="No"
    st.markdown(f'<div class="status {status_class}"><div class="status-title">{status_icon} {decision}</div><div class="status-text">{risk} risk · {status_message}</div></div>',unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    with c1: st.metric("Risk Level",risk)
    with c2: st.metric("Risk Score",f"{risk_score}/100")
    with c3: st.metric("Safe to Share",safe_text)
    st.write("")
    with st.container(border=True):
        st.markdown('<div class="section-title">🔎 Detected threats & sensitive data</div>',unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Information and patterns identified in the prompt.</div>',unsafe_allow_html=True)
        if detected:
            if isinstance(detected,list): st.markdown("".join(f'<span class="pill">{str(item)}</span>' for item in detected),unsafe_allow_html=True)
            else: st.markdown(f'<span class="pill">{str(detected)}</span>',unsafe_allow_html=True)
        else: st.markdown('<span class="pill">No specific items detected</span>',unsafe_allow_html=True)
    st.write("")
    left,right=st.columns(2)
    with left:
        with st.container(border=True):
            st.markdown('<div class="section-title">⚠️ Why it is risky</div>',unsafe_allow_html=True)
            if risks:
                if isinstance(risks,list):
                    for item in risks: st.markdown(f"• {item}")
                else: st.write(risks)
            else: st.write("No major privacy risks were identified.")
    with right:
        with st.container(border=True):
            st.markdown('<div class="section-title">💡 Recommended action</div>',unsafe_allow_html=True)
            if recommendations:
                if isinstance(recommendations,list):
                    for item in recommendations: st.markdown(f"• {item}")
                else: st.write(recommendations)
            else: st.write("No additional recommendations.")
    st.write("")
    with st.container(border=True):
        st.markdown('<div class="section-title">✨ Sanitized prompt</div>',unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Sensitive values are masked so the prompt can be reviewed safely.</div>',unsafe_allow_html=True)
        st.code(str(sanitized),language="text")

st.markdown('<div class="footer">PromptShieldAI · AI Prompt Security & Privacy Analyzer · Powered by Gemma</div>',unsafe_allow_html=True)
