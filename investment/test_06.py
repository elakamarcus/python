import requests
from datetime import datetime

# Function to fetch and display fund information
def get_fund_info(fund_id):
    # API URL
    url = f"https://www.avanza.se/_api/fund-guide/guide/{fund_id}"
    
    # Send GET request
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract the required information from the JSON
        fund_name = data.get("name", "Fund name not available")
        nav_price = data.get("nav", "NAV not available")
        nav_date_raw = data.get("navDate", None)

        # If we have a date, format it to YYYY-MM-DD
        if nav_date_raw:
            try:
                nav_date = datetime.strptime(nav_date_raw, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                nav_date = "Invalid date format"
        else:
            nav_date = "Date not available"
        
        # Print the information
        #print(f"{fund_name}: {nav_price} SEK (as of {nav_date})")
        print(f"{fund_name}: {nav_price} SEK ()")
    
    else:
        print(f"Failed to retrieve data: {response.status_code}")


def get_stock_info(stock_id):
    # API URL for stocks
    url = f"https://www.avanza.se/_api/market-guide/stock/{stock_id}"


    # Send GET request
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract the required information from the JSON
        stock_name = data.get("name", "Stock name not available")
        # stock_price = data.get("price", "Price not available")
        quote = data.get("quote", {})
        stock_price = quote.get("last", "Price not available")
        stock_date_raw = data.get("date", None)
        stock_low = quote.get("lowest", "Not available")
        stock_high = quote.get("highest", "Not available")

        # If we have a date, format it to YYYY-MM-DD
        if stock_date_raw:
            try:
                stock_date = datetime.strptime(stock_date_raw, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                stock_date = "Invalid date format"
        else:
            stock_date = "Date not available"

        # Print the information
       # print(f"Stock: {stock_name}")
        #print(f"{stock_name}: {stock_price} SEK (as of {stock_date})")
        print(f"{stock_name}: {stock_price} SEK (High: {stock_high}, Low: {stock_low})")


    else:
        print(f"Failed to retrieve data: {response.status_code}")


# Example of multiple fund IDs you want to check
fund_ids = [150048, 2007]  # Add your fund IDs here

# Loop through the fund IDs and get their information
for fund_id in fund_ids:
    get_fund_info(fund_id)

# Example of multiple stock IDs you want to check
stock_ids = [5269, 5401, 52332, 5247, 5364]  # Example stock IDs, replace with your own

# Loop through the stock IDs and get their information
for stock_id in stock_ids:
    get_stock_info(stock_id)
