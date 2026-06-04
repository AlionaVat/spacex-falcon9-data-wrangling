# 🚀 SpaceX Falcon 9 Data Wrangling & Exploratory Analysis

## 📌 Overview

This project is part of the IBM Data Science curriculum and focuses on data wrangling, exploratory data analysis (EDA), and preparation of SpaceX Falcon 9 launch data for predictive modeling.

The objective is to analyze historical Falcon 9 launch records, identify patterns related to first-stage landing outcomes, and prepare a clean dataset suitable for machine learning applications.

---

## 🎯 Project Objectives

* Load and inspect SpaceX launch data
* Identify and handle missing values
* Explore launch site distributions
* Analyze orbit types and mission characteristics
* Investigate relationships between launch parameters and landing outcomes
* Prepare target labels for future machine learning models
* Create a structured dataset for predictive analysis

---

## 📊 Dataset

The dataset contains historical Falcon 9 launch information, including:

* Flight Number
* Launch Site
* Payload Mass
* Orbit Type
* Booster Version
* Landing Outcome
* Launch Date
* Mission Success Indicators

The data was provided through IBM Skills Network and SpaceX educational resources.

---

## 🔍 Data Wrangling Process

### Data Loading

* Imported launch dataset using Pandas
* Reviewed dataset structure and contents
* Performed initial validation checks

### Missing Value Analysis

* Calculated missing value percentages
* Identified incomplete attributes
* Evaluated data quality

### Feature Inspection

* Classified numerical and categorical variables
* Reviewed feature distributions
* Examined launch-related attributes

### Exploratory Analysis

* Launch frequency by launch site
* Orbit distribution analysis
* Payload mass exploration
* Landing outcome investigation
* Mission pattern identification

---

## 📈 Key Analysis Areas

### Launch Sites

The project analyzes launch activity across major SpaceX launch facilities:

* CCAFS LC-40
* CCAFS SLC-40
* KSC LC-39A
* VAFB SLC-4E

### Orbit Analysis

Mission orbit categories include:

* LEO (Low Earth Orbit)
* ISS (International Space Station)
* GTO (Geostationary Transfer Orbit)
* Polar Orbit
* Sun-Synchronous Orbit
* Other mission-specific trajectories

### Landing Outcome Investigation

Special attention is given to:

* Successful landings
* Failed landings
* Ocean landings
* Drone ship landings
* Ground pad landings

---

## 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook

---

## 📂 Project Structure

```text
spacex-falcon9-data-wrangling/
│
├── labs-jupyter-spacex-Data wrangling.ipynb
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/spacex-falcon9-data-wrangling.git
cd spacex-falcon9-data-wrangling
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
labs-jupyter-spacex-Data wrangling.ipynb
```

Run all cells sequentially to reproduce the analysis.

---

## 📊 Expected Outcomes

* Cleaned and validated launch dataset
* Missing value assessment
* Launch site statistics
* Orbit distribution insights
* Landing outcome analysis
* Machine learning label preparation

---

## 📚 Learning Outcomes

Through this project:

* Applied data wrangling techniques
* Practiced exploratory data analysis
* Investigated real-world aerospace datasets
* Prepared data for machine learning workflows
* Improved proficiency with Pandas and Jupyter

---

## 🚀 Future Improvements

* Advanced visualization with Plotly
* Predictive landing success models
* Feature engineering
* Interactive dashboards
* Deployment of predictive services

---

## 👩‍💻 Author

Aliona Vataman

IBM Data Science Professional Certificate
Software Engineering 
