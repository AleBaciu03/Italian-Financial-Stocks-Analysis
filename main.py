import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

tickers = ['FBK.MI', 'ISP.MI', 'G.MI', 'UCG.MI'] #Fineco, Intesa San Paolo, Generali e UniCredit
df = yf.download(tickers, start = '2015-1-1', end = dt.datetime.today())
df = df['Close']
df
norm = df/df.iloc[0]
plt.figure(figsize=(18,9))
label = ['Fineco','Generali' , 'Intesa San Paolo', 'UniCredit']
plt.plot(norm, label = label)
plt.title('Stocks return')
plt.xlabel('Date')
plt.ylabel('Prices')
plt.grid(True, alpha = 0.6, linestyle = '--')
plt.legend()
plt.show()
for ticker in tickers:
    df[f'{ticker} Price Change'] = df[ticker].diff()
df = df.dropna()
df2 = df.copy()
df2 = df2.drop(['FBK.MI', 'ISP.MI', 'G.MI', 'UCG.MI'], axis = 1)
plt.figure(figsize=(20,10))
sns.violinplot(df2, width=0.8, inner='box', linewidth=2)
plt.grid(True, alpha = 0.6, linestyle = '--')
plt.title('Violinplot', size= 30)
plt.figure(figsize=(20,10))

fig, axes = plt.subplots(2, 2, figsize=(12,8))  # 2x2 grid
axes = axes.flatten()  # make it easier to loop

for i, ticker in enumerate(df2.columns):
    axes[i].hist(df2[ticker].dropna(), bins=30, color="skyblue", edgecolor="black")
    axes[i].set_title(f"Histogram of {ticker}")
    axes[i].set_xlabel("Value")
    axes[i].set_ylabel("Frequency")

plt.tight_layout()
plt.show()
corr = df2.corr()
plt.figure(figsize=(5,4))
sns.heatmap(corr, annot = True, cmap = 'RdYlGn')
plt.xticks(rotation=45)
