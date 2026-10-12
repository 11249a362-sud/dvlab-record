import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sales_data(num_rows=1000):
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Configuration arrays
    products = {
        'Laptop': {'category': 'Electronics', 'price': 999.99},
        'Smartphone': {'category': 'Electronics', 'price': 599.99},
        'Headphones': {'category': 'Accessories', 'price': 89.99},
        'Backpack': {'category': 'Accessories', 'price': 49.99},
        'Desk Chair': {'category': 'Furniture', 'price': 149.99},
        'Coffee Maker': {'category': 'Appliances', 'price': 79.99}
    }
    regions = ['North', 'East', 'South', 'West']
    channels = ['Online', 'In-Store', 'Wholesale']
    
    # Generate random baseline lists
    start_date = datetime(2025, 1, 1)
    
    data = []
    for i in range(1, num_rows + 1):
        order_id = f"ORD-{100000 + i}"
        date = start_date + timedelta(days=random.randint(0, 365), minutes=random.randint(0, 1440))
        product_name = random.choice(list(products.keys()))
        category = products[product_name]['category']
        unit_price = products[product_name]['price']
        
        # Add slight variance to unit prices (discounts or updates)
        unit_price = round(unit_price * random.uniform(0.9, 1.0), 2)
        
        quantity = random.randint(1, 5) if category != 'Wholesale' else random.randint(10, 50)
        total_sales = round(unit_price * quantity, 2)
        
        region = random.choice(regions)
        sales_channel = random.choice(channels)
        customer_id = f"CUST-{random.randint(1000, 5000)}"
        
        data.append([
            order_id, date.strftime('%Y-%m-%d %H:%M:%S'), customer_id,
            product_name, category, quantity, unit_price, total_sales,
            region, sales_channel
        ])
        
    # Create DataFrame
    columns = [
        'Order_ID', 'Order_Date', 'Customer_ID', 'Product', 
        'Category', 'Quantity', 'Unit_Price', 'Total_Sales', 
        'Region', 'Sales_Channel'
    ]
    df = pd.DataFrame(data, columns=columns)
    
    # Sort chronologically
    df = df.sort_values(by='Order_Date').reset_index(drop=True)
    
    # Save to CSV
    df.to_csv('sample_sales_data.csv', index=False)
    print(f"Successfully generated {num_rows} rows and saved to 'sample_sales_data.csv'.")
    return df

# Execute generator
df_sales = generate_sales_data(1000)
