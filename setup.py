import pandas as pd
from config import API_KEY

def validate_api_key(): # Checks if the API key exists or not and prints it
    print(f"Using API Key: {API_KEY}")



# Function to read and process the portfolio CSV
def read_portfolio_from_csv(file_path):
    try:
        portfolio_df = pd.read_csv(file_path)

        if not {"Currency Name", "Holdings"}.issubset(portfolio_df.columns):
            raise ValueError("CSV file must contain 'Currency Name' and 'Holdings' columns.")

        portfolio_df["Currency Name"] = portfolio_df["Currency Name"].str.strip()
        portfolio_df["Holdings"] = portfolio_df["Holdings"].astype(float)

        portfolio = portfolio_df.set_index("Currency Name")["Holdings"].to_dict()
        return portfolio

    except Exception as e:
        print(f"Error reading and processing CSV file: {e}")
        return {}