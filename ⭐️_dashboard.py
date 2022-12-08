import streamlit as st
import os
from streamlit_card import card
from st_on_hover_tabs import on_hover_tabs
from annotated_text import annotated_text
from streamlit.components.v1 import components

st.set_page_config(page_title="MatCom Dashboard", page_icon="⭐", layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True) 

st.title("⭐ Bienvenido al Dashboard de MatCom")

left, right = st.columns(2)

with left:

    tab1, tab2 = st.tabs(["🔍 Boolean Model", "🔍 Vectorial Model"])
    with tab1:

        for i in range(10):
            with st.expander(f"**[Job's Name {i}](github.com) from 🇨🇱**"):
                st.markdown("""
                - 💵 1000-2000
                - 📢 02/2020
                """)

                st.write("")

                annotated_text(
                    ("python ", "🤩" ),
                    ' / ',
                    ("junior","🤩" ),
                    ' / ',
                    ("ia", '😍'),
                    ' / ',
                    ("html", '🥲'),
                )

                st.write("")
                st.write("")
        container = st.container()

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
