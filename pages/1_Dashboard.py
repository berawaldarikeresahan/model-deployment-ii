import streamlit as st
import pandas as pd

st.title("📊 Executive Dashboard")
st.caption("Employee Promotion Intelligence Platform")

st.divider()

# KPI SECTION

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👥 Employees",
        "54,808"
    )

with c2:
    st.metric(
        "🎯 Promotion Rate",
        "8.5%"
    )

with c3:
    st.metric(
        "🏢 Departments",
        "9"
    )

with c4:
    st.metric(
        "🌍 Regions",
        "34"
    )

st.divider()

# CHART

department_df = pd.DataFrame({
    "Department": [
        "Sales",
        "Operations",
        "Technology",
        "Analytics"
    ],
    "Promotion": [
        120,
        180,
        250,
        90
    ]
})

st.subheader("📈 Promotion Distribution")

st.bar_chart(
    department_df.set_index(
        "Department"
    )
)

st.divider()

# INSIGHT SECTION

left, right = st.columns(2)

with left:

    st.success(
        """
        🏆 Top Department

        Technology department shows
        the highest promotion count.
        """
    )

with right:

    st.warning(
        """
        ⚠️ Attention Needed

        Analytics department has
        the lowest promotion count.
        """
    )

st.divider()

st.subheader("💡 Key Business Insights")

st.info(
    """
    • Technology employees have the strongest promotion performance.

    • Promotion opportunities appear uneven across departments.

    • Analytics department may require additional training programs.

    • Promotion rate remains below 10%, indicating a selective promotion strategy.
    """
)
