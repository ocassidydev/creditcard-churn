import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_mushroom_data():
    """ 
    Load the raw mushroom data as a DataFrame for display on the dashboard
    Taken from Walkthrough Project 02 - Churnometer

    Args:
        None

    Returns:
        None
    """
    df = pd.read_csv("outputs/datasets/collection/mushrooms.csv")
    return df


def load_pkl_file(file_path):
    """ 
    Loads a pkl file to return pipeline objects for use on the streamlit app
    Taken from Walkthrough Project 02 - Churnometer

    Args:
        None

    Returns:
        None
    """
    return joblib.load(filename=file_path)