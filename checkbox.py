import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("Iris.csv")
if st.checkbox('Show dataframe'):
    st.write(df)
