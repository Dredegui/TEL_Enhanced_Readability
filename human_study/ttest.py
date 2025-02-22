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

# Extract the scores for analysis
enhanced_total_scores = data_0['Total score %'].dropna()
original_total_scores = data_1['Total score %'].dropna()

enhanced_pre_text_scores = data_0['Pre-text score %'].dropna()
original_pre_text_scores = data_1['Pre-text score %'].dropna()

enhanced_post_text_scores = data_0['Post-text score %'].dropna()
original_post_text_scores = data_1['Post-text score %'].dropna()

# Calculate the mean and standard deviation for each set of scores
enhanced_mean_stats = [enhanced_total_scores.mean(), enhanced_pre_text_scores.mean(), enhanced_post_text_scores.mean()]
original_mean_stats = [original_total_scores.mean(), original_pre_text_scores.mean(), original_post_text_scores.mean()]
enhanced_std_stats = [enhanced_total_scores.std(), enhanced_pre_text_scores.std(), enhanced_post_text_scores.std()]
original_std_stats = [original_total_scores.std(), original_pre_text_scores.std(), original_post_text_scores.std()]



print("Normality test for enhanced_pre_text_scores:", stats.shapiro(enhanced_pre_text_scores))
print("Normality test for original_pre_text_scores:", stats.shapiro(original_pre_text_scores))
print("Normality test for enhanced_post-text_scores:", stats.shapiro(enhanced_post_text_scores))
print("Normality test for original_post-text_scores:", stats.shapiro(original_post_text_scores))
print("Normality test for enhanced_total_scores:", stats.shapiro(enhanced_total_scores))
print("Normality test for original_total_scores:", stats.shapiro(original_total_scores))

# Perform independent t-tests
t_total, p_total = ttest_ind(enhanced_total_scores, original_total_scores, equal_var=False)
t_pre_text, p_pre_text = ttest_ind(enhanced_pre_text_scores, original_pre_text_scores, equal_var=False)
t_post_text, p_post_text = ttest_ind(enhanced_post_text_scores, original_post_text_scores, equal_var=False)

t_stats = [t_total, t_pre_text, t_post_text]
p_stats = [p_total, p_pre_text, p_post_text]

# Put results in a xlxs file
results = {
    'Original Mean': original_mean_stats,
    'Enhanced Mean': enhanced_mean_stats,
    'Original Standard Deviation': original_std_stats,
    'Enhanced Standard Deviation': enhanced_std_stats,
    'T-Statistic': t_stats,
    'P-Value': p_stats
}

df = pd.DataFrame(results, index=['Total', 'Pre-text', 'Post-text'])
excel_path = 'ttest_results.xlsx'
df.to_excel(excel_path, index=True)

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