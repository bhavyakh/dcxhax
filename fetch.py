import requests
import json
import pandas as pd
from tqdm import tqdm
def fetch(pair):
    df = pd.DataFrame(columns=["open", "close", "low", "high", "time", "volume"])
    # pair_name = "B-ETH_USDT"
    pair_name = pair
    res = requests.get(
        f"https://public.coindcx.com/market_data/candles?pair={pair_name}&limit=1000&interval=1m")
    # print(res.content.decode('utf-8'))
    obj = json.loads(res.content.decode('utf-8'))
    # print(obj[-1])
    for i in tqdm(range(50)):
        endTime = obj[-1]["time"] - 1
        # print(endTime)
        res = requests.get(
            f"https://public.coindcx.com/market_data/candles?pair={pair_name}&limit=1000&interval=1m&startTime=1600000&endTime={endTime}")
        obj = json.loads(res.content.decode('utf-8'))
        
        df = df.append(obj, ignore_index=True)


    df = df.iloc[::-1]

    df.to_csv(f'{pair_name}.csv')
