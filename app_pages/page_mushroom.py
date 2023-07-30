import streamlit as st
import pandas as pd
from src.data_management import load_mushroom_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (predict_edible, predict_cluster)


def page_mushroom_body():
    """ Page for displaying the model input widget and then predictions of edibility and cluster based on user input """
    version = 'v1'
    edible_pipe_fe = load_pkl_file(f'outputs/ml_pipeline/predict_edible/{version}/clf_pipeline_feat_eng.pkl')
    edible_pipe_model = load_pkl_file(f"outputs/ml_pipeline/predict_edible/{version}/clf_pipeline_model.pkl")

    cluster_pipe = load_pkl_file(f"outputs/ml_pipeline/cluster_analysis/{version}/classify_pipeline.pkl")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv").columns.to_list())
    cluster_profile = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    st.write("### Mushroom Edibility Interface")
    st.success(f"* The client would like to determine whether a given mushroom is edible. It is essential that any means of doing this has a false "
            f" positive rate of zero, as the client does not want to inadvertently sell poisonous mushrooms mistakenly identified as edible."
            f"* The client has informed us that there are a number of distinct species of mushroom in the dataset. They want to investigate "
            f"if this can be identified by grouping mushrooms with similar categories by means of a cluster algorithm, and to determine the rates "
            f"of edibility among each identified cluster. Ideally, this will allow the picking team to identify certain categorical heuristics for "
            f"selecting edible mushrooms.")

    st.info(f"* The client is interested in determining whether a given mushroom is edible or poisonous.\n"
            f"* The client would also like to know which cluster of similar mushrooms a given " 
            f"mushroom belongs to, in order to group mushrooms similar in appearance and heurestically "
            f"rule out/target certain mushrooms for harvesting if their cluster tends to be poisonous/edible." )
    st.write("---")

    X_live = DrawInputsWidgets()

    if st.button("Run Predictive Analysis"):
        predict_edible(X_live, edible_pipe_fe, edible_pipe_model)
        predict_cluster(X_live, cluster_features, cluster_pipe, cluster_profile)

def DrawInputsWidgets():
    """ Creates the widget for the user to input mushroom categorical data, which is then returned for the pipelines to predict on """
    df = load_mushroom_data()

    # we create input widgets only for 22 features
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)
    col9, col10, col11, col12 = st.beta_columns(4)
    col13, col14, col15, col16 = st.beta_columns(4)
    col17, col18, col19, col20 = st.beta_columns(4)
    col21, col22, col23, col24 = st.beta_columns(4)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
    # 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
    # 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
    # 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
    # 'stalk-surface-below-ring', 'stalk-color-above-ring',
    # 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
    # 'ring-type', 'spore-print-color', 'population', 'habitat'

    X_live = pd.DataFrame([], index=[0])

    with col1:
        feature = "cap-shape"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "cap-surface"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "cap-color"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "bruises"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col5:
        feature = "odor"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col6:
        feature = "gill-attachment"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col7:
        feature = "gill-spacing"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col8:
        feature = "gill-size"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col9:
        feature = "gill-color"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col10:
        feature = "stalk-shape"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col11:
        feature = "stalk-root"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col12:
        feature = "stalk-surface-above-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col13:
        feature = "stalk-surface-below-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col14:
        feature = "stalk-color-above-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col15:
        feature = "stalk-color-below-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col16:
        feature = "veil-type"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col17:
        feature = "veil-color"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col18:
        feature = "ring-number"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col19:
        feature = "ring-type"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col20:
        feature = "spore-print-color"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col21:
        feature = "population"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col22:
        feature = "habitat"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget


    return X_live
