import streamlit as st
from app_pages.multipage import MultiPage 

# load page scripts
from app_pages.page_summary import page_summary_body



from app_pages.page_predict_edible import page_predict_edible_body

app = MultiPage(app_name = "Mushroom Safety")

app.add_page("Project Summary", page_summary_body)



app.add_page("ML: Mushroom Edibility", page_predict_edible_body)

app.run()