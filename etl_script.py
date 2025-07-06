import pandas as pd
from sqlalchemy import create_engine, text

# READ EXCEL FILE AND FILL NA VALUES
file_path = 'sales_data.xlsx' 
df = pd.read_excel(file_path)

df['Quantity'] = df['Quantity'].fillna(0)
df['Unit_Price'] = df['Unit_Price'].fillna(0)
df['Date'] = pd.to_datetime(df['Date'])
df['Total_Sales'] = df['Quantity'] * df['Unit_Price']

engine = create_engine('sqlite:///sales_data.db') 

df.to_sql('sales', con=engine, if_exists='replace', index=False)

print('Data loaded successfully to "sales_data.db".')

# Query to get the top 3 products by total sales
with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT Product, SUM(Total_Sales) AS Total_Sales
        FROM sales
        GROUP BY Product
        ORDER BY Total_Sales DESC
        LIMIT 3
    """))
    top_products = pd.DataFrame(result.fetchall(), columns=result.keys())
# Display the top 3 products by revenue
print('\nTop 3 Products by Revenue:\n', top_products)

# Monthly sales report
query_monthly_sales = """
    SELECT strftime('%Y-%m', Date) as Month, SUM(Total_Sales) as Total_Sales
    FROM sales
    GROUP BY Month;
"""

# Corrected: use engine, not closed connection
monthly_sales = pd.read_sql(query_monthly_sales, con=engine)

print("Monthly Sales Report:")
print(monthly_sales)

# Export result to Excel
with pd.ExcelWriter('monthly_sales_report.xlsx') as writer:
    top_products.to_excel(writer, sheet_name='Top_Products', index=False)
    monthly_sales.to_excel(writer, sheet_name='Monthly_Sales', index=False)

print("Monthly sales report exported to 'monthly_sales_report.xlsx'.")
