# Medical Data Warehouse Scripts

This repository contains Python scripts for populating a PostgreSQL database with medical data, scraping data from Telegram channels, and utility functions for data analysis.

## Table of Contents

- [Installation](#installation)
- [Scripts](#scripts)
  - [populate_database.py](#populate_databasepy)
  - [telegram_scrapper.py](#telegram_scrapperpy)
  - [utils.py](#utils)
- [Usage](#usage)
- [License](#license)

## Installation

To run these scripts, ensure you have Python installed along with the necessary packages. You can install the required packages using pip:

```bash
pip install psycopg2 telethon python-dotenv pandas
```

Additionally, make sure you have PostgreSQL installed and running.

## Scripts

### populate_database.py

This script connects to a PostgreSQL database and creates two tables: `photos` and `yolo_detections`. It then populates these tables with image data and YOLO detection results.

- **Database Configuration**: Update the database credentials in the script to match your PostgreSQL setup.
- **Directories**: Ensure the paths for the `photos` and `detection_results` folders are correctly set.

**How it works**:

1. Connects to the PostgreSQL database.
2. Creates the `photos` and `yolo_detections` tables if they do not exist.
3. Reads images from the specified `photos` directory and inserts them into the `photos` table.
4. For each image, it looks for corresponding YOLO detection results in CSV format and inserts those into the `yolo_detections` table.

### telegram_scrapper.py

This script uses the Telethon library to scrape photos and messages from specified Telegram channels.

- **Environment Variables**: The script relies on environment variables defined in a `.env` file, including `TG_API_ID`, `TG_API_HASH`, and `phone`.
- **Directories**: Creates a directory for scrapped data and logs.

**How it works**:

1. Initializes the Telegram client with provided API credentials.
2. Scrapes photos and messages from specified channels.
3. Saves photos in the designated directory and logs the activity.
4. Writes scraped messages into CSV files for easy access.

### utils.py

This module contains utility functions for data analysis, specifically for handling missing values and generating column summaries from pandas DataFrames.

- **Functions**:
  - `missing_values_table(df)`: Returns a DataFrame summarizing missing values in the input DataFrame.
  - `column_summary(df)`: Generates a summary of the columns in the DataFrame, including data types, number of nulls, and distinct values.

## Usage

1. Ensure PostgreSQL is running and your database is set up.
2. Update the necessary file paths and database credentials in `populate_database.py`.
3. Create a `.env` file with your Telegram API credentials for `telegram_scrapper.py`.
4. Run the scripts as needed:

```bash
python populate_database.py
python telegram_scrapper.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Notes:

- Make sure to adapt paths and installation instructions based on your specific setup and requirements.
- Consider adding examples of how to run the scripts with command-line arguments if applicable.
- You may want to include error handling or troubleshooting sections based on common issues users might encounter.
```
