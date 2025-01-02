# Importing required libraries
from setup import validate_api_key, read_portfolio_from_csv

# Define trading strategy options (customizable for future)
ROI_OPTIONS = ["Daily", "Weekly", "Monthly", "Yearly"]
ROI_PERCENT_OPTIONS = [5, 10, 15, 20]  # Percent
RISK_RATIO_OPTIONS = ["1:2", "1:3", "1:5"]
TRADING_STRATEGY_OPTIONS = ["Scalping", "Swing Trading", "Arbitrage"]

# Default trading strategy
selected_roi = "Daily"
selected_roi_percent = 5
selected_risk_ratio = "1:2"
selected_trading_strategy = "Scalping"

#TODO: Implement LLM Logic for prosessing Data and implementing trading strategy - explore virtual protocols and a16z

# Main function
if __name__ == "__main__":
    validate_api_key()

    file_path = "portfolio.csv"
    portfolio = read_portfolio_from_csv(file_path)

    if portfolio:
        print(f"Portfolio: {portfolio}")
    else:
        print("No portfolio data found.")