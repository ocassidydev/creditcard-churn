import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_mushroom_data
import streamlit as st
import numpy as np
import plotly.express as px

sns.set_style("whitegrid")

def page_mushroom_edibility_study_body():
    """ Page for displaying the mushroom edibility study findings"""
    df = load_mushroom_data()

    vars_to_study = ['gill-color',
                     'odor',
                     'ring-type',
                     'spore-print-color',
                     'stalk-surface-above-ring']

    st.write("### Mushroom Edibility Study")
    st.success(f"* The client would like to better understand the patterns in the mushroom database so that the "
            f"client can learn the variable categories of a mushroom most likely to be edible. This will help "
            f"their picking team know what mushroom characteristics to look for and focus on picking.")
    st.info(f"* Performing this analysis answers Business Requirement 1 by revealing patterns in the dataset "
            f"that indicate which mushroom categories are the strongest indicators of edibility.")

    if st.checkbox("Inspect Mushroom Population"):
        st.write(f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
                f"below are the first 10 rows.")
        st.write(df.head(10))

    st.write("---")

    st.write(f"* A correlation study was conducted in the Mushroom Edibility Study notebook to gain insight into how "
            f"mushroom variables are correlated to levels of edibility. \n"
            f"The most correlated variables are: **{vars_to_study}**")

    st.info(
        f"The correlation coefficients and the interpretations of the plots below converge. "
        f"It is indicated that: \n"
        f"* Mushrooms with **`buff`** for **`gill-color`** are most liable to be poisonous.\n"
        f"* Mushrooms with **`foul`** for **`odor`** are most liable to be poisonous.\n"
        f"* Mushrooms with **`pendant`** for **`ring-type`** have the best chance of being edible.\n"
        f"* Mushrooms with **`buff`** for **`spore-print-color`** have the best chance of being edible.\n"
        f"* Mushrooms with **`silky`** for **`stalk-surface-above-ring`** are most liable to be poisonous.\n")

    df_eda = df.filter(vars_to_study + ['edible'])

    if st.checkbox("Edibility levels per variable"):
        st.success(f"These plots display the frequency of edible (**`edible=1`**) and poisonous (**`edible=0`**) "
                    f"mushrooms for categories of the 5 variables found to be most correlated to a mushrooms edibiility.")
        edible_level_per_variable(df_eda)

    if st.checkbox("Parallel Plot"):
        st.success(f"This plot shows the connections between mushroom categories for the variables found to be most correlated to a mushrooms edibiility.\n"
                f"* Information in yellow indicates the profile of an edible mushroom.")
        parallel_plot_edible(df_eda)


def edible_level_per_variable(df_eda):
    """ Calls plot_categorical for each column in the dataset """
    target_var = 'edible'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        plot_categorical(df_eda, col, target_var)

def plot_categorical(df, col, target_var):
    """ Plots distribution of categorical variables with respect to a target variable """
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var, order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)

def parallel_plot_edible(df_eda):
    """ Plots parallel plot of selected variables in dataset with respect to edibility """
    fig = px.parallel_categories(df_eda, color="edible", width=750, height=500)
    st.plotly_chart(fig)
