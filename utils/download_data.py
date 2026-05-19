import kagglehub
import shutil
import os

# ==================================
# DOWNLOAD DATASET
# ==================================

path = kagglehub.dataset_download(
    "blastchar/telco-customer-churn"
)

print("Dataset Downloaded")

# ==================================
# COPY CSV TO PROJECT
# ==================================

source_file = os.path.join(
    path,
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

destination = (
    "data/raw/"
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

shutil.copy(
    source_file,
    destination
)

print("CSV Copied Successfully")