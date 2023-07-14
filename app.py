import streamlit as st
from app_pages.multipage import MultiPage 

# load page scripts
from app_pages.page_summmary import page_summary_body

app = MultiPage(app_name = "Mushroom Safety")

app.add_page("Project Summary", page_summary_body)

app.run()