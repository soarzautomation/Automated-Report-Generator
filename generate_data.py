import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define the number of records
num_records = 200

# List of products and salespeople
products = ['Alpha Widget', 'Beta Gadget', 'Gamma Gizmo', 'Delta Device', 'Epsilon Gear']
salespeople = ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward']

# Generate data
data = []
start_date = datetime(2025, 1, 1)
for _ in range(num_records):
    record_date = start_date + timedelta(days=random.randint(0, 240)) # Data for first ~8 months
    product = random.choice(products)
    salesperson = random.choice(salespeople)
    amount = round(random.uniform(50.0, 1000.0), 2)
    customer = fake.company()

    data.append([
        record_date.strftime('%Y-%m-%d'),
        product,
        salesperson,
        amount,
        customer
    ])

# Create a DataFrame
columns = ['Date', 'Product', 'Salesperson', 'Amount', 'Customer']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
file_path = 'sales_data_2025.csv'
df.to_csv(file_path, index=False)

print(f"✅ Successfully generated '{file_path}' with {num_records} records.")