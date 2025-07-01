import pandas as pd
import requests


url = "https://api.binance.com/api/v3/klines?"

params = {
    "symbol":"BTCUSDT",
    "interval":"1d",
    "limit":100
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data,columns=["timestamp","open","high","low","close",
    "volume","close_time","quote_asset_volume",
    "number_of_trades","taker_buy_base_volume",
    "taker_buy_quote_volume","ignore"])


df["timestamp"] = pd.to_datetime(df["timestamp"],unit="ms")

df.set_index('timestamp',inplace=True)
df.sort_index(inplace=True)

print(df.head())

import matplotlib.pyplot as plt


df["SMA short"] = df["close"].rolling(window=10).mean()
df["SMA long"] = df['close'].rolling(window = 50).mean() #вичитала про rolling в інтернеті, шукала щось, що рахуватиме в проміжку

df["signal"] = 0
df.loc[df['SMA short'] > df['SMA long'], "signal"] = 1 #треба брать
df.loc[df['SMA long'] > df["SMA short"], "signal"] = -1 #треба продать

df['position'] = 0
for i in range(1, len(df)):
    df.loc[df.index[i], 'position'] = df.loc[df.index[i - 1], 'signal']



# df["returns"] = 0
# for i in range(1, len(df)):
#     prev = df["close"].iloc[i - 1]
#     curr = df["close"].iloc[i]
#     df.loc[df.index[i], "returns"] = (curr - prev) / prev

# df["returns_strategichni"] = df["returns"] * df['position']
#я намагалась це прописати ось так, але воно видає можливість майбутньої помилки, тому не склалось...буду вдячна, якщо в фідбек напишете, чому тут пайтон ламався :(

cols = ["open", "high", "low", "close", "volume"]
df[cols] = df[cols].astype(float) #бо інакше через int64 в датафреймі починаються помилки

df['returns'] = df['close'].pct_change()
df["returns_strategichni"] = df["returns"] * df['position']

df['cumulative_rynok'] = (1 + df["returns"]).cumprod()
df['cumulative_strategichno'] = (1+df['returns_strategichni']).cumprod()

print("🩷порівняння результатів🩷")
print("купити і чекати: {:.2%}".format(df['cumulative_rynok'].iloc[-1]-1))
print("стратегічні результати: {:.2%}".format(df['cumulative_strategichno'].iloc[-1]-1))

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(df.index, df["cumulative_rynok"], label="купити і чекати", linestyle = "--", linewidth = "2")
plt.plot(df.index, df["cumulative_strategichno"], label="стратегічні результати", linestyle = "--", linewidth = "2")
plt.title("порівнння результативності двох методів")
plt.xlabel("дані")
plt.ylabel("кумулятивний дохід")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#у висновку, шось погано стратегія працює.......