import streamlit as st

def page_project_hypothesis_body():
    """
    Page for displaying project hypothesis and validation
    """
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"** We suspect a mushroom with no odor is typically edible: Correct.**\n"
        f"* A mushroom having no odor is strongly correlated to edibility, with the flag **`odor_none`** " 
        f"having Spearman correlation coefficient of 0.79 and Pearson coefficient of 0.79 to the "
        f"**`edible`** flag.\n* It was also found that 96.6% of all mushrooms in the dataset with no odor " 
        f"are edible.\n* Hence, it can be said mushrooms lacking an odor can be said to be typically edible.\n\n"
        f"** We suspect a mushroom with a silky consistency to the surface of its stalk above the stalk ring is typically poisonous: Correct.**\n"
        f"* A mushroom having a silky consistency above the ring is negatively correlated to a mushroom being edible, with the flag "
        f"**`stalk-surface-above-ring_silky`** having a Spearman correlation coefficient of -0.59 and Pearson correlation coefficient of -0.59 to " 
        f"the **`edible`** flag.\n* It was also found only 6.06% of mushrooms with a silky stalk surface above the stalk ring are edible.\n"
        f"* Hence mushrooms with a silky consistency on the stalk above the ring can be said to be typically poisonous."
    )
