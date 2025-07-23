import streamlit as st
import pandas as pd
import os

# File path
file_path = "output/remoteok_jobs.csv"

# Check if file exists
if os.path.exists(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Convert all column names to lowercase
    df.columns = df.columns.str.lower()

    # Optional: remove rows with missing values
    df = df.dropna()

    # Filters
    locations = st.multiselect("Filter by Location:", options=df['location'].unique())
    tags = st.multiselect("Filter by Tags:", options=df['tags'].unique())

    # Apply filters
    filtered_df = df.copy()

    if locations:
        filtered_df = filtered_df[filtered_df['location'].isin(locations)]

    if tags:
        filtered_df = filtered_df[filtered_df['tags'].isin(tags)]

    # Display results
    st.title("📊 Remote Job Tracker")
    st.dataframe(filtered_df)

else:
    st.error("❌ File not found: output/remoteok_jobs.csv\n\n👉 Pehle `main.py` run karo taaki file ban jaaye.")
