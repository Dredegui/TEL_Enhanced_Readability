import pandas as pd

# Load the datasets
text_0_file = 'data_0.xlsx'
text_1_file = 'data_1.xlsx'

text_0_data = pd.read_excel(text_0_file)
text_1_data = pd.read_excel(text_1_file)

# Assume the data has columns for readability and scores ('Readability', 'Total Before Score', 'Total After Score')

# Calculate readability scores
readability_0 = text_0_data['How was the readability of the text?'].mean()
readability_1 = text_1_data['How was the readability of the text?'].mean()

# Calculate Understandability scores
understandability_0 = text_0_data['How understandable was the content of text?'].mean()
understandability_1 = text_1_data['How understandable was the content of text?'].mean()


# Calculate statistics for "Did you feel some content was missing?"
missing_content_0 = text_0_data['Did you feel the some content was missing?'].value_counts(normalize=True)
missing_content_1 = text_1_data['Did you feel the some content was missing?'].value_counts(normalize=True)


# Calculate total scores (total scores)
scores_0 = (text_0_data['Total After Score'] + text_0_data['Total Before Score']).mean()
scores_1 = (text_1_data['Total After Score'] + text_1_data['Total Before Score']).mean()

# Calculate comprehension scores (pre-knowledge scores)
pre_scores_0 = (text_0_data['Total Before Score']).mean()
pre_scores_1 = (text_1_data['Total Before Score']).mean()

# Calculate comprehension scores (post-knowledge scores)
post_scores_0 = (text_0_data['Total After Score']).mean()
post_scores_1 = (text_1_data['Total After Score']).mean()

# Compare results
results = {
    'Text 0 Readability': readability_0,
    'Text 1 Readability': readability_1,
    'Text 0 Understandability': understandability_0,
    'Text 1 Understandability': understandability_1,
    'Text 0 Pre-Knowledge Scores': pre_scores_0,
    'Text 1 Pre-Knowledge Scores': pre_scores_1,
    'Text 0 Post-Knowledge Scores': post_scores_0,
    'Text 1 Post-Knowledge Scores': post_scores_1,
    'Text 0 Scores': scores_0,
    'Text 1 Scores': scores_1,
    'Better Readability': 'Text 0' if readability_0 > readability_1 else 'Text 1',
    'Better Scores': 'Text 0' if scores_0 > scores_1 else 'Text 1',
    'Text 0 Missing Content': missing_content_0.to_dict(),
    'Text 1 Missing Content': missing_content_1.to_dict()
}


# Output results
for key, value in results.items():
    print(f"{key}: {value}")