import pandas as pd
import sys
import matplotlib.pyplot as plt
from pathlib import Path # Changed from 'import os'

def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    Includes error handling for a missing file.
    """
    try:
        df = pd.read_csv(file_path)
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
    total_sales = df['Amount'].sum()
    df_monthly = df.set_index('Date')
    monthly_sales = df_monthly['Amount'].resample('M').sum()
    top_salespeople = df.groupby('Salesperson')['Amount'].sum().nlargest(5)
    top_products = df.groupby('Product')['Amount'].sum().nlargest(5)
    
    analysis_results = {
        'total_sales': total_sales,
        'monthly_sales': monthly_sales,
        'top_salespeople': top_salespeople,
        'top_products': top_products
    }
    print("✅ Data processing complete.")
    return analysis_results

def create_visuals(report_data, output_folder='reports'):
    """
    Generates and saves charts based on the analysis using pathlib.
    """
    print("🎨 Creating visuals...")
    
    # --- Pathlib Implementation ---
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
        
    # --- Create Monthly Sales Line Chart ---
    plt.figure(figsize=(10, 5))
    report_data['monthly_sales'].plot(kind='line', marker='o')
    plt.title('Monthly Sales Trend - 2025')
    plt.ylabel('Total Sales ($)')
    plt.xlabel('Month')
    plt.grid(True)
    plt.tight_layout()
    monthly_sales_chart_path = output_path / 'monthly_sales.png'
    plt.savefig(monthly_sales_chart_path)
    plt.close()
    print(f"    - Saved monthly sales chart to '{monthly_sales_chart_path}'")

    # --- Create Top Salespeople Bar Chart ---
    plt.figure(figsize=(10, 6))
    report_data['top_salespeople'].sort_values().plot(kind='barh')
    plt.title('Top 5 Salespeople by Sales Amount')
    plt.xlabel('Total Sales ($)')
    plt.ylabel('Salesperson')
    plt.tight_layout()
    top_sales_chart_path = output_path / 'top_salespeople.png'
    plt.savefig(top_sales_chart_path)
    plt.close()

    print(f"    - Saved top salespeople chart to '{top_sales_chart_path}'")
    print("✅ Visuals created successfully.")

# --- Main execution block ---
if __name__ == "__main__":
    input_csv_path = 'sales_data_2025.csv'
    
    sales_df = load_data(input_csv_path)
    report_data = process_data(sales_df)
    create_visuals(report_data)

    print("\n--- Key Metrics ---")
    print(f"Total Sales: ${report_data['total_sales']:,.2f}")