import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():
    """
    Page for displaying the summary of the project.
    """
    st.write("### Project Summary")

    st.write("mushroom-safety is a dashboard application that enables an wild mushroom harvesting business "
            "to analyse various properties of mushrooms to determine whether they are edible or poisonous.")

    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A mushroom describes any which has been picked by the company and physically classified using a set of categorical variables\n"
        f"* Edibility describes whether a mushroom is edible or not, ie. if it is not poisonous\n"
        f"* A variable is any individual column in the dataset that describes a mushroom, e.g. **`odor`**\n"
        f"* A category is any possible value of each variable for a mushroom, e.g. **`odor=none`**")

    st.write(
        f"* For additional information, please visit and read the "
        f"[Project README file](https://github.com/ocassidydev/mushroom-safety).")

    st.success(
        f"The project has 3 business requirements:\n"
        f"* 1 - The client would like to better understand the patterns in the mushroom database so that they can learn the variable categories "
        f"of a mushroom most likely to be edible. This will help their picking team know what mushroom characteristics to look for and focus on picking.\n"
        f"* 2 - The client would like to determine whether a given mushroom is edible. It is essential that any means of doing this has a false "
        f" positive rate of zero, as the client does not want to inadvertently sell poisonous mushrooms mistakenly identified as edible.\n"
        f"* 3 - The client has informed us that there are a number of distinct species of mushroom in the dataset. They want to investigate "
        f"if this can be identified by grouping mushrooms with similar categories by means of a cluster algorithm, and to determine the rates "
        f"of edibility among each identified cluster. Ideally, this will provide the picking team with certain categorical heuristics for "
        f"selecting edible mushrooms."
        )

    mushroom_diagram = plt.imread(f"assets/mushroom-diagram.jpg")
    st.image(mushroom_diagram)