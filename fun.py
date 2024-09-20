import streamlit as st

class buttons:
    def __init__ (self,button_name):
        if st.button(f"square of  {button_name}"):
            st.toast(button_name*button_name)

for i in range(10):
    buttons(i)
