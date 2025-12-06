# Worldwide Travel Analysis

This repository contains all the project files for the first group hackathon in Code Institute's, Data Analytics with AI bootcamp.

## Table of Contents

1. [Project Overview & Goal](#1-project-overview-goal)
2. [Technical Stack](#2-technical-stack)
3. [ETL Pipeline and Transformation Summary](#3-etl-pipeline-and-transformation-summary)
4. [How to Run the Project Locally](#4-how-to-run-the-project-locally)


## 1. Project Overview & Goal

### Data Source
This project utilises the [*Worldwide Travel Cities (Ratings and Climate*](https://www.kaggle.com/datasets/furkanima/worldwide-travel-cities-ratings-and-climate) sourced from Kaggle.

The dataset provides a comprehensive view of digital habits and lifestyle factors through the following key variables:

- Digital Habits: Daily screen time, preferred social media platform, and days spent without social media (digital detox).

- Mental Health Indicators: Happiness levels, sleep quality, stress scores, and exercise frequency.

### Project's Focus
Our project focuses on analysing global travel destinations using the Worldwide Travel Cities dataset to understand how factors like budget level, climate, and other attributes influence trip choices. We aim to explore patterns in travel ratings, duration preferences, and climate characteristics across 560 cities.

#### Key Research Questions
Our goal for the project was explored using the following research questions. We created hypothese for each question based on what we expected to find and that was the guide for our analysis.

1. **Are luxury destinations associated with higher temperatures?**
    
    Hypothesis: Luxury destinations will be located in cities that have higher average temperatures compared to mid-range and budget destinations.
   
2. **Do budget levels influence trip duration?**

    Hypothesis: Budget-friendly destinations will be associated with shorter recommended trip durations compared to mid-range and luxury destinations.

## 2. Technical Stack

- **Core Languages:** Python
- **Data Processing (ETL):** Pandas, NumPy, kagglehub
- **Visualisation:** Matplotlib (Basic Plotting), Seaborn (Statistical Visuals/Heatmaps), Scipy, Scikit Learn (Machine Learning), Streamlit (Advanced Interactive Charts) and Tableau (Visualisation)
- **Version Control:** Git & GitHub


## 3. ETL Pipeline and Transformation Summary
The data used is the [*Worldwide Travel Cities (Ratings and Climate*](https://www.kaggle.com/datasets/furkanima/worldwide-travel-cities-ratings-and-climate), containing 560 records and 19 attributes.

"Discuss here any issues with the data when cleaning"

### Categorical Variables (No Encoding)


## Key Findings

**Question 1:**


**Question 2:**


## Final Summary


## 4. How to Run the Project Locally

### Clone the Repository

```bash
git clone [https://github.com/miteshbkumar-ship-it/social_mental_health_project]

cd social_mental_health_project
```

### Install Dependencies

You will need a ```requirements.txt``` file listing pandas, numpy, streamlit, etc.
Open your terminal or a Jupyter cell and run:

```bash
pip install -r requirements.txt
```

### Streamlit Dashboard

Run the streamlit ```dashboard_app.py``` app and it will open automatically in your browser, displaying the interactive plots (Scatter, Sunburst, etc.).

```bash
streamlit run dashboard_app.py
```

### Run the Notebook

Open `spf_analysis.ipynb` and run all cells sequentially. The notebook will automatically download the data, run the ETL pipeline, and generate all seaborn/matplotlib visualizations.



Created by Team C: **Anisa, Bhavita, Kanyinsola and Lola**
