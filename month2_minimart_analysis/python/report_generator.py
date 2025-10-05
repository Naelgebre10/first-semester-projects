# C# report_generator.py
import pandas as pd
from utils import load_data, calculate_total_sales, calculate_profit_margin

def generate_summary_report(file_path):
    """Generate a summary report for the MiniMart dataset."""
    df = load_data(file_path)
    
    print("\n🛒 MINIMART SALES SUMMARY REPORT 🛒")
    print("-----------------------------------")
    
    # Total sales and profit
    total_sales = calculate_total_sales(df)
    df["Profit Margin"] = df.apply(lambda row: calculate_profit_margin(row["Total"], row["Cost"]), axis=1)
    
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Average Profit Margin: {df['Profit Margin'].mean():.2f}%\n")
    
    # Best-selling products
    best_products = df.groupby("Product")["Total"].sum().sort_values(ascending=False).head(5)
    print("🏆 Top 5 Best-Selling Products:")
    print(best_products)
    
    # Sales by category
    category_sales = df.groupby("Category")["Total"].sum().sort_values(ascending=False)
    print("\n📊 Sales by Category:")
    print(category_sales)
    
    # Monthly trend (if date column exists)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Total"].sum()
        print("\n📈 Monthly Sales Trend:")
        print(monthly_sales)
    
    return {
        "total_sales": total_sales,
        "avg_profit_margin": df["Profit Margin"].mean(),
        "top_products": best_products,
        "category_sales": category_sales
    }

if __name__ == "__main__":
    report = generate_summary_report("../data/sales_data.csv")
ode to generate dictionary summary reports
