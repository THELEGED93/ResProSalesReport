🛒 Sales Data ETL and Reporting
📈 Overview
This project automates the extraction, transformation, and loading (ETL) of sales data. It reads an Excel file, cleans and processes the data, stores it in a SQLite database, runs analytical queries to summarize performance, and exports the results to Excel reports.

✨ Features
Data Cleaning: Handles missing quantities and unit prices.

Data Enrichment: Calculates total sales for each transaction.

Database Storage: Loads cleaned data into a SQLite database.

Analysis:

Identifies top 3 products by total revenue.

Generates monthly sales summaries.

Reporting: Exports analysis results to a multi-sheet Excel file.

🛠️ Technologies Used
Python

pandas

SQLAlchemy

SQLite

Excel (via pandas)

🚀 Getting Started
Prerequisites
Make sure you have Python installed (version 3.7+ recommended) and install the required packages:

bash
Copy
Edit
pip install pandas SQLAlchemy openpyxl
Project Structure
graphql
Copy
Edit
sales-etl-project/
├── sales_data.xlsx              # Input Excel file with sales data
├── sales_data.db                # Generated SQLite database
├── monthly_sales_report.xlsx    # Output Excel report with analysis
├── etl_script.py                # Main ETL and analysis script
└── README.md                    # Project documentation
🧩 How to Run
Place your input Excel file in the project directory, named sales_data.xlsx.
The Excel file should have at least the following columns:

Date

Product

Quantity

Unit_Price

Run the script:

bash
Copy
Edit
python etl_script.py
The script will:

Create (or overwrite) sales_data.db

Print the top 3 products by revenue

Print the monthly sales summary

Export monthly_sales_report.xlsx with:

Top_Products sheet

Monthly_Sales sheet

🖼️ Sample Output
Console:

yaml
Copy
Edit
Data loaded successfully to "sales_data.db".

Top 3 Products by Revenue:
        Product  Total_Sales
0     Product A        5000
1     Product B        4200
2     Product C        3900

Monthly Sales Report:
       Month  Total_Sales
0  2023-01         2100
1  2023-02         3500
2  2023-03         4600
Excel Output:

monthly_sales_report.xlsx

Sheet 1: Top_Products

Sheet 2: Monthly_Sales

📝 Notes
The script automatically fills missing Quantity and Unit_Price with 0.

Dates are parsed using pd.to_datetime.

SQLite is used as a lightweight, file-based database.

📄 License
This project is provided under the MIT License.

