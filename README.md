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

creditcard-churn is a dashboard application that enables a bank to analyse various aspects of prospective credit card customers (prospects) to determine if they will be retained as customers and how profitable they will be overall.

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

| Variable                 | Meaning                                                                                     | Units                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| CLIENTNUM                | Client number. Unique identifier for the customer holding the account                       | Positive integer that forms unique identifier of customer |
| Attrition_Flag           | Event variable describing if customer has closed account or not                             | 1 for account closed, 0 for account still active          |
| Customer_Age             | Demographic variable - customer's age in years                                              | Positive integer: range 26-73                             |
| Gender                   | Demographic variable - whether customer is male or female                                   | Single character: 'M' if male, 'F' if female              |
| Dependent_count          | Demographic variable - number of dependents of customer                                     | Positive integer: range 0-5                               |
| Education_Level          | Demographic variable - educational qualification of customer                                | String: 'Graduate', 'High School',                        |
| Marital_Status           | Demographic variable - marital status of customer                                           | String: 'Married', 'Single', 'Divorced', 'Unknown'        |
| Income_Category          | Demographic variable - annual income bracket of customer                                    | String: 'Less than $40K', '$40K - $60K', '$60K - $80K',   |
| Card_Category            | Product variable - type of card                                                             | String: 'Blue', 'Silver', 'Gold', 'Platinum'              |
| Months_on_book           | Period of customer relationship with bank in months                                         | Positive integer: range 13-56                             |
| Total_Relationship_Count | Total number of bank products held by the customer (ie. other accounts)                     | Positive integer: range 1-6                               |
| Months_Inactive_12_mon   | Number of months customer was inactive in the last 12 months                                | Positive integer: range 0-6                               |
| Contacts_Count_12_mon    | Number of contacts in the last 12 months                                                    | Positive integer: range 0-6                               |
| Credit_Limit             | Product variable - credit limit on the customer's credit card                               | Positive integer: range 1440-34500                        |
| Total_Revolving_Bal      | Usage variable - total revolving balance on the customer's credit card                      | Positive integer: range 0-2517                            |
| Avg_Open_To_Buy          | Usage variable - 12 month average of customer's open to buy credit line                     | Positive integer: range 3-34500                           |
| Total_Amt_Chng_Q4_Q1     | Usage variable - relative change in transaction amount on card between previous quarters    | Positive float: range 0.63-3.4                            |
| Total_Trans_Amt          | Usage variable - total transaction amount on card in last 12 months                         | Positive integer: range 510-18500                         |
| Total_Trans_Ct           | Usage variable - total count of transactions on card in last 12 months                      | Positive integer: range 10-139                            |
| Total_Ct_Chng_Q4_Q1      | Usage variable - relative change in transaction count on card between previous quarters     | Positive float: range 0-3.71                              |
| Avg_Utilization_Ratio    | Usage variable - Customers average ratio between revolving balance and credit limit on card | Positive float: range 0-1                                 |

## Business Requirements

- Describe your business requirements

## Hypothesis and how to validate?

- List here your project hypothesis(es) and how you envision validating it (them)

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- List your business requirements and a rationale to map them to the Data Visualizations and ML tasks

## ML Business Case

- In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course

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
