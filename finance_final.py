
get_ipython().system('pip install fredapi')



#Global price of wheat, corn, soybeans
from fredapi import Fred
fred = Fred(api_key='4e4a4ea389197ac12ee3036ee4cff0fc')
data_wheat = fred.get_series('PWHEAMTUSDM','1/1/2010')
data_corn = fred.get_series('PMAIZMTUSDM','1/1/2010')
data_soybeans = fred.get_series('PSOYBUSDM','1/1/2010')



data_wheat
data_corn
data_soybeans




data_wheat.plot()
data_corn.plot()
data_soybeans.plot()


#讀取資料
frame_wheat = data_wheat.to_frame(name = 'PWHEAMTUSDM')
frame_corn = data_corn.to_frame(name = 'PMAIZMTUSDM')
frame_soybeans = data_soybeans.to_frame(name = 'PSOYBUSDM')
frame_wheat,frame_corn,frame_soybeans




import pandas as pd
df_merged = pd.concat([frame_wheat, frame_corn, frame_soybeans],axis=1)



import matplotlib
import matplotlib.pyplot as plt




#繪製基本圖形
plt.plot(df_merged.index, df_merged['PWHEAMTUSDM'])
plt.plot(df_merged.index, df_merged['PMAIZMTUSDM'])
plt.plot(df_merged.index, df_merged['PSOYBUSDM'])



fig,ax_wheat = plt.subplots()
fig,ax_corn = plt.subplots()
fig,ax_soybeans = plt.subplots()
ax_wheat.plot(df_merged.index,df_merged['PWHEAMTUSDM'],color = 'tan')
ax_corn.plot(df_merged.index,df_merged['PMAIZMTUSDM'],color = 'lightseagreen')
ax_soybeans.plot(df_merged.index,df_merged['PSOYBUSDM'],color = 'slategray')



import matplotlib.pyplot as plt

# 創建一個包含三個子圖的畫布
fig, (ax_wheat, ax_corn, ax_soybeans) = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

# 繪製每個子圖的資料
ax_wheat.plot(df_merged.index, df_merged['PWHEAMTUSDM'], color='tan', label='Wheat')
ax_corn.plot(df_merged.index, df_merged['PMAIZMTUSDM'], color='lightseagreen', label='Corn')
ax_soybeans.plot(df_merged.index, df_merged['PSOYBUSDM'], color='slategray', label='Soybeans')

# 設置標籤和標題
ax_wheat.set_ylabel('Price (USD)')
ax_corn.set_ylabel('Price (USD)')
ax_soybeans.set_ylabel('Price (USD)')
ax_soybeans.set_xlabel('Date')

# 添加圖例
ax_wheat.legend()
ax_corn.legend()
ax_soybeans.legend()

# 顯示圖形
plt.show()


import matplotlib.pyplot as plt

# 創建一張包含三條相關趨勢圖的線的圖表
fig, (ax_wheat, ax_corn, ax_soybeans) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# 繪製每條趨勢圖的線
ax_wheat.plot(df_merged.index, df_merged['PWHEAMTUSDM'], color='tan', label='Wheat')
ax_corn.plot(df_merged.index, df_merged['PMAIZMTUSDM'], color='lightseagreen', label='Corn')
ax_soybeans.plot(df_merged.index, df_merged['PSOYBUSDM'], color='slategray', label='Soybeans')

# 設置標籤、標題等
ax_wheat.set_ylabel('Wheat Price (USD)')
ax_corn.set_ylabel('Corn Price (USD)')
ax_soybeans.set_ylabel('Soybeans Price (USD)')
ax_soybeans.set_xlabel('Date')

# 增加圖例
ax_wheat.legend()
ax_corn.legend()
ax_soybeans.legend()

# 顯示圖表
plt.show()



import matplotlib.pyplot as plt

# 創建一個包含三個子圖的圖表
fig, (ax_wheat, ax_corn, ax_soybeans) = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

# 繪製三條趨勢線
ax_wheat.plot(df_merged.index, df_merged['PWHEAMTUSDM'], color='tan', label='Wheat')
ax_corn.plot(df_merged.index, df_merged['PMAIZMTUSDM'], color='lightseagreen', label='Corn')
ax_soybeans.plot(df_merged.index, df_merged['PSOYBUSDM'], color='slategray', label='Soybeans')

# 設定標題和標籤
ax_wheat.set(title='Wheat Price Trend')
ax_corn.set(title='Corn Price Trend')
ax_soybeans.set(title='Soybeans Price Trend')
plt.xlabel('Date')

# 顯示圖例
ax_wheat.legend()
ax_corn.legend()
ax_soybeans.legend()

# 調整子圖的間距
plt.tight_layout()

# 顯示圖表
plt.show()



import matplotlib.pyplot as plt

# 創建一個圖和一個 Axes 對象
fig, ax = plt.subplots()

# 繪製三條線
ax.plot(df_merged.index, df_merged['PWHEAMTUSDM'], color='tan', label='Wheat')
ax.plot(df_merged.index, df_merged['PMAIZMTUSDM'], color='lightseagreen', label='Corn')
ax.plot(df_merged.index, df_merged['PSOYBUSDM'], color='slategray', label='Soybeans')

# 添加圖例
ax.legend()

# 添加標題和軸標籤
ax.set_title('Wheat, Corn, and Soybeans Prices Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Price (in USD)')

# 顯示圖形
plt.show()
fig.savefig('穀物折線圖.jpg',format = 'jpeg')





