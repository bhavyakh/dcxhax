import pandas as pd


def numCross(filename, low=4000, high=4100):
    df = pd.read_csv(filename)

    amount = 100000
    profit = 0
    lastbuyprice = 0
    owned = False
    count = 0
    for idx, row in df.iterrows():
        if not owned:
            if row["low"] <= low:
                owned = True
        else:
            if row["high"] >= high:
                owned = False
                count += 1
                amount *= ((high*0.999)/(low*1.001))

        if owned:
            if row["close"] >= high:
                owned = False
                count += 1
                amount *= ((high*0.999)/(low*1.001))
        else:
            if row["close"] <= low:
                owned = True
    print(count)
    return amount


print(numCross("del.csv"))
