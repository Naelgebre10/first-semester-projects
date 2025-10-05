# Uti# utils.py
import pandas as pd

def load_data(file_path):
    """Load CSV data into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return pd.DataFrame()

def calculate_total_sales(df):
    """Calculate total sales."""
    if "Total" in df.columns:
        return df["Total"].sum()
    else:
        print("⚠️ 'Total' column not found.")
        return 0

def calculate_profit_margin(selling_price, cost):
    """Calculate profit margin percentage."""
    if cost == 0:
        return 0
    return ((selling_price - cost) / cost) * 100
lity functions for data conversion and filtering
