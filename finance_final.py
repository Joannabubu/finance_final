
get_ipython().system('pip install fredapi')



#Global price of wheat, corn, soybeans
from fredapi import Fred
fred = Fred(api_key='4e4a4ea389197ac12ee3036ee4cff0fc')
data_wheat = fred.get_series('PWHEAMTUSDM','1/1/2010')
data_corn = fred.get_series('PMAIZMTUSDM','1/1/2010')
data_soybeans = fred.get_series('PSOYBUSDM','1/1/2010')
data_CPI = fred.get_series('USACPALTT01CTGYM', '1/1/2010')

#print(data_CPI)
data_wheat.plot()
data_corn.plot()
data_soybeans.plot()
data_CPI.plot()


#讀取資料
frame_wheat = data_wheat.to_frame(name = 'PWHEAMTUSDM')
frame_corn = data_corn.to_frame(name = 'PMAIZMTUSDM')
frame_soybeans = data_soybeans.to_frame(name = 'PSOYBUSDM')
frame_CPI = data_CPI.to_frame(name='USACPALTT01CTGYM')
frame_wheat,frame_corn,frame_soybeans,frame_CPI




import pandas as pd
df_merged = pd.concat([frame_wheat, frame_corn, frame_soybeans],axis=1)



import matplotlib
import matplotlib.pyplot as plt



#繪製穀物趨勢圖
# 創建一個圖和一個 Axes 對象
fig, ax = plt.subplots(figsize=(10,7))

#set the background color
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 繪製三條線
ax.plot(df_merged.index, df_merged['PWHEAMTUSDM'], color='slategray', label='Wheat')
ax.plot(df_merged.index, df_merged['PMAIZMTUSDM'], color='steelblue', label='Corn')
ax.plot(df_merged.index, df_merged['PSOYBUSDM'], color='cadetblue', label='Soybeans')

# 添加圖例
ax.legend()

# 添加標題和軸標籤
ax.set_title('Wheat, Corn, and Soybeans Prices Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Price (in USD)')

# 顯示圖形
plt.show()
fig.savefig('穀物折線圖.jpg',format = 'jpeg',dpi=300, facecolor='white')


#繪製 CPI 圖型!

df_merged2 = pd.concat([frame_CPI],axis=1)

#畫布
fig, ax = plt.subplots(figsize=(11,8))

#set the background color
fig.patch.set_facecolor('white')
ax.set_facecolor('white')


# 繪製CPI 
ax.plot(df_merged2.index, df_merged2['USACPALTT01CTGYM'], color='peru', label='CPI')

ax.legend()

ax.set_title('CPI : All Items : Total for USA')
ax.set_xlabel('year')
ax.set_ylabel('Contribution to annual inflation')

plt.show()
fig.savefig('USA_CPI.jpg',format = 'jpeg',dpi=300, facecolor='white')

#合併兩張圖表 (穀物 & CPI)
fig, ax1 = plt.subplots(figsize=(11,8))
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')

#穀物之三條線
line1 = ax1.plot(df_merged.index, df_merged['PWHEAMTUSDM'], color='slategray', label='Wheat')
line2 = ax1.plot(df_merged.index, df_merged['PMAIZMTUSDM'], color='steelblue', label='Corn')
line3 = ax1.plot(df_merged.index, df_merged['PSOYBUSDM'], color='cadetblue', label='Soybeans')
 
#將位置放在左上角
ax1.legend(loc='upper left')
ax1.set_title('Data of wheat, corn, soybeans and CPI')
ax1.set_xlabel('Year')
ax1.set_ylabel('Price (in USD)')

#第二個 Y 軸
ax2 = ax1.twinx()

#繪製 CPI 
line4 = ax2.plot(df_merged2.index, df_merged2['USACPALTT01CTGYM'], color='peru', label='CPI')

#將位置放在 右上角
ax2.legend(loc = 'upper right')

ax2.set_ylabel('Contribution to annual inflation - CPI')

plt.show()
fig.savefig('合併.jpg', format='jpeg', dpi=300, facecolor='white')