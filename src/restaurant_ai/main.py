import streamlit as st
import generator
st.title("RESTURANT NAME GENERATOR")
cuisine = st.sidebar.selectbox("Pick a cuisine", ('Indian', 'Italian', 'Mexican', 'American', 'Arabic'))

def main():
    import streamlit.web.cli as stcli
    import sys
    sys.argv = ["streamlit", "run", __file__]
    stcli.main()

if cuisine :
    response = generator.restaurant_name_suggestor(cuisine)
    st.write(response['resturant_name'].strip())
    menu_items = response['item_list'].strip().split(",")
    st.write('Menu Items')
    for items in menu_items:
        st.write("-", items)

