import pandas as pd
from scipy.stats import ttest_ind
import re

# Load the data from the provided Excel files
file_0_path = 'data_0.xlsx'
file_1_path = 'data_1.xlsx'

data_0 = pd.read_excel(file_0_path)
data_1 = pd.read_excel(file_1_path)

# Function to extract numerical values from the "Total score" column
def extract_score(score_str):
    match = re.match(r"(\d+)", str(score_str))
    return int(match.group(1)) if match else None

# Apply extraction to the relevant columns in both datasets
data_0['Total score'] = data_0['Total score'].apply(extract_score) / 15
data_0['Total Before Score'] = pd.to_numeric(data_0['Total Before Score'], errors='coerce') / 5
data_0['Total After Score'] = pd.to_numeric(data_0['Total After Score'], errors='coerce') / 10

data_1['Total score'] = data_1['Total score'].apply(extract_score) / 15
data_1['Total Before Score'] = pd.to_numeric(data_1['Total Before Score'], errors='coerce') / 5
data_1['Total After Score'] = pd.to_numeric(data_1['Total After Score'], errors='coerce') / 10

# Extract the scores for analysis
enhanced_total_scores = data_0['Total score'].dropna()
original_total_scores = data_1['Total score'].dropna()

enhanced_before_scores = data_0['Total Before Score'].dropna()
original_before_scores = data_1['Total Before Score'].dropna()

enhanced_after_scores = data_0['Total After Score'].dropna()
original_after_scores = data_1['Total After Score'].dropna()

# Perform independent t-tests
t_total, p_total = ttest_ind(enhanced_total_scores, original_total_scores, equal_var=False)
t_before, p_before = ttest_ind(enhanced_before_scores, original_before_scores, equal_var=False)
t_after, p_after = ttest_ind(enhanced_after_scores, original_after_scores, equal_var=False)

# Display the results
res ={
    "Total Score Comparison": {"t-statistic": t_total, "p-value": p_total},
    "Before Score Comparison": {"t-statistic": t_before, "p-value": p_before},
    "After Score Comparison": {"t-statistic": t_after, "p-value": p_after}
}

print(res)
