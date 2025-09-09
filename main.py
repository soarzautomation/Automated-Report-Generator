import pandas as pd
import sys
import matplotlib.pyplot as plt
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch
from datetime import datetime

# --- 1. Data Loading ---
def load_data(file_path):
    """Loads and preprocesses data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        print("✅ Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
        sys.exit(1)

# --- 2. Data Processing ---
def process_data(df):
    """Analyzes the sales data to extract key metrics."""
    print("⚙️  Processing data...")
    analysis_results = {
        'total_sales': df['Amount'].sum(),
        'monthly_sales': df.set_index('Date')['Amount'].resample('M').sum(),
        'top_salespeople': df.groupby('Salesperson')['Amount'].sum().nlargest(5),
        'top_products': df.groupby('Product')['Amount'].sum().nlargest(5)
    }
    print("✅ Data processing complete.")
    return analysis_results

# --- 3. Chart Creation ---
def create_visuals(report_data, output_folder):
    """Generates and saves charts based on the analysis."""
    print("🎨 Creating visuals...")
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Monthly Sales Chart
    plt.figure(figsize=(10, 5))
    report_data['monthly_sales'].plot(kind='line', marker='o')
    plt.title('Monthly Sales Trend - 2025')
    plt.ylabel('Total Sales ($)'); plt.xlabel('Month'); plt.grid(True); plt.tight_layout()
    monthly_sales_chart_path = output_path / 'monthly_sales.png'
    plt.savefig(monthly_sales_chart_path)
    plt.close()

    # Top Salespeople Chart
    plt.figure(figsize=(10, 6))
    report_data['top_salespeople'].sort_values().plot(kind='barh')
    plt.title('Top 5 Salespeople by Sales Amount')
    plt.xlabel('Total Sales ($)'); plt.ylabel('Salesperson'); plt.tight_layout()
    top_sales_chart_path = output_path / 'top_salespeople.png'
    plt.savefig(top_sales_chart_path)
    plt.close()
    
    print("✅ Visuals created successfully.")
    return {'monthly_chart': monthly_sales_chart_path, 'salespeople_chart': top_sales_chart_path}

# --- 4. PDF Generation (Revised for Professional Formatting) ---
def create_pdf_report(report_data, chart_paths, output_folder):
    """Generates a professional PDF report with all the findings."""
    print("📄 Generating PDF report...")
    output_path = Path(output_folder)
    report_pdf_path = output_path / f"sales_report_{datetime.now().strftime('%Y_%m')}.pdf"
    
    c = canvas.Canvas(str(report_pdf_path), pagesize=letter)
    width, height = letter
    margin = inch

    # --- Header ---
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, height - margin, "Monthly Sales Performance Report")
    c.setFont("Helvetica", 11)
    c.drawString(margin, height - margin - 0.25 * inch, f"Report Generated: {datetime.now().strftime('%Y-%m-%d')}")
    c.line(margin, height - margin - 0.4 * inch, width - margin, height - margin - 0.4 * inch)
    
    # --- Section 1: Key Metrics & Top Products Table ---
    y_position = height - margin - 0.75 * inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y_position, "Summary & Top Products")
    y_position -= 0.4 * inch

    # Key Metric
    c.setFont("Helvetica", 12)
    total_sales_text = f"Total Sales This Period: ${report_data['total_sales']:,.2f}"
    c.drawString(margin, y_position, total_sales_text)
    y_position -= 0.3 * inch

    # Top Products Table
    top_products_df = report_data['top_products'].reset_index()
    top_products_df['Amount'] = top_products_df['Amount'].apply(lambda x: f"${x:,.2f}")
    table_data = [top_products_df.columns.to_list()] + top_products_df.values.tolist()
    
    table = Table(table_data, colWidths=[2.5 * inch, 1.25 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkslategray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.ghostwhite),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    table.wrapOn(c, width, height)
    table_height = sum(table._rowHeights)
    # Calculate the total width of the table
    table_width = 2.5 * inch + 1.25 * inch
    # Calculate the centered x-coordinate
    centered_x_position = (width - table_width) / 2
    table.drawOn(c, centered_x_position, y_position - table_height)

    # --- Section 2: Visual Analysis ---
    y_position -= (table_height + 0.5 * inch)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y_position, "Visual Analysis")
    y_position -= 0.25 * inch
    
    # Monthly Sales Chart (Full Width)
    chart_height = 2.5 * inch
    c.drawImage(str(chart_paths['monthly_chart']), margin, y_position - chart_height, 
                width=width - 2 * margin, height=chart_height, preserveAspectRatio=True, anchor='n')
    y_position -= (chart_height + 0.25 * inch)
    
    # Top Salespeople Chart (Full Width)
    c.drawImage(str(chart_paths['salespeople_chart']), margin, y_position - chart_height, 
                width=width - 2 * margin, height=chart_height, preserveAspectRatio=True, anchor='n')

    c.save()
    print(f"✅ PDF report saved to '{report_pdf_path}'")

# --- Main Execution Block ---
if __name__ == "__main__":
    REPORTS_FOLDER = 'reports'
    
    sales_df = load_data('sales_data_2025.csv')
    report_data = process_data(sales_df)
    chart_paths = create_visuals(report_data, REPORTS_FOLDER)
    create_pdf_report(report_data, chart_paths, REPORTS_FOLDER)

    print("\n🎉 Automation complete! Check the 'reports' folder.")