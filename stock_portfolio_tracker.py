# Stock Portfolio Tracker

# Hardcoded stock prices (only 5 stocks)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 125,
    "MSFT": 330
}

# Dictionary to store user stock holdings
portfolio = {}

# Display all stock symbols and prices
print("📌 Available Stock Symbols and Prices:")
for symbol, price in stock_prices.items():
    print(f"→ {symbol}: ${price}")
print("\nType 'done' when you're finished entering your stocks.\n")

# Taking input from user
available_symbols = ", ".join(stock_prices.keys())

while True:
    stock = input(f"Enter stock symbol ({available_symbols}): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of shares for {stock}: "))
        if quantity < 0:
            raise ValueError
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid positive number.")

# Calculate and display total investment
print("\n📊 Portfolio Summary:")
total_investment = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Ask to save the summary
save_option = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save_option == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print("✅ Summary saved to 'portfolio_summary.txt'.")