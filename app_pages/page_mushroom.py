import streamlit as st
import pandas as pd
from src.data_management import load_mushroom_data, load_pkl_file

from src.machine_learning.predictive_analysis_ui import (
    predict_edible,
    predict_cluster)


def page_mushroom_body():

    # load predict edible files
    version = 'v1'
    edible_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_edible/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    edible_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_edible/{version}/clf_pipeline_model.pkl")
    edible_features = (pd.read_csv(f"outputs/ml_pipeline/predict_edible/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )

    # load cluster analysis files
    version = 'v1'
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    st.write("### Mushroom Edibility Interface")
    st.info(
        f"* Test"
    )
    st.write("---")

    # Generate Live Data
    check_variables_for_UI(edible_features, cluster_features)
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        _prediction = predict_edible(
            X_live, edible_features, edible_pipe_dc_fe, edible_pipe_model)

        predict_cluster(X_live, cluster_features,
                        cluster_pipe, cluster_profile)


def check_variables_for_UI(edible_features, cluster_features):
    import itertools

    # The widgets inputs are the features used in all pipelines (tenure, edible, cluster)
    # We combine them only with unique values
    combined_features = set(
        list(
            itertools.chain(edible_features, cluster_features)
        )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    # load dataset
    df = load_mushroom_data()
    percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets only for 19 features
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)
    col9, col10, col11, col12 = st.beta_columns(4)
    col13, col14, col15, col16 = st.beta_columns(4)
    col17, col18, col19, col20 = st.beta_columns(4)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
    # {'cap-color', 'stalk-color-below-ring', 'veil-type', 'stalk-root', 'stalk-shape', 'cap-surface', 'stalk-color-above-ring',
    # 'ring-number', 'bruises', 'gill-spacing', 'population', 'gill-size', 'veil-color', 'cap-shape', 'habitat', 'stalk-surface-below-ring',
    # 'ring-type', 'stalk-surface-above-ring', 'odor'}

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable
    # and set initial values
    with col1:
        feature = "cap-color"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "stalk-color-below-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "veil-type"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "stalk-root"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col5:
        feature = "stalk-shape"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col6:
        feature = "cap-surface"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col7:
        feature = "stalk-color-above-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col8:
        feature = "ring-number"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col9:
        feature = "bruises"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col10:
        feature = "gill-spacing"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col11:
        feature = "population"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col12:
        feature = "gill-size"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col13:
        feature = "veil-color"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col14:
        feature = "cap-shape"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col15:
        feature = "habitat"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col16:
        feature = "stalk-surface-below-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col17:
        feature = "ring-type"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col18:
        feature = "stalk-surface-above-ring"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col19:
        feature = "odor"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget
    # st.write(X_live)

    return X_live
