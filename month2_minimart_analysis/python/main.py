import json

orders = [
    {"customer": "Alice", "product": "Cola", "price": 10, "quantity": 3},
    {"customer": "Bob", "product": "Bread", "price": 6.5, "quantity": 2},
    {"customer": "Diana", "product": "Water", "price": 5, "quantity": 5},
    {"customer": "Ethan", "product": "Milk", "price": 12, "quantity": 2},
]

def convert_currency(price_usd, rate=60):
    return price_usd * rate

def generate_report():
    total_sold = sum(o["quantity"] for o in orders)
    revenue_per_customer = {}
    for o in orders:
        total = o["price"] * o["quantity"]
        revenue_per_customer[o["customer"]] = revenue_per_customer.get(o["customer"], 0) + total

    most_popular = max(orders, key=lambda x: x["quantity"])["product"]

    report = {
        "total_products_sold": total_sold,
        "most_popular_product": most_popular,
        "revenue_per_customer": revenue_per_customer,
        "revenue_in_ETB": {k: convert_currency(v) for k, v in revenue_per_customer.items()},
    }

    with open("report.json", "w") as file:
        json.dump(report, file, indent=4)
    
    print("🧾 Report Summary:")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    generate_report()
# Entry point for the MiniMart data reporting system
