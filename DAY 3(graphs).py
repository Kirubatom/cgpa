# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:09:05 2022

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(80,2,100)  
plt.hist(data)
plt.boxplot(data)
import numpy as np
import matplotlib.pyplot as plt
list1=[100,80,70,60,50,150]
plt.hist(data)
plt.boxplot(data)

#calculating intervals
from scipy import stats
stats.norm.interval(0.95,loc=0,scale=1)

import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,4,6,8,10])
y=np.array([12,10,9,6,5])
plt.plot(x)
plt.plot(y,'o')  #dot plot
plt.plot(x,y,'o') #scatter plot
plt.plot(x,y) #line plot
plt.plot(x)   #2.run together
plt.plot(y)   #2.run together
plt.plot(y,'s:g')
plt.plot(y,'^:b') #triangle dotted blue color
plt.plot(x,y)
plt.xlabel('height')
plt.ylabel('weight')
plt.title('height vs weight') #title of a graph
plt.grid() #creating grid
plt.grid(color='red')
import matplotlib.pyplot as plt
x=['yellow','red','blue','pink','black']
y=[10,12,14,16,18]
plt.bar(x,y,color='red')   #bar graph
plt.pie(y) #pie graoh
plt.scatter(x,y) #only numbers
import seaborn as sns
tips=sns.load_dataset("tips") #requires intrnet
tips.head()  #analysis of domain knowledge
tips.columns
sns.scatterplot(x='total_bill',y='tip',data=tips,hue='smoker') #here hew is smoker
#here we can only have one hew ata a tym
sns.scatterplot(x='total_bill',y='tip',data=tips,hue='sex',palette={"Male":'blue',"Female":'pink'})
import matplotlib.pyplot as plt
plt.xlabel('bill')  #labeling x axis
plt.ylabel('tips') #labeling y axis
sns.relplot(x='total_bill',y='tip',data=tips,kind='scatter',hue='sex')









