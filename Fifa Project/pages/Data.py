import streamlit as st
import pandas as pd
st.markdown("<h1> <center>Data Set </center> </h1>",unsafe_allow_html=True)
df =pd.read_csv("./sources/fifa_eda.csv")
st.write(df)