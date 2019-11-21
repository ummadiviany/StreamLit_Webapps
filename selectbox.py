import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("Iris.csv")
option = st.selectbox(
    'Which Species you like most?',
     df['Species'].unique())
'You selected: ', option
