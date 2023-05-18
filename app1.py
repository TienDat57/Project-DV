import streamlit as st

from components import side_bar
from pages import home, collection, explorations, question, reflection

# set up config page
st.set_page_config(
   page_title="House Rent", 
   layout="wide",
   initial_sidebar_state="expanded",
)

apps = [
    {"page": home.app, "title": "Home", "icon": "house"},
    {"page": collection.app, "title": "Data Collection", "icon": "map"},
    {"page": explorations.app, "title": "Data Explorations", "icon": "graph-up-arrow"},
    {"page": question.app, "title": "Question & Insight", "icon": "patch-question"},
    {"page": reflection.app, "title": "Reflection", "icon": "box-seam"}
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

# Get index of page when select 
params = st.experimental_get_query_params()
if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

# Custom side bar
with st.sidebar:
    selected = side_bar.make_side_bar(titles, icons, default_index)

# Display the selected page
for app in apps:
    if app["title"] == selected:
        app["page"]()
        break
