import pandas as pd
import sys

def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    Includes error handling for a missing file.
    """
    try:
        df = pd.read_csv(file_path)
        # Convert 'Date' column to datetime objects for proper analysis
        df['Date'] = pd.to_datetime(df['Date'])
        print("✅ Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
        print("Please ensure the data file exists in the same directory.")
        sys.exit(1)

def process_data(df):
    """
    Analyzes the sales data to extract key metrics.
    """
    print("⚙️  Processing data...")
    
    # 1. Calculate total sales
    total_sales = df['Amount'].sum()
    
    # 2. Analyze monthly sales
    # Set the 'Date' column as the index for time-based resampling
    df_monthly = df.set_index('Date')
    # Resample by month ('M') and sum the 'Amount'
    monthly_sales = df_monthly['Amount'].resample('M').sum()
    
    # 3. Find top 5 salespeople by sales amount
    top_salespeople = df.groupby('Salesperson')['Amount'].sum().nlargest(5)
    
    # 4. Find top 5 products by sales amount
    top_products = df.groupby('Product')['Amount'].sum().nlargest(5)
    
    # Store all analyses in a dictionary to return
    analysis_results = {
        'total_sales': total_sales,
        'monthly_sales': monthly_sales,
        'top_salespeople': top_salespeople,
        'top_products': top_products
    }
    
    print("✅ Data processing complete.")
    return analysis_results

# --- Main execution block ---
if __name__ == "__main__":
    # Define the input file
    input_csv_path = 'sales_data_2025.csv'
    
    # Load the data
    sales_df = load_data(input_csv_path)
    
    # Process the data
    report_data = process_data(sales_df)
    
    # --- Verification Step ---
    print("\n--- Key Metrics ---")
    print(f"Total Sales: ${report_data['total_sales']:,.2f}")
    
    print("\n--- Monthly Sales ---")
    print(report_data['monthly_sales'].to_string(float_format="${:,.2f}".format))
    
    print("\n--- Top 5 Salespeople ---")
    print(report_data['top_salespeople'].to_string(float_format="${:,.2f}".format))

    print("\n--- Top 5 Products ---")
    print(report_data['top_products'].to_string(float_format="${:,.2f}".format))