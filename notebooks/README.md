

# Data Processing and Object Detection Notebooks

This repository contains Jupyter notebooks for data processing and object detection tasks related to Ethiopian medical business data. The two main notebooks included are:

1. **data cleaning.ipynb**: This notebook is designed to clean and preprocess CSV files containing scrapped data.
2. **YOLLO.ipynb**: This notebook performs object detection on images using the YOLOv5 model.

## Table of Contents

- [Prerequisites](#prerequisites)
- [File Structure](#file-structure)
- [data cleaning.ipynb](#data-cleaningipynb)
- [YOLLO.ipynb](#yolloipynb)
- [License](#license)

## Prerequisites

To run these notebooks, ensure you have the following installed:

- **Python 3.8+**
- **Jupyter Notebook** or **Jupyter Lab**
- Required libraries:
  - `pandas`
  - `torch`
  - `opencv-python`
  - `emoji`

You can install the necessary libraries using pip:
```bash
pip install pandas torch opencv-python emoji
```

## File Structure

```bash
notebooks/
├── data cleaning.ipynb  # Notebook for data cleaning and preprocessing
└── YOLLO.ipynb          # Notebook for object detection using YOLOv5
scripts/
├── utils.py              # Utility functions for data processing (if applicable)
data/
└── scrapped_data/       # Directory containing raw CSV files and processed data
```

## data cleaning.ipynb

The `data cleaning.ipynb` notebook performs the following tasks:

1. **Data Loading**: Loads multiple CSV files from the `data/scrapped_data/` directory and merges them into a single DataFrame.
2. **Missing Values Handling**: Checks for and drops rows with missing values.
3. **Duplicate Handling**: Identifies and displays duplicated rows.
4. **Data Type Conversion**: Converts specific columns to the appropriate data types, such as string and datetime.
5. **Data Validation**: Removes emojis from the 'Message' column using the `emoji` library.
6. **Saving Cleaned Data**: Saves the cleaned DataFrame to a new CSV file.

### Key Functions
- `missing_values_table(df)`: Displays a table of missing values in the DataFrame.
- `column_summary(df)`: Provides a summary of the DataFrame's columns.

## YOLLO.ipynb

The `YOLLO.ipynb` notebook implements the following steps:

1. **YOLOv5 Installation**: Clones the YOLOv5 repository and installs the required dependencies.
2. **Model Loading**: Loads a pre-trained YOLOv5 model for object detection.
3. **Object Detection**: Loops through images in a specified folder and applies the YOLOv5 model to detect objects.
4. **Results Saving**: Saves detection results (bounding boxes, class labels, and confidence scores) to CSV files in the `detection_results/` directory.
5. **Zip Results**: Zips the results folder for easy download.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

Feel free to adjust any sections or add more details as needed!
