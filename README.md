# CSV Data Analyzer

The CSV Data Analyzer is a Streamlit application that allows users to upload a CSV file and quickly explore and analyze its data. It provides an overview of the dataset, summary statistics, visualizations, and custom filtering options to help users perform basic exploratory data analysis (EDA) with ease.

---

## Features

1. **File Upload**: Upload a CSV file to analyze its contents.
2. **Data Overview**:
   - Displays the first few rows of the dataset.
   - Shows the dataset shape (number of rows and columns).
   - Lists all column names.
3. **Summary Statistics**: Provides key metrics (mean, median, min, max, etc.) for numerical columns.
4. **Null Value Analysis**: Shows the count and percentage of missing values for each column.
5. **Visualizations**:
   - Histogram for numerical columns.
   - Pie chart for categorical columns.
6. **Custom Query**: Filter the dataset using custom queries (e.g., `Age > 30 & Gender == 'Male'`).

---

## Try the Application

Access the live application here: [CSV Data Analyzer](https://csv-viewer-ahmddbilall.streamlit.app/)

---

## How to Use

1. Open the application using the [deployed link](https://csv-viewer-ahmddbilall.streamlit.app/).
2. Upload a CSV file by clicking on the file uploader.
3. Explore the dataset with the following features:
   - **Dataset Overview**: View the shape, column names, and first few rows.
   - **Summary Statistics**: Get detailed statistics for numerical columns.
   - **Visualizations**: Select columns to view histograms or pie charts.
   - **Custom Query**: Enter a query to filter the data and view the results.

---

## Example

### Input:
Upload a CSV file containing data like:
| Name   | Age | Gender | Income  |
|--------|-----|--------|---------|
| Alice  | 25  | Female | 50000   |
| Bob    | 30  | Male   | 60000   |
| Charlie| 35  | Male   | 70000   |

### Output:
1. **Dataset Overview**:
   - Shape: `(3, 4)`
   - Columns: `['Name', 'Age', 'Gender', 'Income']`
   - First 5 rows: Displays the above table.
   
2. **Summary Statistics**:
   - Numerical data like `Age` and `Income` show mean, median, etc.

3. **Visualizations**:
   - Histogram for `Age`.
   - Pie chart for `Gender`.

4. **Custom Query**:
   - Query: `Age > 25 & Gender == 'Male'`
   - Output: Data filtered to show rows for Bob and Charlie.

---

## Run Locally

1. Clone the repository or download the `csv_analyzer.py` file.
2. Install dependencies:
   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

---
