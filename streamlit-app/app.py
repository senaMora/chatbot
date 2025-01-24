import streamlit as st
import pandas as pd
import numpy as np



st.title("Hello, Streamlit!")
st.write("This is your first Streamlit app.")


number = st.slider("Pick a number", 0, 100)
st.write(f"You selected {number}")


data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["Monday", "Tuesday", "Wednesday"]
)
st.line_chart(data)




st.sidebar.title("Sidebar")
option = st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2"])

st.write(f"You selected {option}")
