import pandas as pd
import sys

def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    Includes error handling for a missing file.
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
        print("Please ensure the data file exists in the same directory.")
        sys.exit(1) # Exit the script with an error code

# --- Main execution block ---
if __name__ == "__main__":
    # Define the input file
    input_csv_path = 'sales_data_2025.csv'
    
    # Load the data
    sales_df = load_data(input_csv_path)
    
    # --- Verification Step ---
    # Display the first 5 rows and a summary of the data
    print("\n--- First 5 Rows of Data ---")
    print(sales_df.head())
    
    print("\n--- Data Summary & Types ---")
    sales_df.info()