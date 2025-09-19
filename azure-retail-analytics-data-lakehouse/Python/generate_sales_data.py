import pandas as pd
import datetime
import random

def generate_sales_data(num_rows=1000, file_name=r"C:\Users\pawan\Downloads\Data Engineering Projects\SalesData_Azure\sales_data.csv"):
    """Generates a sample CSV file with retail sales data."""
    data = []
    regions = ["North", "South", "East", "West", "Central"]
    product_ids = [f"PROD{i:03d}" for i in range(1, 21)] # 20 products
    customer_ids = [f"CUST{i:04d}" for i in range(1, 51)] # 50 customers

    # Generate data for the last 6 months for a good time range
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=180) # Approx 6 months

    for i in range(num_rows):
        transaction_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        price = round(random.uniform(10.0, 500.0), 2)
        region = random.choice(regions)

        data.append({
            "TransactionID": f"TXN{i+1:05d}",
            "CustomerID": customer_id,
            "ProductID": product_id,
            "Quantity": quantity,
            "Price": price,
            "TransactionDate": transaction_date.isoformat(), # YYYY-MM-DD format
            "Region": region
        })

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print(f"Generated {num_rows} rows and saved to {file_name}")

if __name__ == "__main__":
    generate_sales_data(num_rows=1000) # Generate 1000 rows