# Heatlthcare-related-prediction

### Table of content
- Demo
- Overview
- Motivation and goals
- Technical aspects
- Installation and Run
- Technologies used
- Credits

#### Demo
link-https://healthcare-related-prediction.herokuapp.com

- You may click the above link and check the health condition based on three disease

#### Overview

This healthcare related prediction project consists of diabetes, heart disease and breast cancer prediction using Flask web app and Heroku platform. The freely available datasets have downloaded from kaggle.com to train and the fit machine learning models. To get the better understanding of each dataset, explanatory data analysis has performed. According to the features’ behavior and the model that going to be trained, different techniques of feature engineering carried out.

#### Motivation and goals

Since theoretical knowledge of machine learning concepts are not enough to get better understanding, I try to implement end to end project. Through this project, I could able to understand the life cycle of a data science project. when it was perfectly deployed in Heroku platform, it gave me the courage to implement many data science projects.

#### Technical Aspects
This project consists of two major parts:
1.	Model training and fitting
- Explanatory Analysis - graphs and charts have used according to the type of variables, this will help to get the better understanding of features.

- Feature engineering – if necessary, handling missing values, feature scaling, log transformation and handling categorical variables.

- Model fitting-  final machine learning algorithm has been selected depending on the behavior of the dataset and the accuracy of the prediction during train and test.

2.	Create web app and hosting it through Herako platform 
- Creating HTML pages for end user to enter the measurements for each disease prediction Building a Flask app to get those users entered values to the fitted model Deployed the final model using Heroku.

#### Installation
- Clone the repository
- Change to the project directory
 ```python
 cd file_path
 ```
- Create a python virtual environment
```python
conda create --name myenv
```
- Activate the virtual environment
```pyhton
activate myenv
```
- Install the requirements
```python
pip install -r requirements.txt
```
- Running the app
```python
python app.py
```
#### Technologies used
<img src="https://www.seekpng.com/png/detail/807-8079213_jupyter-sq-text-jupyter-notebook-logo-png.png" width="100" height="115">    <img src="https://www.seekpng.com/png/full/141-1415544_html-css-projects-small-logo-on-html.png" wwidth="100" height="75">     <img src="https://miro.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png" width="100" height="75">      <img src="https://www.nicepng.com/png/detail/67-671824_heroku-logo-heroku.png" width="100" height="75">

#### Credits
This project would not have completed without the help of the tutorials of [Krish Naik](https://www.youtube.com/watch?v=bPrmA1SEN2k&list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe), because his explanation on each topic gives the depth understanding of all the concepts of machine learning and deep learning concepts. 

