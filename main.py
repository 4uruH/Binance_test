import requests


def futures_fall_count(simbol: str, prcnt_chng: int):
    """tracking cutters of a given futures and falling of its price by more than a given percentage
        simbol - futures name
        prcnt_chng - expected price drop in percent"""
    count = 0  # counter for easy perception that everything works

    while True:
        try:
            res_prices = requests.get(f"https://api.binance.com/api/v3/ticker?symbol={simbol.upper()}&windowSize=1h")
            hr_h_price = res_prices.json()['highPrice']  # max price for last 1 hr
            last_price = res_prices.json()['lastPrice']  # token price on last resp
            percent_change = ((float(hr_h_price) - float(last_price)) / float(hr_h_price)) * 100

            if percent_change >= prcnt_chng:
                print(f"drop of more than {prcnt_chng} percent from the high price of this hour,\n"
                      f"futures price {last_price}\n"
                      f"high price of this hour {hr_h_price}")
        except Exception as ex:
            print(ex)
        count += 1

        if count % 10 == 0:
            print("Working fine! Wait for price change")


if __name__ == "__main__":
    futures_fall_count("XRPUSDT", 1)
