stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    name = input("Enter stock name (or 'done' to stop): ").upper()
    if name == "DONE":
        break

    if name in stocks:
        qty = int(input("Enter quantity: "))
        total_investment += stocks[name] * qty
    else:
        print("Stock not found!")

print(" Total Investment Value:", total_investment)

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: {total_investment}")