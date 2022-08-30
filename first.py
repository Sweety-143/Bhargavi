import streamlit as st
st.title('my first app')
data=pd.read_csv('big_mart_data)
st.dataframe(data)
