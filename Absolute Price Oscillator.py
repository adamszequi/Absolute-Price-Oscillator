# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 00:00:25 2019

@author: Dell
"""

'''

The absolute price oscillator is a class of indicators that
builds on top of moving averages of prices to capture specific short-term deviations in
prices.

The absolute price oscillator is computed by finding the difference between a fast
exponential moving average and a slow exponential moving average. Intuitively, it is
trying to measure how far the more reactive EMA is deviating from the more
stable EMA. A large difference is usually interpreted as one of two things:
instrument prices are starting to trend or break out, or instrument prices are far away from
their equilibrium prices, in other words, overbought or oversold:

This is an implementation of the absolute price oscillator, with the faster EMA using a period of 10
days and a slower EMA using a period of 40 days, and default smoothing factors being 2/11
and 2/41, respectively, for the two EMAs.

'''
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#Create variables for fast EMA
nFast=10#umOfPeriodsForFast
'''

the shorter the time period,
the more reactive the EMA is to new price observations; in other words, the EMA
converges to new price observations faster and forgets older observations faster, also
referred to as Fast EMA.

'''
smoothingConstantFast=2/(nFast+1)
EMApriceFast=0

#Create variables for Slow EMA
nSlow=40
''' 
The longer the time period, the less reactive the EMA is to new
price observations; that is, EMA converges to new price observations slower and forgets
older observations slower, also referred to as Slow EMA.

'''
smoothingConstantSlow=2/(nSlow+1)
EMApriceSlow=0


#Create lists to hold newly calculated values
EMAfastValues=[]
EMAslowValues=[]
APO=[]

#download data
data=yf.download('GOOG',start='2015-9-1',end='2018-11-11')
adjustedClose=data['Adj Close']

#Calulate fast and close prices
for price in adjustedClose:
    if EMApriceFast==0:
        EMApriceFast=price
        EMApriceSlow=price
    
    else:
        EMApriceFast=(price - EMApriceFast) * smoothingConstantFast + EMApriceFast
        EMApriceSlow=(price - EMApriceSlow) * smoothingConstantSlow + EMApriceSlow
    
    EMAfastValues.append(EMApriceFast)
    EMAslowValues.append(EMApriceSlow)
    APO.append(EMApriceFast-EMApriceSlow)

#create dataframe of values    
df=pd.DataFrame(adjustedClose,index=data.index)
df['EMAfast']=EMAfastValues
df['adjustedPrice']=adjustedClose
df['EMAslow']=EMAslowValues
df['APO']=APO

#declare variables for plotting graph
close=df['adjustedPrice']
EMAfast=df['adjustedPrice']
EMAslow=df['EMAslow']
APO=df['APO']

#plot figures
fig=plt.figure()
axis=fig.add_subplot(211,ylabel='EMA Fast and Slow')
close.plot(ax=axis,color='g',lw=2.,legend=True)
EMAfast.plot(ax=axis,color='b',lw=2.,legend=True)
EMAslow.plot(ax=axis,color='r',lw=2.,legend=True)
axis2=fig.add_subplot(212,ylabel='APO of Google price')
APO.plot(ax=axis2, color='black', lw=2., legend=True)
plt.show()







        
    