import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📊 Executive Dashboard")

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric("Employees","54,808")

with k2:
    st.metric("Promotion Rate","8.5%")

with k3:
    st.metric("Departments","9")

with k4:
    st.metric("Regions","34")

st.divider()

department_df = pd.DataFrame({
    "Department":[
        "Sales",
        "Operations",
        "Technology",
        "Analytics"
    ],
    "Promotion":[
        120,
        180,
        250,
        90
    ]
})

fig = px.bar(
    department_df,
    x="Department",
    y="Promotion",
    title="Promotion by Department"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
