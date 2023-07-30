import streamlit as st
from app_pages.multipage import MultiPage

# load page scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_mushroom_edibility_study import page_mushroom_edibility_study_body
from app_pages.page_mushroom import page_mushroom_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_edible import page_predict_edible_body
from app_pages.page_cluster_mushroom import page_cluster_mushroom_body
from app_pages.page_classify_mushroom import page_classify_mushroom_body

app = MultiPage(app_name="Mushroom Safety")

app.add_page("Project Summary", page_summary_body)
app.add_page("Mushroom Edibility Study", page_mushroom_edibility_study_body)
app.add_page("Mushroom Edibility Detector", page_mushroom_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Mushroom Edibility", page_predict_edible_body)
app.add_page("ML: Mushroom Cluster Analysis", page_cluster_mushroom_body)
app.add_page("ML: Mushroom Classify Cluster", page_classify_mushroom_body)

app.run()
