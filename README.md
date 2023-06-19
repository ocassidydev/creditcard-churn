![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Gitpod Template Instructions section of this README.md file, and modify the remaining paragraphs for your own project. Please do read the Gitpod Template Instructions at least once, though! It contains some important information about Gitpod and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.

## Gitpod Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

## Summary

creditcard-attritionscope is a dashboard application that enables a bank to analyse various aspects of prospective credit card customers (prospects) to determine if they will be retained as customers and how profitable they will be overall.

- gain visual insight into what aspects of prospect's demographics and their chosen product offerings influence their tendency to churn
- allows the company to determine the probability a prospect will churn or not based on information the prospect supplies
- allows the company to determine how long a churned prospect will remain with the company
- allows the company to predict a prospect's credit utilization ratio

## Dataset Content

The dataset was sourced from the <a href="https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers" target="_blank" rel="noreferrer">Credit Card customers dataset</a> on <a href="https://www.kaggle.com" target="_blank" rel="noreferrer">kaggle</a>. Each row represents a customer, with each column representing attributes regarding the customers, which include:

- Demographic data on the customer (age, sex, education status etc.)
- Type of credit card product the customer uses (blue or silver, credit limit)
- The customers card usage data (Balance on the credit card, change in transactions between previous quarters, credit utilization etc.)
- Whether the customer has "attritioned" - if they have closed their account.

| Variable                    | Meaning                                                                                     | Units                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| CLIENTNUM                   | Client number. Unique identifier for the customer holding the account                       | Positive integer that forms unique identifier of customer                                    |
| Attrition_Flag              | Event variable describing if customer has closed account or not                             | String: 'Attrited Customer' for account closed, 'Existing Customer' for account still active |
| Customer_Age                | Demographic variable - customer's age in years                                              | Positive integer: range 26-73                                                                |
| Gender                      | Demographic variable - whether customer is male or female                                   | Single character: 'M' if male, 'F' if female                                                 |
| Dependent_count             | Demographic variable - number of dependents of customer                                     | Positive integer: range 0-5                                                                  |
| Education_Level             | Demographic variable - educational qualification of customer                                | String: 'Graduate', 'High School',                                                           |
| Marital_Status              | Demographic variable - marital status of customer                                           | String: 'Married', 'Single', 'Divorced', 'Unknown'                                           |
| Income_Category             | Demographic variable - annual income bracket of customer                                    | String: 'Less than $40K', '$40K - $60K', '$60K - $80K',                                      |
| Card_Category               | Product variable - type of card                                                             | String: 'Blue', 'Silver', 'Gold', 'Platinum'                                                 |
| Months_on_book              | Period of customer relationship with bank in months                                         | Positive integer: range 13-56                                                                |
| Total_Relationship_Count    | Total number of bank products held by the customer (ie. other accounts)                     | Positive integer: range 1-6                                                                  |
| Months_Inactive_12_mon      | Number of months customer was inactive in the last 12 months                                | Positive integer: range 0-6                                                                  |
| Contacts_Count_12_mon       | Number of contacts in the last 12 months                                                    | Positive integer: range 0-6                                                                  |
| Credit_Limit                | Product variable - credit limit on the customer's credit card                               | Positive integer: range 1440-34500                                                           |
| Total_Revolving_Bal         | Usage variable - total revolving balance on the customer's credit card                      | Positive integer: range 0-2517                                                               |
| Avg_Open_To_Buy             | Usage variable - 12 month average of customer's open to buy credit line                     | Positive integer: range 3-34500                                                              |
| Total_Amt_Chng_Q4_Q1        | Usage variable - relative change in transaction amount on card between previous quarters    | Positive float: range 0.63-3.4                                                               |
| Total_Trans_Amt             | Usage variable - total transaction amount on card in last 12 months                         | Positive integer: range 510-18500                                                            |
| Total_Trans_Ct              | Usage variable - total count of transactions on card in last 12 months                      | Positive integer: range 10-139                                                               |
| Total_Ct_Chng_Q4_Q1         | Usage variable - relative change in transaction count on card between previous quarters     | Positive float: range 0-3.71                                                                 |
| Avg_Utilization_Ratio       | Usage variable - Customers average ratio between revolving balance and credit limit on card | Positive float: range 0-1                                                                    |
| Naive*Bayes_Classifier*...  | Redundant column left in dataset by uploader, ignore                                        | n/a                                                                                          |
| Naive*Bayes_Classifier*...2 | Redundant column left in dataset by uploader, ignore                                        | n/a                                                                                          |

- **Project Terms & Jargon**
  - A customer is a person holding a credit card with the bank
  - A prospect is a prospective customer
  - An attritioned customer is one who closed their account
  - A relationship describes an individual service that a customer uses with the bank. The credit card account is a relationship, of which customers may have additional relationships (e.g. savings account, mortgage, etc.)
  - Utilization ratio is the ratio between a customers credit card balance and their credit card limit, 0 meaning no debt whatsoever and 1 meaning they have "maxed out"

## Business Requirements

A fictitious client for this project is a highly data-driven bank that is seeking to improve customer retention and profitability in its credit card service. When a customer enters a credit card relationship with the bank, the bank opens a **credit line** for them that they may use at any time to make purchases on the card, which adds to the card's balance. Customers will then service this credit by repayments and may pay the credit off partially or in full if they so choose, all with some additional fee to allow the bank to profit from providing the service. This process of adding to the card balance with purchases and drawing it down with repayments gives rise to a **revolving balance** - the portion of the account that is unpaid at the end of a billing cycle (typically one month long), of which interest is applied to.

Each credit card customer is restricted in the amount they may add to their credit card balance by a value called a **credit limit**. This is the size of the credit line that the bank views as viable to leave open for the customer, as well the maximum amount the bank calculates to be safe to lend to the customer. In terms of the bank's business, it is unprofitable for credit lines to go unused, and would prefer a situation where all customers have maxed out credit cards that they pay interest on, ie. the customers' **utilization ratio**, the ratio of revolving balance to credit limit, is kept as close to 1 as possible.

If a customer **attritions** (ie. closes their credit card account), this hurts the banks profits as the customer will have paid down their card balance in full rather than continually paying interest, may have unused credit lines the bank will need to reassign, and will also lower the banks potential pool of debtors going into the future. Preferably, the bank would like to have customers that will be retained, and if they are going to attrition, they would prefer they stay in the relationship with the bank for as many months as possible and have high utilization ratios in that time.

The client has shared a customer database containing information pertaining to the above profitability considerations for each customer, paired with customer demographic data and the type of credit card product they are using.

- **1** The client would like to better understand the patterns in the customer base so that the client can learn prospect demographics least likely to attrition. This will help their marketing team better target their advertising campaigns.

- **2** The client would like to determine whether a given prospect will attrition. They would also like to know if a prospect is likely to attrition, how long they are likely to keep their account open for. This will allow the sales team to determine if changing the product offered to the prospect (credit limit and type of card) may influence said prospect to not attrition/maintain their account for longer.

- **3** The client would like to determine the credit utilization based on prospect data. This will allow the bank to identify valuable prospects early on, which they may try to build customer loyalty with through offering targeted customer perks.

## Hypothesis and how to validate?

- 1 - It's suspected that attritioned customers have short relationship times.
  - Correlation study may be used to investigate this
- 2 - It's suspected that card category has some correlation with average utilization ratio.
  - Correlation study may be used to investigate this

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1:** Data visualization and correlation study

  - We will inspect the data related to the customer base.
  - We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to attrition.
  - We will plot the main variables that correlate to attrition to visualize insights.

- **Business Requirement 2:** Classification and regression analysis

  - We want to predict if a prospect will attrition or not. We want to build a binary classifier.
  - We want to predict the length of the relationship for a prospect that is predicted to churn. We want to build a regression model for this, but if it is low performing we may change to a multiclass classifier for ranges of relationship duration.

- **Business Requirement 3:** Regression analysis
  - We want to predict the credit utilization ratio for a given prospect. We want to build a regression model for this, but if this displays low performance we could also change this task to a multiclass classifier between low utilization (0-0.3), medium utilization (0.3-0.7), and high utilization (0.7-1).

Should either of the above tasks involve classification, cluster analysis of prospects may be required

## ML Business Case

### Predict Attrition

#### Classification Model

- We want an ML model to predict if a prospect will attrition based on historical data from the customer data, excluding data that would only be available for established customers (usage data, e.g. total revolving balance, total transaction count etc.). The target variable is categorical and contains 2 classes. We consider a **classification model**. It is a supervised model, a 2-class, single label, classification model output: 0 (no attrition) or 1 (yes attrition)
- The ideal outcome is to provide the sales and marketing teams with reliable insight into the best profile of a loyal customer for onboarding/to target advertising to.
- The model success metrics:
  - at least 80% recall for attrition, on train and test set
  - The ML model is considered a failure if:
    - after 3 months of uage, more than 30% of new customers identified to not attrition end up attrition (even if the model performs well on the provided dataset, this will indicate that what it has learned on is not generalizable to future customer dynamics)
    - Precision for no attrition is lower than 80% on train and test set. (Don't want to waste means of converting a customer to no attrition such as raising credit limits or better card categories.)
  - The model output is defined as a flag, indicating if a prospect will attrition or not and the probability they will attrition. If the prospect applies online, they will supply the input data into a form. If the prospect is talking directly to a salesperson, the salesperson will ask for this information directly to input into the app. The predictions is made on the fly (not for batches).
  - Heuristics: There are no obvious heuristics for performing this task.
  - The training data to fit the model comes from the bank. This dataset contains approximately 10,000 customer records.
    - Train data - target: Attrition_Flag; features: Customer_Age, Gender, Dependent_count, Education_Level, Marital_Status, Income_Category, Card_Category, Total_Relationship_Count - 1, Credit_Limit

### Predict Relationship

#### Regression Model

- We want an ML model to predict the length of time a prospect will remain in the credit card relationship, should they be predicted to attrition. The target variable is a discrete number. We consider a **regression model**, which is supervised and unidimensional.
- The ideal outcome is to provide the sales and marketing teams with reliable insight into the best profile of a loyal customer for onboarding/to target advertising to.
- The model success metrics:
  - At least 0.7 for R2 score, on train and test set
  - The ML model is considered a failure if:
    - after 12 months of usage, the model's predictions are 50% off more than 30% of the time.
  - The output is defined as a continuous value for relationship length in months. This model will only make a prediction if the Predict Attrition Classifier predicts 1 (yes attrition). If the prospect applies online, they will supply the input data into a form. If the prospect is talking directly to a salesperson, the salesperson will ask for this information directly to input into the app. The predictions is made on the fly (not for batches).
  - Heuristics: currently, there are no heuristics for predicting relationship lengths for a prospect.
  - The training data to fit the model comes from the bank. This dataset contains approximately 10,000 customer records.
    - Train data - filter data where Attrition_Flag == 'Attrited Customer', then drop the Attrition_Flag variable. Target: Months_on_book; features: Customer_Age, Gender, Dependent_count, Education_Level, Marital_Status, Income_Category, Card_Category, Total_Relationship_Count - 1, Credit_Limit

### Predict Utilization

#### Regression Model

- We want an ML model to predict the average credit utilization ratio for a give prospect. The target variable is a continuous number, ranging from 0 to 1. We consider a **regression model** which is supervised and unidimensional.
- The ideal outcome is to provide the sales and marketing teams with reliable insight into the best profile of a highly profitable customer for onboarding/to target advertising to. It will also provide the finance team with a sense of what utilization they may expect on credit lines for new customers, which may allow them to adjust credit limits (i.e. to save the bank giving a 34.5k credit limit to a customer that never puts more than 500 on their card)
- The model success metrics:
  - At least 0.8 for R2 score, on train and test set
  - The ML model is considered a failure if:
    - after 12 months of usage, the model's predictions are 50% off more than 20% of the time.
  - The output is defined as a continuous value for credit utilization ratio ranging between 0 and 1. If the prospect applies online, they will supply the input data into a form. If the prospect is talking directly to a salesperson, the salesperson will ask for this information directly to input into the app. The predictions is made on the fly (not for batches).
  - Heuristics: There are no obvious heuristics for performing this task.
  - The training data to fit the model comes from the bank. This dataset contains approximately 10,000 customer records.
    - Train data - target: Avg_Utilization_Ratio; features: Customer_Age, Gender, Dependent_count, Education_Level, Marital_Status, Income_Category, Card_Category, Total_Relationship_Count - 1, Credit_Limit

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
- Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

- Thank the people that provided support through this project.
