import ccxt
import time
import logging
from decimal import Decimal

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
binance = ccxt.binance()
coinbase = ccxt.coinbase()

# Define the cryptocurrencies to trade
symbol = 'BTC/USDT'

while True:
    try:
        # Retrieve exchange rate data from the exchanges
        binance_order_book = binance.fetch_order_book(symbol, 10)
        coinbase_order_book = coinbase.fetch_order_book(symbol, 10)

        # Calculate the price difference between the exchanges
        price_difference = Decimal(str(binance_order_book['bids'][0][0])) - Decimal(str(coinbase_order_book['asks'][0][0]))

        # Calculate the profit margin based on the minimum profit threshold and trading fees
        profit_margin = price_difference * (1 - TRADING_FEE_RATES['binance'] - TRADING_FEE_RATES['coinbase'])

        # Check if there is a profitable arbitrage opportunity
        if profit_margin > MIN_PROFIT_THRESHOLD:
            # Calculate the trade amount based on the available balances and maximum trade amounts on each exchange
            binance_balance = binance.fetch_balance()
            coinbase_balance = coinbase.fetch_balance()
            trade_amount = min(binance_balance['USDT']['free'], coinbase_balance['BTC']['free'], MAX_TRADE_AMOUNTS['binance'], MAX_TRADE_AMOUNTS['coinbase'])
            trade_amount = trade_amount.quantize(Decimal('0.00000001'))

            # Execute the trades
            binance_order = binance.create_limit_sell_order(symbol, trade_amount, binance_order_book['bids'][0][0])
            coinbase_order = coinbase.create_limit_buy_order(symbol, trade_amount, coinbase_order_book['asks'][0][0])

            # Log the trades and profit margin
            logging.info(f'Trade executed: sold {binance_order["amount"]} {binance_order["symbol"]} on Binance and bought {coinbase_order["amount"]} {coinbase_order["symbol"]} on Coinbase')
            logging.info(f'Profit margin: {profit_margin:.8f} USDT')

        # Wait for a few seconds before checking again
        time.sleep(5)

    except Exception as e:
        # Handle errors gracefully and log the error message
        logging.error(str(e))
        time.sleep(60)
