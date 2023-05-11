import streamlit as st
from streamlit_option_menu import option_menu

# Custom side bar
def make_side_bar(titles, icons, default_index):
    st.subheader('House Rent make by Group 04')
    if st.button('Congratulation!✨'):
        st.balloons()
    else:
        st.write(' ')
    return option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )
