import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("automobile.csv")
makes = st.multiselect('Show cars for Brands?', df['make'].unique())
engines = st.multiselect('Show by engine-location ?', df['engine-location'].unique())# Filter dataframe
new_df = df[(df['make'].isin(makes)) & (df['engine-location'].isin(engines))]# write dataframe to screen
st.write(new_df)