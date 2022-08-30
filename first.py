import streamlit as st
import pandas as pd
st.title('my first app')
data=pd.read_csv('big_mart_data')
st.dataframe(data)
