from urllib import response
import streamlit as st
import langchain_helper
import time

st.title("Restaurant name generator")

cuisine= st.sidebar.selectbox("Pick a Cuisine",("Indian", "Italian", "Mexican", "American"))

if cuisine:
    try:
        time.sleep(10)
        response = langchain_helper.generate_item_name_items(cuisine)   
        st.header('Restaurant Name: '+ response['restaurant_name'].strip())
        st.write('Menu items')
        menu_items = response['menu_items'].strip().split('-')
        filter(None, menu_items)

        for item in menu_items:
            if(item.strip() != ':' and len(item)>0):
                st.write(item)
    except Exception as err:
        print('Err: ', err)
        st.write("System busy. Please try after some time")
