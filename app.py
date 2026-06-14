import streamlit as st

st.set_page_config(
    page_title="Employee Promotion Intelligence",
    page_icon="📈",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<div class='hero-card'>
<h1>🚀 Employee Promotion Intelligence</h1>
<p>AI-Powered HR Analytics Dashboard</p>
</div>
""",
unsafe_allow_html=True)

st.markdown("---")

st.info(
"""
Use the sidebar to navigate between dashboard pages.
"""
)
