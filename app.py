import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

# Title of the dashboard
st.title("Simple Dashboard with Different Charts")

# Sidebar options
st.sidebar.header("Dashboard Options")
chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar", "Line", "Scatter", "Pie"])

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 23, 45, 67],
    'More Values': [15, 25, 35, 40]
})

# Bar Chart
if chart_type == "Bar":
    st.subheader("Bar Chart (Matplotlib)")
    fig, ax = plt.subplots()
    ax.bar(data['Category'], data['Values'])
    st.pyplot(fig)

# Line Chart
if chart_type == "Line":
    st.subheader("Line Chart (Altair)")
    line_chart = alt.Chart(data).mark_line().encode(
        x='Category',
        y='Values'
    )
    st.altair_chart(line_chart, use_container_width=True)

# Scatter Plot
if chart_type == "Scatter":
    st.subheader("Scatter Plot (Plotly)")
    scatter_fig = px.scatter(data, x='Category', y='More Values', size='Values', color='Category')
    st.plotly_chart(scatter_fig)

# Pie Chart
if chart_type == "Pie":
    st.subheader("Pie Chart (Plotly)")
    pie_fig = px.pie(data, values='Values', names='Category', title='Pie Chart Example')
    st.plotly_chart(pie_fig)

# Show the data in a table format
st.subheader("Data Table")
st.write(data)
