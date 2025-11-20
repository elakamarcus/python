import requests
from datetime import datetime

# make web request and return the response data
def get_response_body(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Function to fetch and display fund information
def get_fund_info(fund_id):
    # pull the data

    data = get_response_body(f"https://www.avanza.se/_api/fund-guide/guide/{fund_id}")
    # Extract the required information from the JSON
    fund_name = data.get("name", "Fund name not available")
    fund_price = data.get("nav", "Price (NAV) not available")
        
    # Print the information
    # TODO: print(f"{fund_name}: {nav_price} SEK (as of {nav_date})")
    print(f"{fund_name}: {fund_price} SEK")

def get_stock_info(stock_id):
    # pull the data
    data = get_response_body(f"https://www.avanza.se/_api/market-guide/stock/{stock_id}")
    # Extract the required information from the JSON
    stock_name = data.get("name", "Stock name not available")
    # stock_price = data.get("price", "Price not available")
    quote = data.get("quote", {})
    stock_price = quote.get("last", "Price not available")
    stock_low = quote.get("lowest", "Not available")
    stock_high = quote.get("highest", "Not available")
    stock_avg = (int(stock_high) + int(stock_low) ) /2

    # Print the information
    # TODO: print(f"{stock_name}: {stock_price} SEK (as of {stock_date})")
    print(f"{stock_name}: {stock_price} SEK (High: {stock_high}, Low: {stock_low}, AVG: {stock_avg:.2f})")


# Fund IDs to check
fund_ids = [150048, 2007]  # Add your fund IDs here

# Loop through the fund IDs and get their information
for fund_id in fund_ids:
    get_fund_info(fund_id)

# Stock IDs to check
stock_ids = [5269, 5401, 52332, 5247, 5364]  # Example stock IDs, replace with your own

# Loop through the stock IDs and get their information
for stock_id in stock_ids:
    get_stock_info(stock_id)
