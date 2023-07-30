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
                f"whereas **mushrooms in cluster 1 are always edible**, and in **clusters"
                f" 3 and 4 mushrooms are almost always poisonous")
    st.success(statement)


    statement = cluster_statement(cluster_prediction[0])
    st.info(statement)

    cluster_profile.index = [" "] * len(cluster_profile)
    st.table(cluster_profile)

def cluster_statement(cluster_num):
    """ Takes predicted cluster and returns some general facts about the cluster from the analysis in the cluster mushroom workbook """
    if cluster_num == 0:
        statement = (f"- Mushrooms in cluster 0:"
                    f"\t- are either in populations of several or solitary"
                    f"\t- typically have broad gill sizes"
                    f"\t- typically have a bulbous stalk root"
                    f"\t- typically have close gill spacing"
                    f"\t- tend to have a stalk color below the ring of white, but can also have gray, or pink. "
                    f"\t- have pendant stalk ring(s)"
                    f"\t- are usually found in the woods, occasionally in urban or grass habitats."
                    f"\t- **are usually edible (86% of cluster), but may occasionally be poisonous (14% of cluster)**")
    elif cluster_num == 1:
        statement = (f"\t* Mushrooms in cluster 1:"
                    f"\t- are either in populations of clustered or several"
                    f"\t- have broad gill sizes"
                    f"\t- have missing stalk roots"
                    f"\t- have close gill spacing"
                    f"\t- have a orange stalk color below the ring"
                    f"\t- have pendant stalk ring(s)"
                    f"\t- are found in leaves habitats"
                    f"\t- **are always edible (100% of cluster)**")
    elif cluster_num == 2:
        statement = (f"\t- Mushrooms in cluster 2:"
                    f"\t- tend to be in populations of scattered, but are also observed in numerous and several"
                    f"\t- usually have broad gill sizes, but may be narrow"
                    f"\t- tend to have a club stalk root, but also may be equal, or rooted"
                    f"\t- have a close gill spacing"
                    f"\t- have a white stalk color below the ring"
                    f"\t- have pendant stalk ring(s) "
                    f"\t- tend to be found in grasses habitat, but may also be found in meadows, or urban"
                    f"\t- **are usually edible (74%), but may be poisonous (26% of cluster)**")
    elif cluster_num == 3:
        statement = (f"\t* Mushrooms in cluster 3:"
                    f"\t- are either in populations of several or solitary"
                    f"\t- typically have broad gill sizes"
                    f"\t- typically have a bulbous stalk root"
                    f"\t- have a close gill spacing"
                    f"\t- either have brown, buff, or pink stalk color below the ring"
                    f"\t- typically have a large stalk ring"
                    f"\t- are either found in woods, paths, or grasses habitats"
                    f"\t- **are almost always poisonous (99% of cluster)**")
    elif cluster_num == 4:
        statement = (f"\t- Mushrooms in cluster 4:"
                    f"\t- are typically in populations of several"
                    f"\t- have narrow gill sizes"
                    f"\t- typically have a missing stalk root"
                    f"\t- typically have a close gill spacing"
                    f"\t- either have a white or pink stalk color below the stalk ring"
                    f"\t- typically have an evanescent stalk ring"
                    f"\t- are either found in woods, leaves, or paths habitats "
                    f"\t- **are almost always poisonous (98% of cluster)**")
    elif cluster_num == 5:
        statement = (f"\t* Mushrooms in cluster 5:"
                    f"\t- tend to be found in populations of either clustered, numerous, or scattered"
                    f"\t- have broad gill sizes"
                    f"\t- usually have a missing stalk root, but may also have a bulbous stalk root"
                    f"\t- either have close or crowded gill spacing"
                    f"\t- usually have a white stalk color below the stalk ring, but may be red"
                    f"\t- mostly have a pendant stalk ring(s), but may have an evanescent"
                    f"\t- **are usually edible (88% of cluster), but may occasionally be poisonous (12% of cluster)**")
    else:
        statement = (f"\t- Mushrooms in cluster 6:"
                    f"\t- are usually found in either populations of scattered or abundant, but may be found in several"
                    f"\t- usually have broad gill sizes, but may have narrow"
                    f"\t- usually have an equal stalk root, but may have bulbous"
                    f"\t- most usually have crowded gill spacings, but may have close"
                    f"\t- typically have white a white stalk color below the stalk ring"
                    f"\t- usually have evanescent stalk ring(s), but may have pendant"
                    f"\t- are usually found in grasses habitat, but may be found in woods or leaves"
                    f"\t- **are usually edible (89% of cluster), but may occasionally be poisonous (11% of cluster)**")

    return statement