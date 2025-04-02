# TEL Enhanced Readability

This project was developed for **Technology Enhanced Learning (TEL)** at **KTH Royal Institute of Technology**. It later evolved into a research paper co-authored by:  

- **Marlinde van den Bosch**  
- **Olga Viberg**  
- **Carrie Demmans Epp**  

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Intrinsic Evaluation](#intrinsic-evaluation)
- [Second Study](#second-study)
- [Data Visualizations](#data-visualizations)
- [License](#license)

## Overview

This project aims to enhance readability through technology, specifically focusing on tools and methods to improve text presentation and comprehension.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

To start the server, run:

```bash
python server.py
```

## Project Structure

- `server.py`: The main server script that handles incoming requests and serves the application.
- `requirements.txt`: A list of dependencies needed to run the project.
- `static/`: Directory containing static files such as CSS, JavaScript, and images.
- `templates/`: Directory containing HTML templates for the web pages.
- `human_study/`: Directory containing files related to the human study conducted as part of this project.
  - `study_answers.csv`: CSV file containing answers from the study participants.
  - `enhanced_text_results.xlsx`: Results related to the enhanced text in the study.
  - `original_text_results.xlsx`: Results related to the original text in the study.
  - `process_stats.py`: Script for processing the statistics of the study.
  - `statistics.xlsx`: Excel file containing statistical analysis.
  - `knowledgeTest.csv`: CSV file containing knowledge test results.
  - `study_text_readability.xlsx`: Excel file related to the readability analysis of the texts.
- `graph_stats/`: Directory containing visualizations of the data from the studies.
- `intrinsic_evaluation/`: Directory containing scripts and resources for processing datasets, cleaning LaTeX documents, and generating statistics related to intrinsic evaluations of text readability.
  - `clean_latex.py`: Contains functions to clean and process LaTeX documents by removing LaTeX commands, environments, and inline/display math.
  - `dataset_clean.py`: Processes raw datasets, cleans LaTeX content, and saves the cleaned results into an Excel file.
  - `dataset_process.py`: Processes text data using various system prompts and saves the results into Excel files for further analysis.
  - `stats.py`: Analyzes and visualizes the readability statistics from the generated Excel files.
  - `api.env`: Environment file containing configuration variables such as `DIR_PATH` and `API_KEY` for accessing datasets and APIs.
  - `excel_stats/`: Contains the input dataset and the results of the intrinsic evaluation.
    - `input.xlsx`: The raw text data used for intrinsic evaluation. This file is processed by `dataset_process.py`.
    - `statistics_plaintext.xlsx`: Results of processing the dataset with a general text enhancement prompt.
    - `statistics_first_metric_based.xlsx`: Results of processing the dataset with the first metric-based prompt.
    - `statistics_second_metric_based.xlsx`: Results of processing the dataset with the second metric-based prompt.
    - `statistics_third_metric_based.xlsx`: Results of processing the dataset with the third metric-based prompt.
- `README.md`: This file, providing an overview and instructions for the project.

## Intrinsic Evaluation

The first study conducted as part of this project was a comparison of readability according to the Flesch-Kincaid grade level metric. The study used four different prompts: three metric-based and one general.
The `intrinsic_evaluation` directory contains scripts and resources for processing datasets, cleaning LaTeX documents, and generating statistics related these intrinsic evaluations of text readability.

### Usage

1. **Clean LaTeX Documents**: Use `clean_latex.py` to preprocess LaTeX documents and extract relevant sections.
2. **Process Datasets**: Run `dataset_clean.py` to clean and filter datasets, or use `dataset_process.py` to process text with AI prompts.
3. **Analyze Results**: Use `stats.py` to analyze and visualize the readability improvements from the processed results.

To clean and generate random samples yourself with the same dataset go to [AAPR Dataset - Github](https://github.com/lancopku/AAPR) or [PapersWithCode](https://paperswithcode.com/dataset/arxiv-academic-paper-dataset)

### Results

- **Excel Files with Results**: The processed results from the intrinsic evaluation are stored in the `excel_stats` folder. You can also download them from the following link:
  [Download Results](https://drive.google.com/file/d/1QT_9MwBEHgfvzXbYBvtCxmrSjOTucf0C/view?usp=sharing)

- **Average Improvements**:
  - `statistics_plaintext.xlsx`: **12.08%**
  - `statistics_first_metric_based.xlsx`: **12.10%**
  - `statistics_second_metric_based.xlsx`: **12.02%**
  - `statistics_third_metric_based.xlsx`: **12.15%**


## Second Study

The group study was the second study conducted as part of this project. It involved distributing a Google Forms survey that contained both original and simplified texts. Participants were asked to read and evaluate the texts.

The `human_study` directory contains various files related to this study, including raw data, statistical analysis scripts, and results. Key files are:
- `study_answers.csv`
- `enhanced_text_results.xlsx`
- `original_text_results.xlsx`
- `process_stats.py`
- `statistics.xlsx`
- `knowledgeTest.csv`

## Data Visualizations

All visualizations for the data from the studies are located in the `graph_stats` directory. This directory contains various files and scripts that generate graphs and charts to help visualize the study results.

## License

This project is still under consideration for a license.
