import pandas as pd

# =========================
# LOAD CLEAN DATA
# =========================

df = pd.read_csv(
    "data/processed/cleaned_churn.csv"
)

print("\nDATA LOADED\n")

# =========================
# BASIC INFO
# =========================

print("Dataset Shape:")
print(df.shape)

# =========================
# CHURN RATE
# =========================

churn_rate = (
    df["Churn"].mean()
) * 100

print("\nChurn Rate:")
print(round(churn_rate, 2), "%")

# =========================
# TOTAL REVENUE
# =========================

total_revenue = (
    df["MonthlyCharges"].sum()
)

print("\nTotal Monthly Revenue:")
print(round(total_revenue, 2))

# =========================
# AVERAGE MONTHLY CHARGE
# =========================

avg_monthly = (
    df["MonthlyCharges"].mean()
)

print("\nAverage Monthly Charge:")
print(round(avg_monthly, 2))

# =========================
# CONTRACT ANALYSIS
# =========================

print("\nContract Distribution:\n")

print(
    df["Contract"]
    .value_counts()
)

# =========================
# INTERNET SERVICE ANALYSIS
# =========================

print("\nInternet Service Distribution:\n")

print(
    df["InternetService"]
    .value_counts()
)

# =========================
# CHURN BY CONTRACT
# =========================

print("\nChurn By Contract:\n")

print(
    df.groupby("Contract")["Churn"]
    .mean()
)

# =========================
# TOP REVENUE CUSTOMERS
# =========================

top_customers = df.sort_values(
    by="MonthlyCharges",
    ascending=False
)

print("\nTop Revenue Customers:\n")

print(
    top_customers[
        [
            "customerID",
            "MonthlyCharges",
            "Contract"
        ]
    ].head(10)
)