# Customer Churn Prediction & Business Intelligence Platform

An AI-powered analytics platform that analyzes customer behavior and predicts customer churn using Machine Learning and Business Intelligence techniques.

The project helps businesses identify high-risk customers, analyze churn patterns, and improve customer retention using interactive dashboards and predictive analytics.

---

# Features

## Customer Analytics
- Customer churn analysis
- Revenue analysis
- Customer segmentation
- Contract type analysis
- Internet service analysis

## Machine Learning
- Churn prediction model
- Customer risk scoring
- AI-based customer retention insights

## Interactive Dashboard
- KPI cards
- Churn distribution charts
- Revenue analytics
- Customer behavior visualization
- Live AI prediction system

## Business Intelligence
- Churn trend analysis
- Retention recommendations
- Customer risk insights
- Revenue impact analysis

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- KaggleHub
- Joblib

---

# Project Structure

```bash
customer-churn-analytics/
│
├── analytics/
│   ├── data_cleaning.py
│   └── eda.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── train_model.py
│   ├── churn_model.pkl
│   └── label_encoders.pkl
│
├── utils/
│   └── download_data.py
│
├── app.py
├── requirements.txt
├── README.md
```

---

# Project Workflow

```text
Dataset Download
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Business Insights
       ↓
Machine Learning Model
       ↓
AI Churn Prediction
       ↓
Interactive Dashboard
```

---

# Dataset

This project uses the IBM Telco Customer Churn dataset downloaded automatically using Python.

Dataset Source:

https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-analytics.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Dataset Download

```bash
python utils/download_data.py
```

---

# Run Data Cleaning

```bash
python analytics/data_cleaning.py
```

---

# Train Machine Learning Model

```bash
python models/train_model.py
```

---

# Run Dashboard

```bash
streamlit run app.py
```

---

# Dashboard Features

- Customer churn distribution
- Contract type analysis
- Revenue analysis
- Internet service insights
- AI churn prediction
- Customer risk probability
- Retention recommendations

---

# Machine Learning Model

The project uses:
- Random Forest Classifier

for customer churn prediction.

Model predicts:
- whether a customer may leave the company
- churn probability score
- customer risk level

---

# Business Problem Solved

Customer churn is a major problem for telecom and subscription-based companies.

This platform helps businesses:
- identify customers likely to churn
- improve customer retention
- reduce revenue loss
- make data-driven business decisions

---

# Future Improvements

- Advanced feature engineering
- XGBoost model
- Deep learning prediction
- Real-time customer analytics
- Cloud deployment
- Automated business reports

---

# Author

Koram Lahari

---

# License

This project is for educational and portfolio purposes.
