import pandas as pd

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print(df.head())

# =========================
# CLEAN TOTAL CHARGES
# =========================

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df.dropna(inplace=True)

# =========================
# ENCODE TARGET
# =========================

df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

# =========================
# SAVE CLEAN DATA
# =========================

df.to_csv(
    "data/processed/cleaned_churn.csv",
    index=False
)

print("Data Cleaning Completed")