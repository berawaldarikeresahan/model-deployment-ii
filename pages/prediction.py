import streamlit as st
import numpy as np
import pandas as pd
from utils.model_loader import load_model
from utils.history_manager import save_history

model = load_model()

st.title("🤖 Promotion Prediction")

left,right = st.columns([1.2,1])

with left:

    department = st.selectbox(
        "Department",
        [
            "Sales & Marketing",
            "Operations",
            "Technology",
            "Analytics",
            "R&D",
            "Procurement",
            "Finance",
            "HR",
            "Legal"
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

with right:

    rating = st.slider(
        "Previous Rating",
        1,
        5,
        3
    )

    service = st.slider(
        "Length of Service",
        1,
        37,
        5
    )

    awards = st.toggle(
        "Awards Won"
    )

if st.button("🚀 Predict Promotion"):

    # Ganti dengan encoding asli
    data = np.array([
        [1,1,2,1,1,2,
         age,
         rating,
         service,
         int(awards),
         training_score]
    ])

    prediction = model.predict(data)

    probability = model.predict_proba(
        data
    )[0][1]

    st.metric(
        "Promotion Probability",
        f"{probability*100:.1f}%"
    )

    st.progress(
        int(probability*100)
    )

    if probability > 0.7:

        st.success(
            "High Promotion Potential"
        )

    elif probability > 0.4:

        st.warning(
            "Medium Promotion Potential"
        )

    else:

        st.error(
            "Low Promotion Potential"
        )

    save_history(
        department,
        probability
    )
