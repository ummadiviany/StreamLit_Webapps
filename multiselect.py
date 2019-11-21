import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("automobile.csv")
options = st.multiselect(
 'What are your favorite Car Makers?', df['make'].unique())
st.write('You selected:', options)