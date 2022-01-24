# Individual-project
# About the Project

## Project Goals

Our overall goal is to identify key drivers for happiness among a variation of countries around the world and predict happiness based on these key drivers.


## Project Description

The World Happiness Report is a landmark survey of the state of global happiness that ranks 156 countries by how happy their citizens perceive themselves to be.

In this project, we will utilize the information in The World Happiness Report, explore key drivers of happiness by analyzing and making correlations with various (quality of) life factors, and then we will use machine learning to create a regression model that predicts happiness.


### Initial Questions

- What is the relationship between happiness and income (GDP)?

- What is the relationship between happiness and freedom?
    
- What is the relationship between happiness and perceptions of corruption?

- How different is happiness depending on the geographical region?



### Data Dictionary

| Variable            |     Description  |     
| ----------------    | ------------------ |
|Ladder score          | Happiness score or subjective well-being. This is the national average response to the question of life evaluations |
|Logged GDP per capita         | The GDP-per-capita time series from 2019 to 2020 using countryspecific forecasts of real GDP growth in 2020 |
|Social support             | Social support refers to assistance or support provided by members of social networks to an individual |
|Healthy life expectancy          | Healthy life expectancy is the average life in good health - that is to say without irreversible limitation of activity in daily life or incapacities - of a fictitious generation subject to the conditions of mortality and morbidity prevailing that year |
|Freedom to make life choices   | Freedom to make life choices is the national average of binary responses to the GWP question “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?” |
|Generosity | Generosity is the residual of regressing national average of response to the GWP question “Have you donated money to a charity in the past month?” on GDP per capita |
|Perceptions of corruption           | The measure is the national average of the survey responses to two questions in the GWP: “Is corruption widespread throughout the government or not” and “Is corruption widespread within businesses or not?”  |
|Ladder score in Dystopia                 | It has values equal to the world’s lowest national averages. Dystopia as a benchmark against which to compare contributions from each of the six factors. Dystopia is an imaginary country that has the world's least-happy people. ... Since life would be very unpleasant in a country with the world's lowest incomes, lowest life expectancy, lowest generosity, most corruption, least freedom, and least social support, it is referred to as “Dystopia,” in contrast to Utopia |



## Steps to Reproduce

- Create an env.py file that contains the hostname, username and password of the mySQL database that contains the zillow table. Store that env file locally in the repository.
- Clone my repo (including an acquire.py and prepare.py) (confirm .gitignore is hiding your env.py file)
- Libraries used are pandas, matplotlib, seaborn, numpy, sklearn.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.

### Plan

Plan - Acquire - Prepare - Explore - Model - Deliver

- Wrangle
    - Acquire data
    - Prepare data by doing a cleanup of null values, duplicates, removed unnecessary outliers.
    - We will create a function that we can reference later to acquire and prepare the data by storing the function in a file name wrangle.py
    - We will split our data to a train, validate, and test
- Explore
    - Create visualizations of data to pin point key drivers of happiness
    - Create a visualizations correlating to hypotheses statements
    - Run at least two statistical tests that will support whether the hypothesis has been rejected or not
- Modeling
    - Establish baseline
    - Ensure models are tested on appropriate validate and test datasets
    - Determine best performing model and test on test dataset
- Delivery
    - Final Report in Jupyter Notebook
    - README with project details
    - Python modules with acquire and prepare functions