import streamlit as st
import numpy as np
from utils.model_loader import load_model
from utils.history_manager import save_history

st.title("🤖 Promotion Prediction")
st.caption("Predict employee promotion eligibility using Machine Learning")

# Load model
try:
    model = load_model()
    model_loaded = True

except Exception as e:

    st.error(f"Model Error: {e}")
    model_loaded = False

left, right = st.columns(2)

# ==========================
# LEFT COLUMN
# ==========================

with left:

    st.subheader("👤 Employee Profile")

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

    region = st.selectbox(
        "Region",
        [f"region_{i}" for i in range(1, 35)]
    )

    age = st.slider(
        "Age",
        18,
        60,
        30
    )

    service = st.slider(
        "Length of Service (years)",
        1,
        37,
        5
    )

    education = st.selectbox(
        "Education Level",
        [
            "Below Secondary",
            "Bachelor's",
            "Master's & Above"
        ]
    )

    trainings = st.number_input(
        "No. of Trainings",
        min_value=1,
        max_value=10,
        value=2
    )

# ==========================
# RIGHT COLUMN
# ==========================

with right:

    st.subheader("📈 Performance Profile")

    rating = st.slider(
        "Previous Year Rating",
        1,
        5,
        3
    )

    gender = st.radio(
        "Gender",
        [
            "Male",
            "Female"
        ],
        horizontal=True
    )

    recruitment = st.selectbox(
        "Recruitment Channel",
        [
            "Referred",
            "Sourcing",
            "Other"
        ]
    )

    training_score = st.slider(
        "Avg Training Score",
        0,
        100,
        60
    )

    awards = st.radio(
        "Awards Won",
        [
            "No",
            "Yes"
        ],
        horizontal=True
    )

st.divider()

# ==========================
# PREDICTION BUTTON
# ==========================

if st.button(
    "🚀 Predict Promotion",
    use_container_width=True
) and model_loaded:

    try:

        # sementara placeholder
        data = np.array([
            [
                1, 1, 2, 1, 1, 2,
                age,
                rating,
                service,
                1 if awards == "Yes" else 0,
                training_score
            ]
        ])

        probability = model.predict_proba(
            data
        )[0][1]

        st.subheader("Prediction Result")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Promotion Probability",
                f"{probability*100:.1f}%"
            )

        with c2:
            st.metric(
                "Training Score",
                training_score
            )

        with c3:
            st.metric(
                "Performance Rating",
                rating
            )

        st.progress(
            int(probability * 100)
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
