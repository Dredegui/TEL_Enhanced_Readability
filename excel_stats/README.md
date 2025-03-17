# Folder Overview: `excel_stats`

## Prompts

1. **General Sentiment Prompt**
   - Prompt: You are a text enhancement AI. Your main goal is to make the text simpler while keeping the main idea. You will also correct any grammatical errors and improve the text. You will not change the main idea of the text. You will not add any new information to the text.

2. **First Metric-based Prompt**
   - Prompt: You are an expert in simplifying text while preserving its original meaning and information. Given the text below, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level metric. Avoid adding new information, and ensure that the text remains clear and true to its original intent. Use shorter sentences, simpler vocabulary, and clear structure to achieve this.

3. **Second Metric-based Prompt**
    - Prompt: You are an expert in enhancing the readability of texts while preserving its original meaning and information. Given the text you receive, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level of the text.

4. **Third Metric-based Prompt**
    - Prompt: Your task is to reduce the Flesch-Kincaid Grade Level of texts. The Flesch-Kincaid Grade Level is calculated using the formula: Grade Level = 0.39 * (Total Words / Total Sentences) + 11.8 * (Total Syllables / Total Words) - 15.59. Given a text, rewrite it to significantly reduce its complexity by focusing on: Simplifying sentence structures; Using fewer syllables per word; Reducing the average sentence length. Ensure the rewritten text maintains its original meaning while achieving a much lower grade level.

## Results/Folder Contents

1. **`statistics_general_sentiment.xlsx`**
   - Description: Contains the raw statistics for the general sentiment prompt.
   - Average Improvement: 13.2000

2. **`statistics_general_sentiment_cleaned.xlsx`**
   - Description: A cleaned version of the statistics related to the general sentiment prompt. (Removed artifacts)
   - Average Improvement: 13.1597

3. **`statistics_first_metric_prompt.xlsx`**
   - Description: Contains data related to the first metric prompt based on general sentiment.
   - Average Improvement: 13.4300 (Has simplification we don't want this)

4. **`statistics_second_metric_prompt.xlsx`**
   - Description: Contains data related to the second metric-based prompt.
   - Average Improvement: 13.3900

5. **`statistics_third_metric_prompt.xlsx`**
   - Description: Contains data related to the third metric-based prompt.
   - Average Improvement: 13.4300

6. **`statistics_third_metric_prompt_cleaned.xlsx`**
   - Description: A cleaned version of the statistics for the third metric-based prompt. (Removed artifacts)
   - Average Improvement: 13.3946

## Conclusion

The data indicates a consistent pattern of improvement across different prompts, with average improvements ranging between 13.15 and 13.43. This suggests a notable performance enhancement across all the prompts analyzed. This testing via this readability metric were purely to be used as an initial indicator of which prompt to use for the study.

Results would be more conclusive if the readability metric was tested on a larger dataset.
