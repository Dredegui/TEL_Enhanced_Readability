import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
file_path = 'original_answers.csv'
data = pd.read_csv(file_path)

# Identify columns for "before" and "after" test scores
choose_number_index = data.columns.get_loc('Choose a number')

pre_text_columns = [
    col for col in data.columns[:choose_number_index] if "[Score]" in col
]
post_text_columns = [
    col for col in data.columns[choose_number_index + 1:] if "[Score]" in col
]

# Extract numeric scores for evaluation
def extract_score(score_str):
    try:
        return float(score_str.split(' / ')[0])
    except:
        return None
    
def sum_percentage(row):
    cleaned_row = row.dropna()
    return round(cleaned_row.sum() / len(cleaned_row) * 100)

def calculate(element):
    # element = x / 15
    x = element.split(' / ')[0]
    return round(float(x) / 15 * 100)    


# Apply extraction to before and after scores
data['Pre-text score %'] = data[pre_text_columns].map(extract_score).apply(sum_percentage, axis=1)
data['Post-text score %'] = data[post_text_columns].map(extract_score).apply(sum_percentage, axis=1)

# Total score calculation
data["Total score"] = data["Total score"].map(calculate)

# Move Total Pre-text Score and Total Post-text Score after Total Score column
if 'Total score' in data.columns:
    score_index = data.columns.get_loc('Total score')
    # Change name of Total Score column
    data.rename(columns={'Total score': 'Total score %'},
                inplace=True)
    columns_order = (
        list(data.columns[:score_index + 1]) +
        ['Pre-text Score %', 'Post-text Score %'] +
        list(data.columns[score_index + 1:].drop(['Pre-text Score %', 'Post-text Score %']))
    )
    data = data[columns_order]


# Split data based on "Choose a number"
data_0 = data[data['Choose a number'] == 0]
data_1 = data[data['Choose a number'] == 1]

# Save to separate Excel files
data_0.to_excel('enhanced_text_results.xlsx', index=False)
data_1.to_excel('original_text_results.xlsx', index=False)

print("Data processing complete. Files saved as enhanced_text_results.xlsx and original_text_results.xlsx.")
