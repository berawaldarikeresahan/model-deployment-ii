import streamlit as st
import numpy as np
from utils.model_loader import load_model
from utils.history_manager import save_history

st.title("🤖 Promotion Prediction Center")
st.caption("AI-powered employee promotion prediction")

try:
    model = load_model()
    model_loaded = True

except Exception as e:

    st.error(f"Model Error: {e}")
    model_loaded = False

left,right = st.columns([1.3,1])

with left:

    st.subheader("Employee Information")

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

    service = st.slider(
        "Length of Service",
        1,
        37,
        5
    )

with right:

    st.subheader("Performance")

    rating = st.slider(
        "Previous Rating",
        1,
        5,
        3
    )

    training_score = st.slider(
        "Training Score",
        0,
        100,
        50
    )

    awards = st.toggle(
        "Awards Won"
    )

st.divider()

if st.button(
    "🚀 Predict Promotion",
    use_container_width=True
) and model_loaded:

    data = np.array([
        [
            1,1,2,1,1,2,
            age,
            rating,
            service,
            int(awards),
            training_score
        ]
    ])

    try:

        probability = model.predict_proba(
            data
        )[0][1]

        st.subheader(
            "Prediction Result"
        )

        c1,c2,c3 = st.columns(3)

        with c1:

            st.metric(
                "Promotion Probability",
                f"{probability*100:.1f}%"
            )

        with c2:

            st.metric(
                "Performance Rating",
                rating
            )

        with c3:

            st.metric(
                "Training Score",
                training_score
            )

        st.progress(
            int(probability*100)
        )

        if probability >= 0.7:

            st.success(
                "🌟 High Promotion Potential"
            )

        elif probability >= 0.4:

            st.warning(
                "⚡ Medium Promotion Potential"
            )

        else:

            st.error(
                "🔻 Low Promotion Potential"
            )

        save_history(
            department,
            probability
        )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )
