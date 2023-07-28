import streamlit as st
import pandas as pd
from src.data_management import load_mushroom_data, load_pkl_file

from src.machine_learning.predictive_analysis_ui import (
    predict_churn,
    predict_tenure,
    predict_cluster)
