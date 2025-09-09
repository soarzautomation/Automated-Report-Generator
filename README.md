# Automated PDF Report Generator
This automation tool transforms raw CSV or Excel data into polished, professional PDF reports in minutes, not hours. It's a demonstration of how a targeted automation can reclaim valuable time and ensure perfect consistency for any business.

## The Business Problem
Does your team spend hours every month manually copying data from spreadsheets into reports? Do formatting inconsistencies and the risk of human error make your business look unprofessional? This tool is designed to solve that exact problem.

## The Solution & Business Impact
This script automates the entire report creation process, delivering significant, measurable benefits:
- **Time Savings:** Reduces a 2-3 hour manual process to under 5 minutes, saving 8-12 hours per month on this single task.
- **Error Elimination:** Removes the risk of human error in data transfer and calculations.
- **Enhanced Professionalism:** Ensures professional, consistently branded formatting every single time.
- **Strategic Focus:** Allows your staff to spend their time on analyzing the data, not just preparing it.

## How It Works 
This tool is built with a clean, modular Python script. It intelligently parses input data using the **pandas** library, performs necessary calculations, and uses **matplotlib** to generate visual charts. Finally, it assembles all data and charts into a professional PDF using **ReportLab**. The code is well-commented and designed for easy customization.

## How to Use

This tool is designed to be run from the command line. Follow these steps to generate your own report:

### 1. Prerequisites

- Ensure you have Python 3.8+ installed on your system.
- It is highly recommended to use a virtual environment to manage dependencies.

### 2. Installation

Clone this repository to your local machine and install the required packages:

```bash
# Clone the repository
git clone https://github.com/soarzautomation/Automated-Report-Generator.git

# Navigate into the project directory
cd Automated-Report-Generator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt
```

### 3. Execution

Place your input data file (e.g., `sales_data.csv`) in the root of the project directory. Then, run the script:

```bash
python main.py
```

The script will generate a new PDF report inside the `reports` folder.sales_summary`

![A screenshot of the final PDF report](./assets/sample_report.jpg)