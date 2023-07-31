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

    statement = (f"* Historically, **mushrooms in clusters 0, 2, 5 and 6 are usually edible**,"
                f" whereas **mushrooms in cluster 1 are always edible**, and **mushrooms in clusters"
                f" 3 and 4 are almost always poisonous**.")
    st.success(statement)


    statement = cluster_statement(cluster_prediction[0])
    st.info(statement)

    # cluster_profile.index = [" "] * len(cluster_profile)
    st.table(cluster_profile)

def cluster_statement(cluster_num):
    """ Takes predicted cluster and returns some general facts about the cluster from the analysis in the cluster mushroom workbook """
    if cluster_num == 0:
        statement = (f"**Mushrooms in cluster 0:**\n"
                    f"* are either in populations of several or solitary.\n"
                    f"* typically have broad gill sizes\n"
                    f"* typically have a bulbous stalk root\n"
                    f"* typically have close gill spacing\n"
                    f"* tend to have a stalk color below the ring of white, but can also have gray, or pink.\n"
                    f"* have pendant stalk ring(s).\n"
                    f"* are usually found in the woods, occasionally in urban or grass habitats.\n"
                    f"* **are usually edible (86% of cluster), but may occasionally be poisonous (14% of cluster)**.")
    elif cluster_num == 1:
        statement = (f"**Mushrooms in cluster 1:**\n"
                    f"* are either in populations of clustered or several.\n"
                    f"* have broad gill sizes.\n"
                    f"* have missing stalk roots.\n"
                    f"* have close gill spacing.\n"
                    f"* have a orange stalk color below the ring.\n"
                    f"* have pendant stalk ring(s).\n"
                    f"* are found in leaves habitats.\n"
                    f"* **are always edible (100% of cluster)**.")
    elif cluster_num == 2:
        statement = (f"**Mushrooms in cluster 2:**\n"
                    f"* tend to be in populations of scattered, but are also observed in numerous and several.\n"
                    f"* usually have broad gill sizes, but may be narrow.\n"
                    f"* tend to have a club stalk root, but also may be equal, or rooted.\n"
                    f"* have a close gill spacing.\n"
                    f"* have a white stalk color below the ring.\n"
                    f"* have pendant stalk ring(s).\n"
                    f"* tend to be found in grasses habitat, but may also be found in meadows, or urban.\n"
                    f"* **are usually edible (74%), but may be poisonous (26% of cluster)**.")
    elif cluster_num == 3:
        statement = (f"**Mushrooms in cluster 3:**\n"
                    f"* are either in populations of several or solitary.\n"
                    f"* typically have broad gill sizes.\n"
                    f"* typically have a bulbous stalk root.\n"
                    f"* have a close gill spacing.\n"
                    f"* either have brown, buff, or pink stalk color below the ring.\n"
                    f"* typically have a large stalk ring.\n"
                    f"* are either found in woods, paths, or grasses habitats.\n"
                    f"* **are almost always poisonous (99% of cluster)**.")
    elif cluster_num == 4:
        statement = (f"**Mushrooms in cluster 4:**\n"
                    f"* are typically in populations of several.\n"
                    f"* have narrow gill sizes.\n"
                    f"* typically have a missing stalk root.\n"
                    f"* typically have a close gill spacing.\n"
                    f"* either have a white or pink stalk color below the stalk ring.\n"
                    f"* typically have an evanescent stalk ring.\n"
                    f"* are either found in woods, leaves, or paths habitats.\n"
                    f"* **are almost always poisonous (98% of cluster)**.")
    elif cluster_num == 5:
        statement = (f"**Mushrooms in cluster 5:**\n"
                    f"* tend to be found in populations of either clustered, numerous, or scattered.\n"
                    f"* have broad gill sizes.\n"
                    f"* usually have a missing stalk root, but may also have a bulbous stalk root.\n"
                    f"* either have close or crowded gill spacing.\n"
                    f"* usually have a white stalk color below the stalk ring, but may be red.\n"
                    f"* mostly have a pendant stalk ring(s), but may have an evanescent.\n"
                    f"* **are usually edible (88% of cluster), but may occasionally be poisonous (12% of cluster)**.")
    else:
        statement = (f"**Mushrooms in cluster 6:**\n"
                    f"* are usually found in either populations of scattered or abundant, but may be found in several.\n"
                    f"* usually have broad gill sizes, but may have narrow.\n"
                    f"* usually have an equal stalk root, but may have bulbous.\n"
                    f"* most usually have crowded gill spacings, but may have close.\n"
                    f"* typically have white a white stalk color below the stalk ring.\n"
                    f"* usually have evanescent stalk ring(s), but may have pendant.\n"
                    f"* are usually found in grasses habitat, but may be found in woods or leaves.\n"
                    f"* **are usually edible (89% of cluster), but may occasionally be poisonous (11% of cluster)**.")

    return statement