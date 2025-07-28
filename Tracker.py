# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

# Dictionary to store user input
portfolio = {}

print("Enter your stock portfolio (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not in list. Available stocks:", ', '.join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Invalid quantity. Please enter an integer.")

# Calculate total investment
total_investment = 0
print("\nYour Investment Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: Save to a file
save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save_option == 'yes':
    file_type = input("Enter file type (.txt or .csv): ").lower()
    filename = f"portfolio{file_type}"
    try:
        with open(filename, 'w') as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
            f.write(f"\nTotal Investment: ${total_investment}")
        print(f"Saved to {filename}")
    except Exception as e:
        print("Error saving file:", e)