# TEL Enhanced Readability

Project for TEL (Technology Enhanced Readability) on KTH.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [First Study](#first-study)
- [Second Study](#second-study)
- [Data Visualizations](#data-visualizations)
- [Contributing](#contributing)
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
- `excel_stats/`: Directory containing files related to the first study on readability comparison.
- `graph_stats/`: Directory containing visualizations of the data from the studies.
- `README.md`: This file, providing an overview and instructions for the project.

## First Study

The first study conducted as part of this project was a comparison of readability according to the Flesch-Kincaid grade level metric. The study used four different prompts: three metric-based and one plain text. The results of this study are contained in the `excel_stats` directory, read its [README](https://github.com/Dredegui/TEL_Enhanced_Readability/tree/main/excel_stats) for more information.

## Second Study

The group study was the second study conducted as part of this project. It involved distributing a Google Forms survey that contained both original and simplified texts. Participants were asked to read these texts and then answer questions designed to assess their comprehension and performance. Additionally, participants provided their opinions regarding the ease of readability for both the original and simplified texts. This study aimed to compare the performance outcomes and subjective readability between the two versions of the texts.

The `human_study` directory contains various files related to this study, including raw data, statistical analysis scripts, and results. Key files are:
- `study_answers.csv`
- `enhanced_text_results.xlsx`
- `original_text_results.xlsx`
- `process_stats.py`
- `statistics.xlsx`
- `knowledgeTest.csv`

## Data Visualizations

All visualizations for the data from the studies are located in the `graph_stats` directory. This directory contains various files and scripts that generate graphs and charts to help visualize the study data.

## License

This project is still under consideration for a license
