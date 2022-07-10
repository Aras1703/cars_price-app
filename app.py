import streamlit as st

from views import home
from views import dataset

st.set_page_config(
    page_title='Cars price prediction',
    page_icon='https://telkomuniversity.ac.id/wp-content/uploads/2019/07/cropped-favicon-2-32x32.png',
    layout='wide'
)

PAGES = {
    "🌎 Home Page": home,
    "💡 Dataset": dataset,
}

st.sidebar.subheader('Navigate')

page = st.sidebar.selectbox("Change Page", list(PAGES.keys()))
page = PAGES[page]
page.app()