# Building a Data Dashboard with Streamlit

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Build an interactive data dashboard using Streamlit — load data, create charts, and add user controls.

## Prerequisites

- Python 3.9+
- Familiarity with Pandas and Matplotlib

## Step 1: Install Streamlit

```bash
pip install streamlit pandas plotly
```

## Step 2: Create the Dashboard

Create `dashboard.py`:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics Dashboard", layout="wide")
st.title("Project Analytics Dashboard")

# Sidebar controls
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Date Range", value=[])
category = st.sidebar.selectbox("Category", ["All", "Tutorial", "How-To", "Reference"])

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# Metrics row
col1, col2, col3 = st.columns(3)
col1.metric("Total Documents", len(df))
col2.metric("Contributors", df["author"].nunique())
col3.metric("This Month", len(df[df["created_at"] >= "2026-03-01"]))

# Chart
fig = px.bar(df.groupby("category").size().reset_index(name="count"),
             x="category", y="count", title="Documents by Category")
st.plotly_chart(fig, use_container_width=True)

# Data table
st.subheader("Recent Documents")
st.dataframe(df.sort_values("created_at", ascending=False).head(20))
```

## Step 3: Run the Dashboard

```bash
streamlit run dashboard.py
```

Opens at `http://localhost:8501` in your browser.

## Step 4: Deploy

```bash
# Using Streamlit Community Cloud (free)
# Push to GitHub, then connect at share.streamlit.io
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
