# import ccxt
import time
import logging
from decimal import Decimal, ROUND_DOWN
import random
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the minimum profit threshold for executing trades (in USDT)
MIN_PROFIT_THRESHOLD = 10

# Define the trading fee rates for each exchange
TRADING_FEE_RATES = {
    'binance': 0.001,
    'coinbase': 0.005,
}

# Define the maximum trade amount (in USDT) for each exchange
MAX_TRADE_AMOUNTS = {
    'binance': 1000,
    'coinbase': 1000,
}

# Connect to the exchanges
# binance = ccxt.binance()
# coinbase = ccxt.coinbase()

# Define the cryptocurrencies to trade
symbol = 'BTC/USDT'

# List of data keys
data_keys = ["direction", "binancePrice", "priceKucoin", "Difference", "Percentage", "EthGasFee"]

# Generate 100 random datasets
random_data = []
for _ in range(13369):
    data = {}
    data["direction"] = random.choice([-1, 0, 1])
    data["binancePrice"] = "{:.8f}".format(random.uniform(27650, 26474))
    data["priceKucoin"] = "{:.8f}".format(random.uniform(27650, 26474))
    data["Difference"] = "{:.8f}".format(float(data["binancePrice"]) - float(data["priceKucoin"]))
    
    # data["Percentage"] = "{:.2f}".format((float(data["Difference"]) / float(data["binancePrice"])) * 100)
    # data["EthGasFee"] = str(random.randint(35, 40))
    
    # Generate percentage value less than 0.03 for 88% of the data
    if random.random() < 0.88:
        data["Percentage"] = "{:.8f}".format(random.uniform(0, 0.03))
    else:
        data["Percentage"] = "{:.8f}".format(random.uniform(0, 0.84))
    
    data["EthGasFee"] = str(random.randint(35, 40))
    
    random_data.append(data)

# # Print the generated datasets
# for data in random_data:
#     print(data)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(random_data)

# Save the DataFrame to an Excel file
df.to_excel("13369_BTC_data.xlsx", index=False)
