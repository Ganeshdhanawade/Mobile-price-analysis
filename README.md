
# Mobile Price Prediction

New startup mobile company, they wants to give tough fight to big companies like Apple,Samsung etc.
They does not know how to estimate price of mobiles his company creates. In this competitive mobile phone market you cannot simply assume things. To solve this problem he collects sales data of mobile phones of various companies.
His wants to find out some relation between features of a mobile phone(eg:- RAM,Internal Memory etc) and its selling price.



## Motivation
The motivation was to experiment with end to end machine learning project and get some idea about deployment platform like [render](https://dashboard.render.com/) and offcourse this "Price prediction" is helpfull the deside the price of mobile. Help to decide wich mobile feature are more important to customer are perches the mobile. Using machine learning we have built a predictive model that can predict whether the mobile price range is low, medium ,high or very high. This is also sort of fun to work on a project like this which could be beneficial for the comapany.
## Features
Below is the features are highly affected by the selection of the correct price of the mobile.

- ram : Random Access Memory in Gega Bytes
- px_height : Pixel Resolution Height
- px_width  : Pixel Resolution Width
- battery_power : Total energy a battery can store in one time measured in mAh


## PowerBI Dekstop
Power BI is a technology-driven business intelligence tool provided by Microsoft for analyzing and visualizing raw data to present actionable information. It combines business analytics, data visualization, and best practices that help an organization to make data-driven decisions.

We can create the visual on PowerBI report to check the relation between features, those are play importat role on the prediction.
PowerBI is good platform for just click to create the visuals and push the online powerbi service to connect so many peaple to create visuals in same time or send to others.
In the more details [click here](https://powerbi.microsoft.com/en-us/desktop/) to check more details about PowerBI.
## Report
Here is the report for PowerBI

![powerbi gif](https://user-images.githubusercontent.com/109405138/209288952-17f6598e-f6ab-4834-afac-627408ed7fc9.gif)

## Installation
```bash
  Pip install requrement.txt
```
```bash
  Flask==1.1.1
gunicorn==19.9.0
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
Werkzeug==0.15.5
numpy>=1.9.2
scipy>=0.15.1
scikit-learn>=0.18
matplotlib>=1.4.3
pandas>=0.19

```
## Deployment

To deploy this project on [render](https://dashboard.render.com/)

```bash
  npm run gunicorn app:app
```


## Demo

Below is the domo for created application

![New Project](https://user-images.githubusercontent.com/109405138/208868848-be1b6bfe-3b83-41bb-a1a4-4959e5c16896.gif)


## Live demo
Below is the link for live demo

https://mobile-price-analysis-api.onrender.com/
## Learning Objective
The following points were the objective of the project . If you are looking for all the following points in this repo then i have not covered all in this repo. I'm working on blog about this mini project and I'll update the link of blog about all the points in details later . (The main intention was to create an end-to-end ML project.)

- Data gathering
- Descriptive Analysis
- Data Visualizations
- Data Preprocessing
- Data Modelling
- Model Evaluation
- Model Deployment
## Technical Aspect
- Using PowerBI dekstop create the report.
- Training a machine learning model using scikit-learn.
- Building and hosting a Flask web app on Render.
- A user has to put details like ram, battry power, Pixel resolution Height etc .
- Once it get all the fields information , the prediction is displayed on a new page .
## Usage/Examples

```javascript
app=Flask(__name__)

@app.route('/')
def page():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
```


## Dataset
Now we can download the dataset on Kaggle and make analysis for it. Kaggle is the one of the largest website have to provide the datasets on verious domain.
In the more information about the Kaggle plese [Click Here](https://www.kaggle.com/)

Below link is to dataset on kaggle

https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification
## Acknowledgements

 - [Awesome HTML Templates](https://github.com/Ganeshdhanawade/Mobile-price-analysis/commit/79213690628738dcd2f12d9bccf38dae35de1725)
 - [Awesome Flask file](https://github.com/matiassingers/awesome-readme)
 - [Project Details](https://github.com/Ganeshdhanawade/Mobile-price-analysis/blob/main/Mobile%20Price%20Classification_detailed.docx)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## Lessons Learned

Now the bulding that project i can learn the concept of how to create the web in HTML and how to desing that page well attractive. Also i can get the tainled knowlaged about the render to how exactly deploy the model on cloud.

In challanges my mesure challange is that how to select the best feature they are highly affected my responce.
and selection of the best model to improve the accuracy.


# Hi, I'm Ganesh! 👋


## 🚀 About Me
I am Completed post graduation in statistics with verious takenincal skills and 2+ year of experiance in data science domain. This project i create on self learning.


## Other Common Github Profile Sections
👩‍💻 I'm currently working on Assistant Proffesor in KVM,wai

🧠 I'm currently learning Deep learning and NLP.

👯‍♀️ I'm looking to Job Change toword the data science.




## 🛠 Skills
R, spss, Python, Flask, ML, DL, NLP, Render, MySQL, PowerBI, Excel etc.


![Logo](https://camo.githubusercontent.com/3cdf9577401a2c7dceac655bbd37fb2f3ee273a457bf1f2169c602fb80ca56f8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)
![images](https://user-images.githubusercontent.com/109405138/209291383-14f3f225-e593-4b1b-a506-54db907bb433.png)
![download](https://user-images.githubusercontent.com/109405138/209292205-98d13147-5a84-47d3-82eb-870197067abf.png)



## Feedback

If you have any feedback, please reach out to us at dhanawadeganesh386@gmail.com


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/Ganeshdhanawade/Data-Science-Portfolio)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ganesh-dhanawade-47653b201/)




