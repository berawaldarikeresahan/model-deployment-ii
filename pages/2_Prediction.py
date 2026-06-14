import streamlit as st

st.title("🤖 Promotion Prediction")

department = st.selectbox(
    "Department",
    [
        "Sales & Marketing",
        "Operations",
        "Technology"
    ]
)

age = st.slider(
    "Age",
    18,
    60,
    30
)

training_score = st.slider(
    "Training Score",
    0,
    100,
    50
)

if st.button("Predict"):
    st.success("Prediction page working")
