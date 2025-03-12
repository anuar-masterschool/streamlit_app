import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Title example")
st.write("Write example")

csv_file = st.file_uploader("Upload a CSV", type=["csv"])

if csv_file is not None:
    df = pd.read_csv(csv_file)

    st.subheader("Data")
    st.write(df)

    st.subheader("Summary")
    st.write(df.describe())

    st.subheader("Filter")
    columns = df.columns.tolist()
    filter_value = st.select_slider("Min value to filter", df['Receipt_Count'])
    df_filtered = df[df['Receipt_Count'] >= filter_value]

    st.write(df_filtered)

    st.subheader("Plot")
    # Create a figure and axes
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(df_filtered["# Date"], df_filtered["Receipt_Count"])

    # Set title and labels
    ax.set_title("Scanned Receipts Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Receipt Count")

    # Display the plot in Streamlit
    st.pyplot(fig)