import streamlit as st
import os
from streamlit_card import card
from st_on_hover_tabs import on_hover_tabs
from annotated_text import annotated_text

st.set_page_config(page_title="MatCom Dashboard", page_icon="⭐", layout="wide")


st.title("⭐ Bienvenido al Dashboard de MatCom")
left, right = st.columns(2)
with right:
    st.info("""
        Si usted es claustro de la facultad y desea modificar los datos, introduzca
        la contraseña correspondiente. De lo contrario, puede leer los datos pero no modificar.
        Si usted cree que debería tener acceso, contacte con [@apiad](https://t.me/apiad) en Telegram.
    """)
    hasClicked = card(
      title="Hello World!",
      text="Some description",
      image="http://placekitten.com/200/300",
      url="https://github.com/gamcoh/st-card"
    )
    # password = st.text_input("Contraseña de acceso", type="password")
    # try:
    #     assert (password == st.secrets["password"])
    #     st.success("Acceso de modificación")
    #     st.session_state.write_access = True
    # except:
    #     st.error("Acceso de solo lectura")
with left:
    with open("main.md") as fp:
        st.markdown(fp.read())
