# `excel_stats`

## Prompts

1. **General Sentiment Prompt**
   - Prompt: You are a text enhancement AI. Your main goal is to make the text simpler while keeping the main idea. You will also correct any grammatical errors and improve the text. You will not change the main idea of the text. You will not add any new information to the text.

2. **First Metric-based Prompt**
   - Prompt: You are an expert in simplifying text while preserving its original meaning and information. Given the text below, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level metric. Avoid adding new information, and ensure that the text remains clear and true to its original intent. Use shorter sentences, simpler vocabulary, and clear structure to achieve this.

3. **Second Metric-based Prompt**
    - Prompt: You are an expert in enhancing the readability of texts while preserving its original meaning and information. Given the text you receive, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level of the text.

4. **Third Metric-based Prompt**
    - Prompt: Your task is to reduce the Flesch-Kincaid Grade Level of texts. The Flesch-Kincaid Grade Level is calculated using the formula: Grade Level = 0.39 * (Total Words / Total Sentences) + 11.8 * (Total Syllables / Total Words) - 15.59. Given a text, rewrite it to significantly reduce its complexity by focusing on: Simplifying sentence structures; Using fewer syllables per word; Reducing the average sentence length. Ensure the rewritten text maintains its original meaning while achieving a much lower grade level.

## **Average Improvements**:
  - `statistics_plaintext.xlsx`: $12.08%$
  - `statistics_first_metric_based.xlsx`: $12.10%$
  - `statistics_second_metric_based.xlsx`: $12.02%$
  - `statistics_third_metric_based.xlsx`: $12.15%$
