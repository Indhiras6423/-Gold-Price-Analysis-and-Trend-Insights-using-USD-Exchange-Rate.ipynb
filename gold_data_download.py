import yfinance as yf

gold = yf.download("GC=F", start="2020-01-01", end="2026-04-19")
gold.reset_index(inplace=True)
gold.to_csv("gold_data.csv", index=False)

usd = yf.download("USDINR=X", start="2020-01-01", end="2026-04-19")
usd.reset_index(inplace=True)
usd.to_csv("usd_data.csv", index=False)

print("Datasets downloaded successfully!")
