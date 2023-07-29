# **Mushroom Safety**
![Mushroom Image](https://i.pinimg.com/originals/83/1d/42/831d42fa56e68793b9cf4949d596c120.png)

## Summary

<a href="https://mushroom-safety-a3c88f9ac249.herokuapp.com/">mushroom-safety</a> is a dashboard application that enables an wild mushroom harvesting business to analyse various properties of mushrooms to determine whether they are edible or poisonous. The project was agreed to achieve the following objectives for the company:

- gives the company visual insight into what aspects of mushrooms generally indicate if they are likely to be edible
- allows the company to determine the probability a mushroom will be edible or not based on information that gan be gathered from visually categorizing the mushroom
- allows the company to group similar mushroom types together

## Dataset Content

The dataset was sourced from the <a href="https://www.kaggle.com/datasets/uciml/mushroom-classification" target="_blank" rel="noreferrer">Mushroom Classification dataset</a> on <a href="https://www.kaggle.com" target="_blank" rel="noreferrer">kaggle</a>. Each row represents a mushroom, with each column representing physical attributes of the mushrooms, which include:

- The appearance of the <a href="https://en.wikipedia.org/wiki/Pileus_(mycology)">cap</a>, the structure that forms the head of the mushrooma
- The bruising on the mushroom
- The mushroom's odor
- The appearance of the mushroom's <a href="https://en.wikipedia.org/wiki/Lamella_(mycology)">gills</a>, the structures that hang vertically under the cap
- The appearance of the mushroom's <a href="https://en.wikipedia.org/wiki/Stipe_(mycology)">stipe</a>, aka the stalk
- The appearance of the mushroom's <a href="https://en.wikipedia.org/wiki/Veil_(mycology)">veil</a>, the membrane that covers the cap and the stalk
- The appearance of the mushroom's <a href="https://en.wikipedia.org/wiki/Annulus_(mycology)">annulus</a>, the ring(s) that are seen on the stalk
- The mushrooms's <a href="https://en.wikipedia.org/wiki/Spore_print">spore print</a> color
- The mushroom's population, ie. how many of the same type were found in the area
- The habitat the mushroom was found in.

| Variable                    | Meaning                                                                                     | Units                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| class                   | Whether the mushroom is edible or poisonous                       | Character: 'e' - edible, 'p' - poisonous                                    |
| cap-shape | The shape of the mushroom's cap | Character: 'b' - bell, 'c' - conical, 'x' - convex, 'f' - flat, 'k' - knobbed, 's' - sunken |
| cap-surface | The consistency of the mushroom's cap surface | Character: 'f' - fibrous, 'g' - grooves, 'y' - scaly, 's' - smooth |
| cap-color | The color of the mushroom's cap | Character: 'n' - brown, 'b' - buff, 'c' - cinnamon, 'g' - gray, 'r' - green, 'p' - pink, 'u' - purple, 'e' - red, 'w' - white, 'y' - yellow |
| bruises | Whether the mushroom has bruises or not | Character: 't' - bruises, 'f' - no |
| odor | The mushroom's smell | Character: 'a' - almond, 'l' - anise, 'c' - creosote, 'y' - fishy, 'f' - foul, 'm' - musty, 'n' - none, 'p' - pungent, 's' - spicy |
| gill-attachment | How the mushroom's gills are attached to the stalk | Character: 'a' - attached, 'd' - descending, 'f' - free, 'n' - notched |
| gill-spacing | How the mushroom's gills are spaced out | Character: 'c' - close, 'w' - crowded, 'd' - distant |
| gill-size | The size of the mushroom's gills | Character: 'b' - broad, 'n' - narrow |
| gill-color | The color of the mushroom's gills | Character: 'k' - black, 'n' - brown, 'b' - buff, 'h' - chocolate, 'g' - gray, 'r' - green, 'o' - orange, 'p' - pink, 'u' - purple, 'e' - red, 'w' - white, 'y' - yellow |
| stalk-shape | The shape of the mushroom's stalk | Character: 'e' - enlarging, 't' - tapering |
| stalk-root | The shape of the stalk's root | Character: 'b' - bulbous, 'c' - club, 'u' - cup, 'e' - equal, 'z' - rhizomorphs, 'r' - rooted, '?' - missing |
| stalk-surface-above-ring | The consistency of the mushroom's stalk surface above the ring(s) | Character: 'f' - fibrous, 'y' - scaly, 'k' - silky, 's' - smooth |
| stalk-surface-below-ring | The consistency of the mushroom's stalk surface below the ring(s) | Character: 'f' - fibrous, 'y' - scaly, 'k' - silky, 's' - smooth |
| stalk-color-above-ring | The color of the mushroom's stalk above the ring(s) | Character: 'n' - brown, 'b' - buff, 'c' - cinnamon, 'g' - gray, 'o' - orange, 'p' - pink, 'e' - red, 'w' - white, 'y' - yellow |
| stalk-color-below-ring | The color of the mushroom's stalk below the ring(s) | Character: 'n' - brown, 'b' - buff, 'c' - cinnamon, 'g' - gray, 'o' - orange, 'p' - pink, 'e' - red, 'w' - white, 'y' - yellow |
| veil-type | The type of veil that the mushroom has covering the cap and stalk | Character: 'p' - partial, 'u' - universal |
| veil-color | The color of the mushroom's veil | Character: 'n' - brown, 'o' - orange, 'w' - white, 'y' - yellow |
| ring-number | The number of rings (annuli) on the mushroom's stalk | Character: 'n' - none, 'o' - one, 't' - two |
| ring-type | The type of ring (annulus) on mushroom's stalk| Character: 'c' - cobwebby, 'e' - evanescent, 'f' - flaring, 'l' - large, 'n' - none, 'p' - pendant, 's' - sheathing, 'z' - zone |
| spore-print-color | The color of the mushroom's spore print | Character: 'k' - black, 'n' - brown, 'b' - buff, 'h' - chocolate, 'r' - green, 'o' - orange, 'u' - purple, 'w' - white, 'y' - yellow |
| population | The number of mushroom's of the same type in the location it was found | Character: 'a' - abundant, 'c' - clustered, 'n' - numerous, 's' - scattered, 'v' - several, 'y' - solitary |
| habitat | The habitat the mushroom was found in | Character: 'g' - grasses, 'l' - leaves, 'm' - meadows, 'p' - paths, 'u' - urban, 'w' - waste, 'd' - woods |

- **Project Terms & Jargon**
  - A mushroom describes any which has been picked by the company and physically classified using the above table of variables
  - Edibility describes whether a mushroom is edible or not

## Business Requirements

A fictitious client for this project is a highly data-driven artisanal wild mushroom harvesting business that is seeking a reliable means to classify whether the Agaricus and Lepiota mushrooms they pick are edible or poisonous. They want to avoid selling toxic mushrooms to their customers, but also wish to avoid paying for costly toxicity screening or hiring expert mycologists to correctly identify mushrooms, and would prefer a cheap and reliable model to determine whether mushrooms are safe to eat. When a mushroom is picked, the picker will classify the mushroom based on it's physical characteristics, using set categories provided by the client. This information is logged, and then the mushroom is tested on cell cultures to determine if it is poisonous or not. 

The client has shared a mushroom database containing information pertaining to the physical characteristics of the mushrooms and whether they were classed as edible or poisonous.

- **1** The client would like to better understand the patterns in the mushroom database so that the client can learn the variables of a mushroom most likely to be edible. This will help their picking team know what characteristics to look for and focus on picking.

- **2** The client would like to determine whether a given mushroom is edible. It is essential that any means of doing this has a false positive rate of zero, as the client does not want to inadvertently sell poisonous mushrooms mistakenly identified as edible.

- **3** The client has informed us that there are 23 distinct species of mushroom in the dataset. They want to investigate if these 23 species can be identified from the variables supplied by cluster analysis, and the rates of edibility among each identified cluster. 

## Hypothesis and how to validate?

- 1 - It's suspected that poisonous mushrooms typically have a foul odor.
  - Viewing the average rate of edibility among mushrooms with a foul odor compared to those with other odors, combined with a correlation study on odor to determine if odor is a predictor of edibility may be used to investigate this.
- 2 - It's suspected that poisonous mushrooms typically have a brown gill color.
  - Viewing the average rate of edibility among mushrooms with a brown gill color compared to those with other gill colors, combined with a correlation study on gill color to determine if gill color is a predictor of edibility may be used to investigate this.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1:** Data visualization and correlation study

  - We will inspect the data related to the logged mushrooms.
  - We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to edibility.
  - We will plot the main variables that correlate to edibility to visualize insights.

- **Business Requirement 2:** Classification analysis

  - We want to predict if a given mushroom will be edible or poisonous. We will build a binary classifier.

- **Business Requirement 3:** Cluster analysis

  - We want to investigate if there distinct groups of similar mushrooms by unsupervised learning. We are told b
  - When these distinct groups are identified, we want to build a classifier that can identify which group a mushroom belongs to.
  - We then wish to investigate if the rates of edibility among clusters of similar mushrooms.

## ML Business Case

### Predict Edible

#### Classification Model

- We want an ML model to predict if a mushroom is edible based on historical data from the mushrooms the client has logged. The target variable is categorical and contains 2 classes. We consider a **classification model**. It is a supervised, 2-class, single label, classification model with outputs of 0 (poisonous) or 1 (edible).
- The ideal outcome is to provide the picking team with reliable insight into the best profile of an edible mushroom for focusing on picking.
- The model success metrics: 
  - at least a precision of 1 for ediblility, on train and test set - no false positives
  - at least a recall of 0.9 for edibility, on train and test set - minimum false negatives
  - The ML model is considered a failure if:
    - after 3 months of test usage, any newly picked mushrooms identified as edible come up as poisonous in a toxicity screen (even if model performs perfectly on the provided mushroom data, this will indicate what it has learned is not generalizable to a wider population of mushrooms)
    - after 3 months of test usage, more than 20% of newly picked mushrooms identified as poisonous come up as edible in a toxicity screen (don't want a model that discards too many perfectly edible mushrooms for no reason)
  - The model output is defined as a flag, indicating if a mushroom will be edible or poisonous and the probability they are edible. The picking team will have the dashboard available via their smartphones' web browser, enabling them to enter mushroom information in the field as they are collected. The prediction is made on the fly (not for batches).
  - Heuristics: There are no obvious heuristics for performing this task.
  - The training data to fit the model comes from the mushroom picking company. This dataset contains approximately 8000 logged mushrooms.
    - Train data - target: `class`; features: `cap-shape`, `cap-surface`, `cap-color`, `bruises`, `odor`, `gill-attachment`, `gill-spacing`, `gill-size`, `gill-color`, `stalk-shape`, `stalk-root`, `stalk-surface-above-ring`, `stalk-surface-below-ring`, `stalk-color-above-ring`, `stalk-color-below-ring`, `veil-type`, `veil-color`, `ring-number`, `ring-type`, `spore-print-color`, `population`, `habitat`

### Cluster Mushroom

#### Clustering Model

- We want an ML model to identify the various clusters that exist in the data to see if these correspond to the 23 species the client has claimed is in the dataset. We consider a **clustering model**, which is unsupervised. 
- The ideal outcome is to provide the client with reliable insight into whether the variables their pickers are collecting can identify the mushroom's species.
- The model success metrics:
  - An average silhouette score of at least 0.6 among all clusters
  - The ML model is considered a failure if:
    - 23 distinct species are not successfully identified.
  - The output is defined as a flag, indicating which unlabeled cluster a mushroom belongs to. The picking team will have the dashboard available via their smartphone web browser, enabling them to enter mushroom information in the field as they are collected. The prediction is made on the fly (not for batches).
  - The training data to fit the model comes from the mushroom picking company. This dataset contains approximately 8000 logged mushrooms.
    - Train data - features: `cap-shape`, `cap-surface`, `cap-color`, `bruises`, `odor`, `gill-attachment`, `gill-spacing`, `gill-size`, `gill-color`, `stalk-shape`, `stalk-root`, `stalk-surface-above-ring`, `stalk-surface-below-ring`, `stalk-color-above-ring`, `stalk-color-below-ring`, `veil-type`, `veil-color`, `ring-number`, `ring-type`, `spore-print-color`, `population`, `habitat`

### Classify Mushroom

#### Classification Model

- We want an ML model to predict the cluster a mushroom belongs to. The target variable is categorical and will contain the number of classes determined as suitable from Cluster Mushroom. We consider a **classification model**. It is a supervised, multi-class, single label, classification model, with integer outputs corresponding to each unlabeled cluster.
- The ideal outcome is to provide the picking team with a reliable method of identifying which clusters the mushrooms they pick belong to.
- The model success metrics:
  - An average recall of 0.7 among all clusters
  - The ML model is considered a failure if:
    - After 3 months of test usage, the model incorrectly assigns species labels to mushrooms more than 40% of the time.
  - The output is defined as a flag, indicating which unlabeled cluster a mushroom belongs to. The picking team will have the dashboard available via their smartphone web browser, enabling them to enter mushroom information in the field as they are collected. The prediction is made on the fly (not for batches).
  - The training data to fit the model comes from the mushroom picking company. This dataset contains approximately 8000 logged mushrooms.
    - Train data - target: `mushroom-cluster`(from Cluster Mushroom) features: `cap-shape`, `cap-surface`, `cap-color`, `bruises`, `odor`, `gill-attachment`, `gill-spacing`, `gill-size`, `gill-color`, `stalk-shape`, `stalk-root`, `stalk-surface-above-ring`, `stalk-surface-below-ring`, `stalk-color-above-ring`, `stalk-color-below-ring`, `veil-type`, `veil-color`, `ring-number`, `ring-type`, `spore-print-color`, `population`, `habitat`

## Dashboard Design

### Page 1: Quick project summary

- Quick summary of the project
  - Project terminology
  - Description of the dataset
  - Business requirements, with some greater context the user can expand on

### Page 2: Mushroom Edibility Study

- Need this page to answer business requirment 1. Will need to display plots that correlate mushroom variables to edibility
- Agreed with stakeholders that this page will:
  - State business requirement 1
  - Checkbox: data inspection (displays the number of rows and columns in dataset, as well as first ten rows of data)
  - Displays most correlated mushroom variables to edibility with conclusions of study
  - Checkbox: Individual plots displaying edibility rates for each variable most correlated to edibility
  - Checkbox: Parallel plots mapping correlated variables to edibility for full visualization of how mushroom population breaks down

### Page 3: Mushroom Classifier

- State business requirements 2 and 3
- Set of input widgets for setting the variables of the picked mushrooms. The inputs are related to ML pipelines that will predict edibility and the cluster the mushroom belongs to.
- "Run prediction" button that feeds the mushroom's data into the ML pipelines. These will predict the probability of whether the mushroom will be edible or poisonous, and which cluster of similar mushrooms they belong to, and whether this cluster tends to have poisonous or edible mushrooms, and at what rate.

### Page 4: Project Hypotheses and Validation

- We have two hypotheses regarding this dataset, which we will state and then display the results of testing them.

* 1 - It's suspected that poisonous mushrooms have a foul odor.
* 2 - It's suspected that poisonous mushrooms have a brown spore print color.

### Page 5: ML: Mushroom Edibility

- Considerations and conclusions after pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline importance

### Page 6: ML: Mushroom Cluster Analysis

- Considerations and conclusions after pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline importance

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: https://mushroom-safety-a3c88f9ac249.herokuapp.com/
- 
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, selected GitHub as the deployment method.
3. Selected "mushroom-safety" and click Search. Once it was found, clicked Connect.
4. In the heroku CLI, ran `heroku stack:set heroku-20 -a mushroom-safety` to set the stack to heroku-20
4. Selected the main branch to deploy, then clicked Deploy Branch.
5. Clicked the button Open App on the top of the page to access App.

## Main Data Analysis and Machine Learning Libraries

- The libraries used in this project:

	-`numpy` - for general usage on array-based data structures.
	-`pandas` - for creating DataFrames to store the dataset in and operating various data cleaning, feature engineering, modelling and model assessment tasks.
	-`matplotlib` - for plotting data to visualize insights
	-`seaborn` - for plotting data to visualize insights
	-`ydata-profiling` - for using the `ProfileReport` class to assess the datasets composition
	-`plotly` - for formatting matplotlib and seaborn plots
	-`ppscore` - for generating correlation coefficients of different variables in the dataset to the target
	-`streamlit` - for implementing the dashboard application
	-`feature-engine` - for various feature engineering tasks
	-`imbalanced-learn` - for performing SMOTE on the training data to ensure a balanced proportion of targets
	-`scikit-learn` - for implementing ML models
	-`xgboost` - for implementing ML models
	-`yellowbrick` - for assessing model perfomance
	-`category_encoders` - for using the `TargetEncoder` class to perform target encoding on the dataset

## Credits

### Content

- 

### Media

- 

## Acknowledgements

- Thank the people that provided support through this project.
