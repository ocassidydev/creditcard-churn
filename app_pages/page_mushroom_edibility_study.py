import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_mushroom_data
import streamlit as st
import numpy as np
import plotly.express as px

sns.set_style("whitegrid")


def page_mushroom_edibility_study_body():

    # load data
    df = load_mushroom_data()

    # hard copied from mushroom edibility study notebook
    vars_to_study = ['gill-color',
                     'odor',
                     'ring-type',
                     'spore-print-color',
                     'stalk-surface-above-ring']

    st.write("### Mushroom Edibility Study")
    st.info(
        f"* Test")

    # inspect data
    if st.checkbox("Inspect Mushroom Population"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to levels of edible mushrooms. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "02 - Mushroom Edibility Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge."
    )

    # Code copied from "02 - Mushroom Edibility Study" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['class'])

    # Individual plots per variable
    if st.checkbox("Edibility Levels per Variable"):
        churn_level_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in yellow indicates the profile from an edible mushroom")
        parallel_plot_churn(df_eda)


# function created using "02 - Mushroom Edibility Study" notebook code - "Variables Distribution by Churn" section
def churn_level_per_variable(df_eda):
    target_var = 'class'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


# code copied from "02 - Mushroom Edibility Study" notebook - "Variables Distribution by Churn" section
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# code copied from "02 - Mushroom Edibility Study" notebook - "Variables Distribution by Churn" section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# function created using "02 - Mushroom Edibility Study" notebook code - Parallel Plot section
def parallel_plot_churn(df_eda):
    fig = px.parallel_categories(
        df_eda, color="class", width=750, height=500)
    # we use st.plotly_chart() to render, in notebook is fig.show()
    st.plotly_chart(fig)
