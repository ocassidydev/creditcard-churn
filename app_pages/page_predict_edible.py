import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_mushroom_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_predict_edible_body():

    version = 'v1'
    # load needed files
    edible_pipe_fe = load_pkl_file(f'outputs/ml_pipeline/predict_edible/{version}/clf_pipeline_feat_eng.pkl')
    edible_pipe_model = load_pkl_file(f"outputs/ml_pipeline/predict_edible/{version}/clf_pipeline_model.pkl")
    edible_feat_importance = plt.imread(f"outputs/ml_pipeline/predict_edible/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_edible/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_edible/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predict_edible/{version}/y_train.csv").values
    y_test = pd.read_csv(f"outputs/ml_pipeline/predict_edible/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Mushroom Edibility")
    st.info(
        f"* The pipeline was tuned aiming at least 1.00 precision on 'edible', "
        f"and a recall of 0.90 on 'edible', since in this project we are interested "
        f"in detecting a potential edible mushrooms at a high rate with no false positives "
        f"(poisonous mushrooms labelled as edible).\n"
        f"* The pipeline performance on train and test set was a precision=1.00 recall=1.00, "
        f"and precision=1.00 recall=1.00, respectively.\n"
        f"* As the model performance exceeded the minimum requirements set out for satisfying "
        f" Business Case 2, it was successful in answering the task it was intended to address. "
    )

    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write("* The first is responsible for feature engineering (no data cleaning was required).")
    st.write(edible_pipe_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(edible_pipe_model)

    st.write("---")
    st.write("* The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(edible_feat_importance)

    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=edible_pipe_model,
                    label_map=["poisonous", "edible"])
