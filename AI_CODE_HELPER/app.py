import streamlit as st
import json
from ai_code_brain import ask_ai

data = json.load(open("DATA/code_knowledge.json", encoding="utf8"))

st.set_page_config(layout="wide")
st.title("AI CODE HELPER")

tab1, tab2, tab3, tab4 = st.tabs([
    "Code Explorer",
    "AI Assistant",
    "Syntax Errors",
    "Potential Issues"
])

# Code Explorer

with tab1:
    st.subheader("Functions")
    for name, f in data["functions"].items():
        with st.expander(name):
            st.write("File:", f["file"])
            st.write("Lines:", f["start"], "-", f["end"])
            st.write("Called by:", f["called_by"])
            st.code(f["code"])

    st.subheader("Classes")
    for name, c in data["classes"].items():
        with st.expander(name):
            st.write("File:", c["file"])
            st.write("Lines:", c["start"], "-", c["end"])
            st.code(c["code"])

# AI Assistant


with tab2:
    q = st.text_input("Ask about code, errors, bugs, or improvements")
    if q:
        st.write(ask_ai(q))

# Syntax Errors

with tab3:
    for e in data["syntax_errors"]:
        st.error(f"{e['file']} | Line {e['line']} | {e['message']}")

# Logical Bugs


with tab4:
    for b in data["logical_bugs"]:
        st.warning(
            f"{b['type']} → {b.get('name','')} ({b['file']})"
        )
