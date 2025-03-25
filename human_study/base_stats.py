import pandas as pd
from openpyxl import load_workbook

####################
# Results Analysis #
####################

# Load the data from the provided Excel files
file_0_path = 'results_enhanced_text.xlsx'
file_1_path = 'results_original_text.xlsx'

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

####################
# Save results     #
####################

# Put results in a xlxs file
results = {
    'Original Mean': original_mean_stats,
    'Enhanced Mean': enhanced_mean_stats,
    'Original Standard Deviation': original_std_stats,
    'Enhanced Standard Deviation': enhanced_std_stats
}

df = pd.DataFrame(results, index=['Total', 'Pre-text', 'Post-text'])
excel_path = 'base_stats.xlsx'
df.to_excel(excel_path, index=True)

########################
# Adjust column widths #
########################
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