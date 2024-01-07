
get_ipython().system('pip install fredapi')



#Global price of wheat, corn, soybeans
from fredapi import Fred
fred = Fred(api_key='4e4a4ea389197ac12ee3036ee4cff0fc')
data_wheat = fred.get_series('PWHEAMTUSDM','1/1/2010')
data_corn = fred.get_series('PMAIZMTUSDM','1/1/2010')
data_soybeans = fred.get_series('PSOYBUSDM','1/1/2010')
data_CPI = fred.get_series('USACPALTT01CTGYM', '1/1/2010')

print(data_CPI)
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







