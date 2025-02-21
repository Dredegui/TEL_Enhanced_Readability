import pandas as pd
from scipy.stats import ttest_ind
from scipy import stats
import numpy as np
import re
from openpyxl import load_workbook

# Load the data from the provided Excel files
file_0_path = 'enhanced_text_results.xlsx'
file_1_path = 'original_text_results.xlsx'

data_0 = pd.read_excel(file_0_path)
data_1 = pd.read_excel(file_1_path)

# Function to extract numerical values from the "Total score" column
def extract_score(score_str):
    match = re.match(r"(\d+)", str(score_str))
    return int(match.group(1)) if match else None

# Apply extraction to the relevant columns in both datasets
data_0['Total score'] = data_0['Total score'].apply(extract_score) / 15
data_1['Total score'] = data_1['Total score'].apply(extract_score) / 15

# Extract the scores for analysis
enhanced_total_scores = data_0['Total score'].dropna()
original_total_scores = data_1['Total score'].dropna()

enhanced_pre_text_scores = data_0['Pre-text Score %'].dropna()
original_pre_text_scores = data_1['Pre-text Score %'].dropna()

enhanced_post_text_scores = data_0['Post-text Score %'].dropna()
original_post_text_scores = data_1['Post-text Score %'].dropna()

# Calculate the mean and standard deviation for each set of scores
mean_pre_text = enhanced_pre_text_scores.mean()
mean_post_text = enhanced_post_text_scores.mean()

std_pre_text = enhanced_pre_text_scores.std()
std_post_text = enhanced_post_text_scores.std()

print("Normality test for enhanced_pre_text_scores:", stats.shapiro(enhanced_pre_text_scores))
print("Normality test for original_pre_text_scores:", stats.shapiro(original_pre_text_scores))

print("Normality test for enhanced_post-text_scores:", stats.shapiro(enhanced_post_text_scores))
print("Normality test for original_post-text_scores:", stats.shapiro(original_post_text_scores))

# Perform independent t-tests
t_total, p_total = ttest_ind(enhanced_total_scores, original_total_scores, equal_var=False)
t_pre_text, p_pre_text = ttest_ind(enhanced_pre_text_scores, original_pre_text_scores, equal_var=False)
t_post_text, p_post_text = ttest_ind(enhanced_post_text_scores, original_post_text_scores, equal_var=False)

# Put results in a xlxs file
results = {
    'ttest total t-value': t_total,
    'ttest total p-value': p_total,
    'ttest pre-text t-value': t_pre_text,
    'ttest pre-text p-value': p_pre_text,
    'ttest post-text t-value': t_post_text,
    'ttest post-text p-value': p_post_text,
    'mean pre-text': mean_pre_text,
    'mean post-text': mean_post_text,
    'std pre-text': std_pre_text,
    'std post-text': std_post_text
}

df = pd.DataFrame(results, index=[0])
excel_path = 'ttest_results.xlsx'
df.to_excel(excel_path, index=False)

# Adjust column widths
wb = load_workbook(excel_path)
ws = wb.active

for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  # Get the column name
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

wb.save(excel_path)

print("Data processing complete. Files saved as enhanced_text_results.xlsx and original_text_results.xlsx.")