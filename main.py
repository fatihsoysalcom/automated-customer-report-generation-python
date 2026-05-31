import datetime
import collections

# --- 1. Simulate Customer Data ---
# In a real-world scenario, this data would typically come from a database, API, or CSV file.
# For this example, we use a list of dictionaries to represent customer transactions.
customer_transactions = [
    {"customer_id": "C001", "name": "Ayşe Yılmaz", "product": "Laptop", "amount": 1200, "date": "2023-10-01"},
    {"customer_id": "C002", "name": "Mehmet Demir", "product": "Mouse", "amount": 50, "date": "2023-10-01"},
    {"customer_id": "C001", "name": "Ayşe Yılmaz", "product": "Keyboard", "amount": 150, "date": "2023-10-02"},
    {"customer_id": "C003", "name": "Zeynep Kaya", "product": "Monitor", "amount": 300, "date": "2023-10-02"},
    {"customer_id": "C002", "name": "Mehmet Demir", "product": "Webcam", "amount": 80, "date": "2023-10-03"},
    {"customer_id": "C001", "name": "Ayşe Yılmaz", "product": "Headphones", "amount": 100, "date": "2023-10-03"},
    {"customer_id": "C004", "name": "Ali Can", "product": "Laptop Bag", "amount": 60, "date": "2023-10-04"},
    {"customer_id": "C003", "name": "Zeynep Kaya", "product": "USB Hub", "amount": 30, "date": "2023-10-04"},
    {"customer_id": "C005", "name": "Elif Ak", "product": "SSD", "amount": 200, "date": "2023-10-05"},
    {"customer_id": "C001", "name": "Ayşe Yılmaz", "product": "External HDD", "amount": 90, "date": "2023-10-05"},
]

def generate_customer_report(data):
    """
    Generates a summary report from customer transaction data.
    This function encapsulates the 'automated reporting' logic.
    """
    total_revenue = 0
    customer_revenue = collections.defaultdict(float)
    unique_customers = set()
    transaction_count = 0

    # --- 2. Process/Analyze Data ---
    # This loop iterates through the simulated data to calculate key metrics.
    for transaction in data:
        amount = transaction["amount"]
        customer_id = transaction["customer_id"]
        customer_name = transaction["name"]

        total_revenue += amount
        customer_revenue[(customer_id, customer_name)] += amount
        unique_customers.add(customer_id)
        transaction_count += 1

    num_unique_customers = len(unique_customers)
    average_transaction_value = total_revenue / transaction_count if transaction_count > 0 else 0

    # Sort customers by revenue to identify top spenders
    sorted_customers = sorted(customer_revenue.items(), key=lambda item: item[1], reverse=True)
    top_n_customers = sorted_customers[:3] # Get top 3 customers for the report

    # --- 3. Generate Report ---
    # This section constructs the human-readable report string.
    report_lines = []
    report_lines.append(f"--- Otomatik Müşteri Raporu ({datetime.date.today().strftime('%Y-%m-%d')}) ---")
    report_lines.append("\nGenel Bakış:")
    report_lines.append(f"  Toplam Gelir: {total_revenue:.2f} TL")
    report_lines.append(f"  Benzersiz Müşteri Sayısı: {num_unique_customers}")
    report_lines.append(f"  Ortalama İşlem Değeri: {average_transaction_value:.2f} TL")
    report_lines.append(f"  Toplam İşlem Sayısı: {transaction_count}")

    report_lines.append("\nEn Çok Harcayan Müşteriler (İlk 3):")
    if top_n_customers:
        for (customer_id, customer_name), revenue in top_n_customers:
            report_lines.append(f"  - {customer_name} ({customer_id}): {revenue:.2f} TL")
    else:
        report_lines.append("  Müşteri verisi bulunamadı.")

    report_lines.append("\n--- Rapor Sonu ---")

    return "\n".join(report_lines)

if __name__ == "__main__":
    # Execute the report generation process automatically
    report_content = generate_customer_report(customer_transactions)

    # Print the generated report to the console
    print(report_content)

    # Save the report to a file, simulating automated delivery or archival
    report_filename = f"customer_report_{datetime.date.today().strftime('%Y%m%d')}.txt"
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"\nBaşarılı: Rapor '{report_filename}' dosyasına kaydedildi.")
    except IOError as e:
        print(f"\nHata: Rapor dosyaya kaydedilemedi: {e}")
