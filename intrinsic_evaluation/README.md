# `intrinsic_evaluation`

This folder contains scripts and resources for processing datasets, cleaning LaTeX documents, and generating statistics related to intrinsic evaluations of text readability. Below is an explanation of each file and folder in this directory.

## Files and Folders

### 1. `clean_latex.py`
- **Purpose**: Contains functions to clean and process LaTeX documents by removing LaTeX commands, environments, and inline/display math.
- **Key Functions**:
  - `remove_latex_commands`: Removes LaTeX-specific syntax and commands.
  - `extract_old`: Extracts specific sections (e.g., Introduction) from LaTeX documents.
  - `split`: Splits text based on specified start and end markers.

### 2. `dataset_clean.py`
- **Purpose**: Processes raw datasets, cleans LaTeX content, and saves the cleaned results into an Excel file.
- **Key Functions**:
  - `save_results`: Saves processed papers and their cleaned text into an Excel file (`cleaned_input_test.xlsx`).
  - `process_chunks`: Processes chunks of data from the dataset, cleans LaTeX content, and filters based on text length.
  - `main`: Entry point for processing the dataset located in the `AAPR_Dataset` directory.

### 3. `dataset_process.py`
- **Purpose**: Processes text data using various system prompts and saves the results into Excel files for further analysis.
- **Key Functions**:
  - `process`: Sends text data to a text enhancement AI using specified prompts and saves the results.
  - `main`: Entry point for processing the dataset in `excel_stats/input.xlsx` using four different prompts and saving results to:
    - `excel_stats/statistics_plaintext.xlsx`
    - `excel_stats/statistics_first_metric_based.xlsx`
    - `excel_stats/statistics_second_metric_based.xlsx`
    - `excel_stats/statistics_third_metric_based.xlsx`

### 4. `stats.py`
- **Purpose**: Analyzes and visualizes the readability statistics from the generated Excel files.
- **Key Functions**:
  - `view_statistics`: Calculates and prints the average improvement in readability.
  - `graph_readability`: Plots the percentage improvement in readability.
  - `graph_readability_categories`: Categorizes and visualizes performance clusters based on readability improvement.

### 5. `api.env`
- **Purpose**: Environment file containing configuration variables such as `DIR_PATH` and `API_KEY` for accessing datasets and APIs.

### 6. `excel_stats/`
- **Purpose**: Contains the input dataset and the results of the intrinsic evaluation.
- **Files**:
  - `input.xlsx`: The raw text data used for intrinsic evaluation. This file is processed by `dataset_process.py`.
  - `statistics_plaintext.xlsx`: Results of processing the dataset with a general text enhancement prompt.
  - `statistics_first_metric_based.xlsx`: Results of processing the dataset with the first metric-based prompt.
  - `statistics_second_metric_based.xlsx`: Results of processing the dataset with the second metric-based prompt.
  - `statistics_third_metric_based.xlsx`: Results of processing the dataset with the third metric-based prompt.

### 7. `__pycache__/`
- **Purpose**: Contains cached Python files for faster execution. This folder is automatically generated and can be ignored.

## Results

- **Excel Files with Results**: The processed results from the intrinsic evaluation are stored in the `excel_stats` folder. You can also download them from the following link:
  [Download Results](https://drive.google.com/file/d/1QT_9MwBEHgfvzXbYBvtCxmrSjOTucf0C/view?usp=sharing)

- **Average Improvements**:
  - `statistics_plaintext.xlsx`: **12.08%**
  - `statistics_first_metric_based.xlsx`: **12.10%**
  - `statistics_second_metric_based.xlsx`: **12.02%**
  - `statistics_third_metric_based.xlsx`: **12.15%**

## Usage

1. **Clean LaTeX Documents**: Use `clean_latex.py` to preprocess LaTeX documents and extract relevant sections.
2. **Process Datasets**: Run `dataset_clean.py` to clean and filter datasets, or use `dataset_process.py` to process text with AI prompts.
3. **Analyze Results**: Use `stats.py` to analyze and visualize the readability improvements from the processed results.

## Notes

- Ensure that the `api.env` file is correctly configured with the required paths and API keys before running the scripts.
- The processed results are saved in the `excel_stats` folder for further analysis and visualization.
