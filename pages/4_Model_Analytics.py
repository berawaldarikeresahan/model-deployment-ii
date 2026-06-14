import streamlit as st

st.title("📈 Model Performance")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Accuracy",
        "94%"
    )

with c2:
    st.metric(
        "Precision",
        "92%"
    )

with c3:
    st.metric(
        "Recall",
        "90%"
    )

with c4:
    st.metric(
        "ROC-AUC",
        "95%"
    )

st.info(
    """
    Replace these metrics with actual values
    from your trained model.
    """
)
