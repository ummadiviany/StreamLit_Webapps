import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
'''
# Automible App.This very simple webapp allows you to select and visualize cars from certain makers and certain specifications of cars.
'''
df = st.cache(pd.read_csv)("automobile.csv")
makes = st.sidebar.multiselect('Show cars for Brands?', df['make'].unique())
engines = st.sidebar.multiselect('Show by engine-location ?', df['engine-location'].unique())# Filter dataframe
new_df = df[(df['make'].isin(makes)) & (df['engine-location'].isin(engines))]# write dataframe to screen
st.write(new_df)

# create figure using plotly express
fig = px.scatter(new_df, x ='horsepower',y='peak-rpm',color='symboling')# Plot!
st.plotly_chart(fig)