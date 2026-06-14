import streamlit as st
import pandas as pd

st.title("📜 Prediction History")

try:

    df = pd.read_csv(
        "history.csv"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(
        index=False
    )

    st.download_button(
        "📥 Download CSV",
        csv,
        "history.csv",
        "text/csv"
    )

except:

    st.warning(
        "No prediction history found"
    )
