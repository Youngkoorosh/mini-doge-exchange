import requests

def get_doge_price():
    try:
        url = "https://apiv2.nobitex.ir/v3/orderbook/DOGEIRT"
        res = requests.get(url, timeout=3)
        data = res.json()

        bid = float(data['bids'][0][0])   # بهترین خریدار
        ask = float(data['asks'][0][0])   # بهترین فروشنده

        price = (bid + ask) / 2

        return price

    except Exception as e:
        print("ERROR:", e)
        return 140000  # fallback منطقی