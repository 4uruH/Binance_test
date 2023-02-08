import aiohttp
import asyncio


async def futures_fall_count(name, prcnt):
    """tracking cutters of a given futures and falling of its price by more than a given percentage
        name - futures name
        prcnt - expected price drop in percent"""
    count = 0  # counter for easy perception that everything works

    async with aiohttp.ClientSession() as session:

        while True:
            url = f'https://api.binance.com/api/v3/ticker?symbol={name}&windowSize=1h'
            async with session.get(url) as resp:
                data = await resp.json()
                hr_h_price = data['highPrice']  # max price for last 1 hr
                last_price = data['lastPrice']  # token price on last resp
                percent_change = ((float(hr_h_price) - float(last_price)) / float(hr_h_price)) * 100

                if percent_change >= prcnt:
                    print(f"drop of more than {prcnt} percent from the high price of this hour,\n"
                          f"futures price {last_price}\n"
                          f"high price of this hour {hr_h_price}")

                count += 1

                if count % 10 == 0:
                    print("Working fine! Wait for price change")


asyncio.run(futures_fall_count('XRPUSDT', 1))
