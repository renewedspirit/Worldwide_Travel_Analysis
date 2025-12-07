![travel icon](https://www.freeiconspng.com/uploads/hajj-and-umrah-travel-icon-24.png)
# Worldwide Travel Analysis 
This repository contains all the project files for the first group hackathon in Code Institute's, Data Analytics with AI bootcamp.

## Table of Contents

1. [Project Overview & Goal](#1-project-overview-goal)
2. [Tools & Technologies](#2-tools-tech)
3. [Target Audience](#3-target-audience)
4. [Expected Deliverables](#4-expected-deliverables)
5. [Data Transformation Summary](#5-data-transformation-summary)
6. [How to Run the Project Locally](#6-how-to-run-the-project-locally)


## 1. Project Overview & Goal

### Dataset & Source
This project utilises the [*Worldwide Travel Cities (Ratings and Climate*](https://www.kaggle.com/datasets/furkanima/worldwide-travel-cities-ratings-and-climate) sourced from Kaggle, contains 560 records and 19 attributes.

This dataset contains travel information for 560 cities worldwide, including city data (name, country, region, coordinates), descriptive summaries, climate data (monthly avg/min/max temperatures), ideal trip durations, budget levels, and ratings of features of the city such as culture, nature, cuisine, wellness, nightlife, and beaches.

### Project's Focus
Our project focuses on analysing global travel destinations using the Worldwide Travel Cities dataset to understand how factors like budget level, climate, and other attributes influence trip choices. We aim to explore patterns in travel ratings, duration preferences, and climate characteristics across 560 cities.

#### Key Research Questions
Our goal for the project was explored using the following research questions. We created hypothese for each question based on what we expected to find and that was the guide for our analysis.

1. **Are luxury destinations associated with higher temperatures?**
    
    Hypothesis: Luxury destinations will be located in cities that have higher average temperatures compared to mid-range and budget destinations.
   
2. **Do budget levels influence trip duration?**

    Hypothesis: Budget-friendly destinations will be associated with shorter recommended trip durations compared to mid-range and luxury destinations.


## 2. Tools & Technologies

- **Trello**
- **Python, Pandas, NumPy, Matplotlib, Seaborn** 
- **Jupyter Notebook** 
- **GitHub (Version Control)**
- **Streamlit (interactive dashboard)**
- **Tableau Public (dashboard)** 


## 3. Target Audience 

The dashboard and interactive tool are intended for:

**1. Travellers who want help choosing a destination -** Those looking for travel suggestions based on a budget, continent, climate, or travel style.

**2. Tourism platforms exploring location insights -** For travel related companies, such as airlines or package holidays companies that are looking for data insights to optimise their offerings.


## 4. Expected Deliverables

Our final outputs for the hackathon will be:

- Clean, structured dataset ready for analysis

- Power BI/Tableau dashboard with interactive visuals

- Streamlit mini-app for destination recommendations

- Project documentation (e.g. README, Project Proposal etc)

- Final presentation summarising findings, insights, and recommendations

## 5. Data Transformation Summary

| Original Column / Feature                                                                                               | Transformation Applied                                                                                           | New Column(s) Created                                                       | Purpose / Notes                                                          |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `id`                                                                                                                    | Dropped                                                                                                          | —                                                                           | Not useful for analysis; default index replaces it.                      |
| `avg_temp_monthly`                                                                                                      | Parsed JSON-like string → extracted monthly averages → calculated annual mean → dropped after feature extraction | `annual_avg_temp`                                                           | Simplifies climate data into one metric for analysis.                    |
| `ideal_durations`                                                                                                       | Converted from string list into Python list using `ast.literal_eval`→ Split into multiple binary indicator → Dropped after creating columns                                                                     | `is_short_trip`, `is_one_week`, `is_long_trip`, `is_weekend`, `is_day_trip` | Enables filtering, grouping, and correlation analysis.                   |
| `budget_level`                                                                                                          | Encoded categories into numbers (e.g., Budget=1, Mid-range=2, Luxury=3)                                          | —                                                                           | Makes the column usable for numerical analysis.                          |
| Ratings Columns (`culture`, `adventure`, `nature`, `beaches`, `nightlife`, `cuisine`, `wellness`, `urban`, `seclusion`) | Combined using mean                                                                                              | `city_rating`                                                               | Creates overall score; representing appeal.                 |
|`short_description`                                                                                                     | Kept for dashboard dataset, then deleted for analysis                                                                                    | —                                                                           | Needed for Streamlit recommendations.                                    |
| `latitude`, `longitude`                                                                                                 | Kept unchanged for dashboard dataset, then deleted for analysis                                                                                                   | —                                                                           | Used for mapping visualisations (even if not used in notebook analysis). |



  
## 6. How to Run the Project Locally

### Clone the Repository

```bash
git clone [https://github.com/renewedspirit/Worldwide_Travel_Analysis]

cd Worldwide_Travel_Analysis
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
