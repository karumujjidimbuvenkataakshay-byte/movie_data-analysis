
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Movie Rating Analysis", layout="wide")

st.title("🎬 Movie Rating Analysis Dashboard")
st.markdown("Analyze movie ratings using interactive visualizations.")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "movie_ratings.csv")

df = pd.read_csv(DATA_PATH)

st.sidebar.header("Filters")
genre = st.sidebar.multiselect(
    "Select Genre",
    df["genre"].unique(),
    df["genre"].unique()
)

df = df[df["genre"].isin(genre)]

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Average Ratings by Genre")
avg = df.groupby("genre")["rating"].mean()
st.bar_chart(avg)

st.subheader("Movie Details")
idx = st.slider("Select Movie Index", 0, len(df) - 1)
st.write(df.iloc[idx])
