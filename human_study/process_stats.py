import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
file_path = 'original_answers.csv'
data = pd.read_csv(file_path)

# Identify columns for "before" and "after" test scores
choose_number_index = data.columns.get_loc('Choose a number')

before_columns = [
    col for col in data.columns[:choose_number_index] if "[Score]" in col
]
after_columns = [
    col for col in data.columns[choose_number_index + 1:] if "[Score]" in col
]

# Extract numeric scores for evaluation
def extract_score(score_str):
    try:
        return float(score_str.split(' / ')[0])
    except:
        return None

# Apply extraction to before and after scores
data['Total Before Score'] = data[before_columns].applymap(extract_score).sum(axis=1)
data['Total After Score'] = data[after_columns].applymap(extract_score).sum(axis=1)

# Move Total Before Score and Total After Score after Total Score column
if 'Total score' in data.columns:
    score_index = data.columns.get_loc('Total score')
    columns_order = (
        list(data.columns[:score_index + 1]) +
        ['Total Before Score', 'Total After Score'] +
        list(data.columns[score_index + 1:].drop(['Total Before Score', 'Total After Score']))
    )
    data = data[columns_order]


# Split data based on "Choose a number"
data_0 = data[data['Choose a number'] == 0]
data_1 = data[data['Choose a number'] == 1]

# Save to separate Excel files
data_0.to_excel('data_0.xlsx', index=False)
data_1.to_excel('data_1.xlsx', index=False)

print("Data processing complete. Files saved as data_0.xlsx and data_1.xlsx.")
