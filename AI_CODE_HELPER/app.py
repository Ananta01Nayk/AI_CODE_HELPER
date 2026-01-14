import streamlit as st
import json
from ai_code_brain import ask_ai

data=json.load(open("DATA/code_knowledge.json"))

st.set_page_config(layout="wide")
st.title("AI_CODE_HELPER")

tab1, tab2 = st.tabs(["Code Explorer","AI_HELPER"])

with tab1:
    st.subheader("Functions")
    for n,f in data["functions"].items():
        with st.expander(n):
            st.write("file:",f["file"])
            st.write("lines:",f["start"],"-",f["end"])
            st.write("dependent by:",f["called_by"])
            st.code(f["code"])

    st.subheader("Classes")
    for n,c in data["classes"].items():
        with st.expander(n):
            st.write("file:",c["file"])
            st.write("lines:",c["start"],"-",c["end"])
            st.code(c["code"])

with tab2:
    q=st.text_input("ask about any function or feature change")
    if q:
        st.write(ask_ai(q))
