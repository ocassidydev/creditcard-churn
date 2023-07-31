import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_classify_mushroom_body():
    """ 
        Page for displaying the information about the Mushroom Classify pipeline's training and model performance 
    """
    version = 'v1'

    classify_pipe = load_pkl_file(f"outputs/ml_pipeline/cluster_analysis/{version}/classify_pipeline.pkl")
    classify_feat_importance = plt.imread(f"outputs/ml_pipeline/cluster_analysis/{version}/features_define_cluster.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/X_train_clf.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/X_test_clf.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/y_train_clf.csv").values
    y_test = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/y_test_clf.csv").values
    classify_features = X_train.columns.to_list()

    st.write("### ML Pipeline: Classify Mushroom Cluster")
    st.info(
        f"* The pipeline was tuned aiming at least 1.00 precision on 'classify', "
        f"* The pipeline performance on train and test set was a precision=1.00 recall=1.00, "
        f"and precision=1.00 recall=1.00, respectively.\n"
        f"* As the model performance exceeded the minimum requirements set out for satisfying "
        f" Business Case 2, it was successful in answering the task it was intended to address. "
    )

    st.write("---")
    st.write("#### Classify ML Pipeline Steps")
    st.write(classify_pipe)

    st.write("---")
    st.write("* The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(classify_feat_importance)

    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=classify_pipe,
                    label_map=["Cluster 0", "Cluster 1", "Cluster 2", "Cluster 3",
                            "Cluster 4", "Cluster 5", "Cluster 6"])