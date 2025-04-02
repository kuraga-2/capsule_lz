import getpass
from datetime import date, datetime
import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime


Crude = pd.read_csv('crude-oil-price.csv')
Brent = pd.read_csv('BrentOilPrices.csv')

for i in range(0, len(Crude)):
    strr = Crude.loc[i, 'date']
    Crude.loc[i, 'date'] = strr[0 : 10]
for i in range(0,3200):
    str1 = Brent.loc[i, 'date']
    data1 = str1.split('-')
    year1 = '19' + data1[2]
    data1[2] = year1
    match data1[1]:
        case 'Jan': 
            data1[1] = "01"
        case 'Feb': 
            data1[1] = "02"
        case 'Mar': 
            data1[1] = "03"
        case 'Apr': 
            data1[1] = "04"
        case 'May': 
            data1[1] = "05"
        case 'Jun': 
            data1[1] = "06"
        case 'Jul': 
            data1[1] = "07"
        case 'Aug': 
            data1[1] = "08"
        case 'Sep': 
            data1[1] = "09"
        case 'Oct': 
            data1[1] = "10"
        case 'Nov': 
            data1[1] = "11"
        case 'Dec': 
            data1[1] = "12"
    Brent.loc[i, 'date'] = datetime.date(int(data1[2]),int(data1[1]),int(data1[0]))
for i in range(3200,8360):
    str11 = Brent.loc[i, 'date']
    data1 = str11.split('-')
    year1 = '20' + data1[2]
    data1[2] = year1
    match data1[1]:
        case 'Jan': 
            data1[1] = "01"
        case 'Feb': 
            data1[1] = "02"
        case 'Mar': 
            data1[1] = "03"
        case 'Apr': 
            data1[1] = "04"
        case 'May': 
            data1[1] = "05"
        case 'Jun': 
            data1[1] = "06"
        case 'Jul': 
            data1[1] = "07"
        case 'Aug': 
            data1[1] = "08"
        case 'Sep': 
            data1[1] = "09"
        case 'Oct': 
            data1[1] = "10"
        case 'Nov': 
            data1[1] = "11"
        case 'Dec': 
            data1[1] = "12"
    Brent.loc[i, 'date'] = datetime.date(int(data1[2]),int(data1[1]),int(data1[0]))
for i in range(8360,len(Brent)):
    str2 = Brent.loc[i, 'date']
    data2 = str2.split(' ')
    month = data2[1]
    data2[1] = month[0:2]
    match data2[0]:
        case 'Jan': 
            data2[0] = "01"
        case 'Feb': 
            data2[0] = "02"
        case 'Mar': 
            data2[0] = "03"
        case 'Apr': 
            data2[0] = "04"
        case 'May': 
            data2[0] = "05"
        case 'Jun': 
            data2[0] = "06"
        case 'Jul': 
            data2[0] = "07"
        case 'Aug': 
            data2[0] = "08"
        case 'Sep': 
            data2[0] = "09"
        case 'Oct': 
            data2[0] = "10"
        case 'Nov': 
            data2[0] = "11"
        case 'Dec': 
            data2[0] = "12"
    Brent.loc[i, 'date'] = datetime.date(int(data2[2]),int(data2[0]),int(data2[1]))

merged_df = pd.merge(Crude, Brent, on='date')
merged_df.info()

x = merged_df['date'].tolist()
y1 = merged_df['price1'].tolist()
y2 = merged_df['price2'].tolist()
plt.plot(x, y1, label='Crude')
plt.plot(x, y2, label='Brent')
plt.xlabel('Date')
plt.ylabel('Prise')
plt.title('График зависимости цены от времени')
plt.show()