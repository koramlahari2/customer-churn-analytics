import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "data/processed/cleaned_churn.csv"
)

# =====================================
# SELECT FEATURES
# =====================================

features = [
    "tenure",
    "MonthlyCharges",
    "Contract",
    "InternetService"
]

X = df[features]

y = df["Churn"]

# =====================================
# ENCODE CATEGORICAL COLUMNS
# =====================================

label_encoders = {}

for column in [
    "Contract",
    "InternetService"
]:

    le = LabelEncoder()

    X[column] = le.fit_transform(
        X[column]
    )

    label_encoders[column] = le

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# TRAIN MODEL
# =====================================

model = RandomForestClassifier()

model.fit(
    X_train,
    y_train
)

# =====================================
# PREDICTIONS
# =====================================

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nMODEL ACCURACY:")
print(round(accuracy * 100, 2), "%")

# =====================================
# SAVE MODEL
# =====================================

joblib.dump(
    model,
    "models/churn_model.pkl"
)

joblib.dump(
    label_encoders,
    "models/label_encoders.pkl"
)

print("\nMODEL SAVED")