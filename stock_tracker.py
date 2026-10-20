"""CodeAlpha Task 2: Portfolio tracker with example fixed USD prices."""
import csv
from pathlib import Path

PRICES = {"AAPL": 180.0, "TSLA": 250.0, "GOOGL": 140.0, "MSFT": 330.0, "AMZN": 130.0}

def main():
    print("Stock Portfolio Tracker (illustrative USD prices, not live market quotes)")
    print("Available:", ", ".join(f"{name}: ${price:.2f}" for name, price in PRICES.items()))
    portfolio = {}
    while True:
        symbol = input("Stock symbol (or DONE): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in PRICES:
            print("Unknown symbol. Choose one from the list.")
            continue
        try:
            qty = int(input("Quantity (positive integer): ").strip())
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Enter a positive whole number.")
            continue
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
    total = 0.0
    rows = []
    print("\nYour portfolio:")
    for symbol, qty in portfolio.items():
        value = PRICES[symbol] * qty
        total += value
        rows.append((symbol, qty, PRICES[symbol], value))
        print(f"{symbol}: {qty} x ${PRICES[symbol]:.2f} = ${value:.2f}")
    print(f"Total investment value: ${total:.2f}")
    if rows and input("Save report to CSV? (y/n): ").strip().lower() == "y":
        path = Path(__file__).with_name("portfolio_report.csv")
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Unit Price USD", "Value USD"])
            writer.writerows(rows)
            writer.writerow(["TOTAL", "", "", f"{total:.2f}"])
        print(f"Saved: {path}")

if __name__ == "__main__":
    main()
