# spillting the complex task
def generate_report():
    return f"{fetch_sales()}\n{filter_valid_sales()}\n{summarize_data()}\nReport is generated"

def fetch_sales():
    sales = int(input("Enter the total sales of today: "))
    return f"Sales data: {sales}."

def filter_valid_sales():
    return f"Valid sales filtered."

def summarize_data():
    return f"Summarizing sales data."

print(generate_report())