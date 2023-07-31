import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from src.data_management import load_mushroom_data, load_pkl_file


def page_cluster_mushroom_body():
    """
    Loads the Cluster Mushroom pipeline and displays its silhouette score
    Taken from Walkthrough Project 02 - Churnometer
    """

    version = 'v1'
    cluster_pipe = load_pkl_file(f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_silhouette = plt.imread(f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_silhouette.png")
    features_to_cluster = plt.imread(f"outputs/ml_pipeline/cluster_analysis/{version}/features_define_cluster.png")
    cluster_profile = pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv").columns.to_list())

    df_edible_vs_clusters = load_mushroom_data().filter(['edible'], axis=1)
    df_edible_vs_clusters['Clusters'] = cluster_pipe['model'].labels_

    st.write("### ML Pipeline: Cluster Analysis")
    st.info(f"* We fitted this cluster pipeline onto the dataset with all variables, including edibility.\n"
            f"* The pipeline average silhouette score is 0.52. This exceeded the mininum requirements for "
            f"satisfying Business Requirement 3 and was hence successful in answering the task it was intended to address.")
    st.write("---")

    st.write("#### Cluster ML Pipeline steps")
    st.write(cluster_pipe)

    st.write("#### The features the model was trained with")
    st.write(cluster_features)

    st.write("#### Clusters Silhouette Plot")
    st.image(cluster_silhouette)

    cluster_distribution_per_variable(df=df_edible_vs_clusters, target='edible')

    st.write("#### Most important features to define a cluster")
    st.image(features_to_cluster)

    st.write("#### Cluster Profile")
    statement = (f"* Historically, **mushrooms in clusters 0, 2, 5 and 6 are usually edible**, "
                f"whereas **mushrooms in cluster 1 are always edible**, and **mushrooms in clusters"
                f" 3 and 4 mushrooms are almost always poisonous**.\n"
                f"* From the Predict Edible model, we noticed that included in the predictors of "
                f"edibility was gill-size, which was also among the predictors for the mushrooms' "
                f"clusters. A potential action for the picking team would be to discard and avoid any mushrooms with "
                f"narrow gill sizes, as from analysing the cluster profiles it is likely such mushrooms belong "
                f"to cluster 4 which is nearly entirely poisonous.\n")
    st.info(statement)

    statement = (
                f"**Mushrooms in cluster 0:**\n"
                f"* are either in populations of several or solitary.\n"
                f"* typically have broad gill sizes.\n"
                f"* typically have a bulbous stalk root.\n"
                f"* typically have close gill spacing.\n"
                f"* tend to have a stalk color below the ring of white, but can also have gray, or pink.\n"
                f"* have pendant stalk ring(s).\n"
                f"* are usually found in the woods, occasionally in urban or grass habitats.\n"
                f"* **are usually edible (86% of cluster), but may occasionally be poisonous (14% of cluster)**.\n\n"
                f"**Mushrooms in cluster 1:**\n"
                f"* are either in populations of clustered or several.\n"
                f"* have broad gill sizes.\n"
                f"* have missing stalk roots.\n"
                f"* have close gill spacing.\n"
                f"* have a orange stalk color below the ring.\n"
                f"* have pendant stalk ring(s).\n"
                f"* are found in leaves habitats.\n"
                f"* **are always edible (100% of cluster)**.\n\n"
                f"**Mushrooms in cluster 2:**\n"
                f"* tend to be in populations of scattered, but are also observed in numerous and several.\n"
                f"* usually have broad gill sizes, but may be narrow.\n"
                f"* tend to have a club stalk root, but also may be equal, or rooted.\n"
                f"* have a close gill spacing.\n"
                f"* have a white stalk color below the ring.\n"
                f"* have pendant stalk ring(s).\n"
                f"* tend to be found in grasses habitat, but may also be found in meadows, or urban.\n"
                f"* **are usually edible (74%), but may be poisonous (26% of cluster)**.\n\n"
                f"**Mushrooms in cluster 3:**\n"
                f"* are either in populations of several or solitary.\n"
                f"* typically have broad gill sizes.\n"
                f"* typically have a bulbous stalk root.\n"
                f"* have close gill-spacing.\n"
                f"* either have brown, buff, or pink stalk color below the ring.\n"
                f"* typically have a large stalk ring.\n"
                f"* are either found in woods, paths, or grasses habitats.\n"
                f"* **are almost always poisonous (99% of cluster)**.\n\n"
                f"**Mushrooms in cluster 4:**\n"
                f"* are typically in populations of several.\n"
                f"* have narrow gill sizes.\n"
                f"* typically have a missing stalk root.\n"
                f"* typically have a close gill spacing.\n"
                f"* either have a white or pink stalk color below the stalk ring.\n"
                f"* typically have an evanescent stalk ring.\n"
                f"* are either found in woods, leaves, or paths habitats.\n"
                f"* **are almost always poisonous (98% of cluster)**.\n\n"
                f"**Mushrooms in cluster 5:**\n"
                f"* tend to be found in populations of either clustered, numerous, or scattered.\n"
                f"* have broad gill sizes.\n"
                f"* usually have a missing stalk root, but may also have a bulbous stalk root.\n"
                f"* either have close or crowded gill spacing.\n"
                f"* usually have a white stalk color below the stalk ring, but may be red.\n"
                f"* mostly have a pendant stalk ring(s), but may have an evanescent.\n"
                f"* **are usually edible (88% of cluster), but may occasionally be poisonous (12% of cluster)**.\n\n"
                f"**Mushrooms in cluster 6:**\n"
                f"* are usually found in either populations of scattered or abundant, but may be found in several.\n"
                f"* usually have broad gill sizes, but may have narrow.\n"
                f"* usually have an equal stalk root, but may have bulbous.\n"
                f"* most usually have crowded gill spacings, but may have close.\n"
                f"* typically have white a white stalk color below the stalk ring.\n"
                f"* usually have evanescent stalk ring(s), but may have pendant.\n"
                f"* are usually found in grasses habitat, but may be found in woods or leaves.\n"
                f"* **are usually edible (89% of cluster), but may occasionally be poisonous (11% of cluster)**.\n"
    )
    st.success(statement)

    cluster_profile.index = [" "] * len(cluster_profile)
    st.table(cluster_profile)

def cluster_distribution_per_variable(df, target):
    """ 
    Displays the distribution of the target (edibility) among each of the clusters 
    Taken from Walkthrough Project 02 - Churnometer
    """
    df_bar_plot = df.value_counts(["Clusters", target]).reset_index()
    df_bar_plot.columns = ['Clusters', target, 'Count']
    df_bar_plot[target] = df_bar_plot[target].astype('object')

    st.write(f"#### Clusters distribution across {target} levels")
    fig = px.bar(df_bar_plot, x='Clusters', y='Count',
                 color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    st.plotly_chart(fig)

    df_relative = (df
                   .groupby(["Clusters", target])
                   .size()
                   .groupby(level=0)
                   .apply(lambda x:  100*x / x.sum())
                   .reset_index()
                   .sort_values(by=['Clusters'])
                   )
    df_relative.columns = ['Clusters', target, 'Relative Percentage (%)']

    st.write(f"#### Relative Percentage (%) of {target} in each cluster")
    fig = px.line(df_relative, x='Clusters', y='Relative Percentage (%)',
                  color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    fig.update_traces(mode='markers+lines')
    st.plotly_chart(fig)
