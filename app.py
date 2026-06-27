import streamlit as st
from chatbot import get_health_response
from report_combiner import combine_reports
from report_analyzer import analyze_medical_report

st.set_page_config(page_title="AI Healthcare Assistant", page_icon="💊", layout="wide")
st.title("💊 AI Healthcare Assistant")

menu = st.sidebar.radio("Select Module", ["Health Chatbot", "Combine Reports"])

# =========================================
# 1️⃣ HEALTH CHATBOT MODULE
# =========================================
if menu == "Health Chatbot":
    st.header("🩺 Ask Health-Related Questions")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "user_inputs" not in st.session_state:
        st.session_state.user_inputs = []

    if st.button("🔄 Reset Chat"):
        st.session_state.chat_history = []
        st.session_state.user_inputs = []
        st.success("Chat has been reset!")

    def handle_send():
        latest = st.session_state.input_box.strip()
        if not latest:
            return
        prior = st.session_state.user_inputs.copy()
        st.session_state.user_inputs.append(latest)
        ai_reply = get_health_response(latest_question=latest, prior_user_inputs=prior)
        st.session_state.chat_history.append(("🧑‍⚕️ You", latest))
        st.session_state.chat_history.append(("🤖 Assistant", ai_reply))
        st.session_state.input_box = ""

    st.text_input(
        "Type your question here...",
        key="input_box",
        placeholder="e.g., I have a headache. What should I do?",
        on_change=handle_send,
    )
    st.button("Send", on_click=handle_send)

    st.subheader("💬 Chat History")
    for role, message in reversed(st.session_state.chat_history):
        bg_color = "#f7f7f7" if role == "🧑‍⚕️ You" else "#e9f7ef"
        st.markdown(
            f"<div style='background-color:{bg_color}; padding:10px; border-radius:10px; margin:5px 0;'><b>{role}:</b> {message}</div>",
            unsafe_allow_html=True,
        )

# =========================================
# 2️⃣ REPORT COMBINER MODULE
# =========================================
elif menu == "Combine Reports":
    st.header("📑 Combine Multiple Reports into One")

    uploaded_files = st.file_uploader(
        "Upload multiple reports (PDFs or images)", 
        type=["pdf", "png", "jpg", "jpeg"], 
        accept_multiple_files=True
    )

    analyze_flag = st.checkbox("🔍 Analyze Combined Report after Generation")

    if st.button("Generate Combined Report"):
        if uploaded_files:
            output_path = combine_reports(uploaded_files)
            st.success("✅ Combined report generated successfully!")

            with open(output_path, "rb") as f:
                st.download_button(
                    label="📥 Download Combined Report",
                    data=f,
                    file_name="combined_report.pdf"
                )

            if analyze_flag:
                with st.spinner("Analyzing the report using AI... please wait ⏳"):
                    analysis_result = analyze_medical_report(output_path)
                st.subheader("🧠 AI Report Analysis")
                st.markdown(f"<div style='background-color:#f9f9f9; padding:15px; border-radius:10px;'>{analysis_result}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please upload at least one report file.")
