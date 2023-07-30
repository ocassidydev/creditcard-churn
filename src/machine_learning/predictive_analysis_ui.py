import streamlit as st


def predict_edible(X_live, edible_pipeline_fe, edible_pipeline_model):
    """ 
    applies the clf pipeline to live data supplied by the user through the widget
    displays the clf model's output in an interpretable way
    """
    X_live_edible = X_live.copy()
    X_live_edible_fe = edible_pipeline_fe.transform(X_live_edible)

    edible_prediction = edible_pipeline_model.predict(X_live_edible_fe)
    edible_prediction_proba = edible_pipeline_model.predict_proba(X_live_edible_fe)

    edible_prob = edible_prediction_proba[0, edible_prediction][0]*100
    if edible_prediction == 1:
        edible_result = 'edible'
    else:
        edible_result = 'poisonous'

    statement = (f'### There is {edible_prob.round(1)}% probability '
                f'that this mushroom is **{edible_result}**.')

    st.write(statement)

def predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile):
    """
    Applies the clustering pipeline to live data supplied by the user through the widget
    displays the cluster model's output with the proportion of mushrooms in that cluster that are edible/poisonous
    """
    X_live_cluster = X_live.filter(cluster_features)

    cluster_prediction = cluster_pipeline.predict(X_live_cluster)

    statement = (f"### The mushroom is expected to belong to **cluster {cluster_prediction[0]}**")
    st.write("---")
    st.write(statement)

    statement = (
        f"* Test"
    )
    st.info(statement)

    statement = (
        f"* Test"
    )
    st.success(statement)

    cluster_profile.index = [" "] * len(cluster_profile)
    st.table(cluster_profile)
