import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Customer Churn Analytics",
    layout="wide"
)

# ====================================
# LOAD DATA
# ====================================

df = pd.read_csv(
    "data/processed/cleaned_churn.csv"
)
# ====================================
# TITLE
# ====================================

st.title("Customer Churn Analytics Platform")


tab1, tab2 = st.tabs([
    "Business Analytics",
    "AI Churn Prediction"
])

# ====================================
# KPI CARDS
# ====================================
with tab1:
    total_customers = len(df)
    churn_rate = round(
    df["Churn"].mean() * 100,
    2
    )
    monthly_revenue = round(
    df["MonthlyCharges"].sum(),
    2
    )
    avg_charge = round(
    df["MonthlyCharges"].mean(),
    2
    )
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(
    "Total Customers",
    total_customers
    )
    col2.metric(
    "Churn Rate",
    f"{churn_rate}%"
    )
    col3.metric(
    "Monthly Revenue",
    f"${monthly_revenue}"
    )
    col4.metric(
    "Avg Monthly Charge",
    f"${avg_charge}"
    )
    # ===================================
    # CHURN DISTRIBUTION
    # ===================================
    st.subheader("Customer Churn Distribution")
    
    fig1 = px.pie(
    df,
    names="Churn",
    title="Churn Distribution"
    )
    st.plotly_chart(
    fig1,
    use_container_width=True,
    key="churn_pie"
    )
    # ====================================
    # CONTRACT ANALYSIS
    # ====================================
    st.subheader("Contract Type Analysis")
    
    contract_data = (
    df["Contract"]
    .value_counts()
    .reset_index()
    )
    contract_data.columns = [
    "Contract",
    "Customers"
    ]
    fig2 = px.bar(
    contract_data,
    x="Contract",
    y="Customers",
    title="Customers by Contract Type"
    )
    st.plotly_chart(
    fig2,
    use_container_width=True,
    key="contract_chart"
    )
    # ===================================
    # INTERNET SERVICE ANALYSIS
    # ===================================
    st.subheader("Internet Service Analysis")
    internet_data = (
    df["InternetService"]
    .value_counts()
    .reset_index()
    )
    internet_data.columns = [
    "Service",
    "Customers"
    ]
    fig3 = px.bar(
    internet_data,
    x="Service",
    y="Customers",
    title="Internet Service Distribution"
    )
    st.plotly_chart(
    fig3,
    use_container_width=True,
    key="internet_chart"
    )
    # ===================================
    # MONTHLY CHARGE DISTRIBUTION
    # # =================================
    st.subheader("Monthly Charges Distribution")
    fig4 = px.histogram(
    df,
    x="MonthlyCharges",
    nbins=30,
    title="Monthly Charges Distribution"
    )
    st.plotly_chart(
    fig4,
    use_container_width=True,
    key="charge_hist"
    )
    model = joblib.load(
    "models/churn_model.pkl"
    )
    label_encoders = joblib.load(
    "models/label_encoders.pkl"
    )


with tab2:

    st.subheader("Customer Churn Prediction")

    tenure = st.slider(
        "Customer Tenure (Months)",
        1,
        72,
        12
    )

    monthly_charges = st.slider(
        "Monthly Charges",
        20,
        150,
        70
    )

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    # ============================
    # ENCODE INPUTS
    # ============================

    contract_encoded = (
        label_encoders["Contract"]
        .transform([contract])[0]
    )

    internet_encoded = (
        label_encoders["InternetService"]
        .transform([internet_service])[0]
    )

    # ============================
    # CREATE INPUT DATAFRAME
    # ============================

    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "Contract": [contract_encoded],
        "InternetService": [internet_encoded]
    })

    # ============================
    # PREDICT BUTTON
    # ============================

    if st.button("Predict Churn"):

        prediction = model.predict(
            input_data
        )[0]

        probability = (
            model.predict_proba(input_data)[0][1]
        )

        # ========================
        # OUTPUT
        # ========================

        if prediction == 1:

            st.error(
                "High Risk Customer Likely To Churn"
            )

        else:

            st.success(
                "Customer Likely To Stay"
            )

        st.subheader("Churn Probability")

        st.write(
            round(probability * 100, 2),
            "%"
        )

        # ========================
        # RETENTION INSIGHTS
        # ========================

        st.subheader(
            "Retention Recommendation"
        )

        if probability > 0.7:

            st.write(
                "- Offer loyalty discounts"
            )

            st.write(
                "- Provide long-term contract benefits"
            )

            st.write(
                "- Improve customer engagement"
            )

        elif probability > 0.4:

            st.write(
                "- Send personalized offers"
            )

            st.write(
                "- Improve support quality"
            )

        else:

            st.write(
                "- Customer appears stable"
            )
   