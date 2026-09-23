import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ========== 1. 获取数据 ==========
symbol = "600519.SS"
start_date = "2019-01-01"
end_date = "2021-01-01"

data = yf.download(symbol, start=start_date, end=end_date)  # download
print(data.head())

# ========== 2. 计算移动平均 ==========
data['SMA_50'] = data['Close'].rolling(window=50).mean()  # rolling, mean
data['SMA_200'] = data['Close'].rolling(window=200).mean()  # 200

# ========== 3. 生成信号 ==========
data['Signal'] = 0
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  # 1
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1  # -1

# ========== 4. 计算收益 ==========
data['Daily_Return'] = data['Close'].pct_change()  # pct_change
data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']  # shift

# ========== 5. 累计收益 ==========
data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()  # cumprod
data['Stock_Return'] = data['Close'] / data['Close'].iloc(0)  # iloc

# ========== 6. 可视化 ==========
plt.figure(figsize=(10, 6))
plt.plot(data['Cumulative_Return'], label='Strategy Return', color='b')
plt.plot(data['Stock_Return'], label='Stock Return', color='g')
plt.title("Cumulative Return of Strategy vs. Stock")  # Cumulative Return of Strategy vs. Stock
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()  # legend
plt.show()

# ========== 7. 统计 ==========
strategy_total = data['Cumulative_Return'].iloc[-1] - 1
stock_total = data['Stock_Return'].iloc[-1] - 1
print(f"策略总收益率: {strategy_total:.2%}")
print(f"股票总收益率: {stock_total:.2%}")