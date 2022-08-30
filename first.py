import streamlit as st
import pandas as pd
st.title('my first app')
data=pd.read_excel('big_mart_data')
st.dataframe(data)
