import streamlit as st


def predict_edible(X_live, edible_features, edible_pipeline_dc_fe, edible_pipeline_model):

    # from live data, subset features related to this pipeline
    X_live_edible = X_live.filter(edible_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_edible_dc_fe = edible_pipeline_dc_fe.transform(X_live_edible)

    # predict
    edible_prediction = edible_pipeline_model.predict(X_live_edible_dc_fe)
    edible_prediction_proba = edible_pipeline_model.predict_proba(
        X_live_edible_dc_fe)
    # st.write(edible_prediction_proba)

    # Create a logic to display the results
    edible_prob = edible_prediction_proba[0, edible_prediction][0]*100
    if edible_prediction == 1:
        edible_result = 'edible'
    else:
        edible_result = 'poisonous'

    statement = (
        f'### There is {edible_prob.round(1)}% probability '
        f'that this mushroom is **{edible_result}**.')

    st.write(statement)

    return edible_prediction


def predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile):

    # from live data, subset features related to this pipeline
    X_live_cluster = X_live.filter(cluster_features)

    # predict
    cluster_prediction = cluster_pipeline.predict(X_live_cluster)

    statement = (
        f"### The mushroom is expected to belong to **cluster {cluster_prediction[0]}**")
    st.write("---")
    st.write(statement)

    # text based on "07 - Modeling and Evaluation - Cluster Mushroom" notebook conclusions
    statement = (
        f"* Test"
    )
    st.info(statement)

    # text based on "07 - Modeling and Evaluation - Cluster Mushroom" notebook conclusions
    statement = (
        f"* Test"
    )
    st.success(statement)

    # hack to not display index in st.table() or st.write()
    cluster_profile.index = [" "] * len(cluster_profile)
    # display cluster profile in a table - it is better than in st.write()
    st.table(cluster_profile)
