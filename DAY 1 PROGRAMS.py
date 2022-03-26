Day 1
#bmi calculation
height = 120
weight = 50
bmi=height/weight
print(bmi) 

#GETTING INPUT FROM USER
name=str(input("enter name"))
height=int(input("enter height value"))
weight=int(input("enter weight value"))
bmi=height/weight
print("the bmi of",name,"is",bmi)


#FINDING DATATYPE
a=1
type(a)

#average findings
a=[1,2,3,5,6,7]
average=sum(a)/len(a)
print(average)

#list (LIST IS MUTABLE)
listA=[1,2,3,5]
listA[3]=7
listA

#TUPLE (IMMUTABLE)
tupleA=(1,2,"kiruba",5)
tupleA[3]="RAVI"
tupleA

#set (IF TWO OR MORE VALUES REPETS IT RETURNS SINGLE VALUE OF IT)
SetA={1,2,2,3,4,5,"Str"}
print(SetA)

#dictionary()
dict={}
print("empty dictionary:")
print(dict)

#dictionary(MAPPINGS OF UNIQUE KEY TO VALUES AND MUTABLE)
dict=({1:'i',2:'am',3:'good'})
print (dict)

#conditional loops
EXAMPLE 1:
a=10
b=12
a>b
EXAMPLE2:
a=10
b=1
a>b

#if conditionL LOOPS
EXAMPLE 1:
a=12
b=12
if a==b:
    print("a is not equal to b")
    
EXAMPLE 2:
 a=1
 b=2
if a==b:
    print("falseb")
    
EXAMPLE 3:
mean=571.655
if mean<=1000:
    print("it has the worst trade")
else:
    print("it has the better trade")
    
# GETTING INPUT FROM USER
name1=input("enter name1")
name2=input("enter name2")
mean1=input("enter mean1")
mean2=input("enter mean2")
if mean1>mean2:
    print("name1 is the highest")
else:
    print("name2 is the highest")


#consistent code
print("enter the name1")
name=str( input())
print("enter the name2")
name=str( input())
print("enter mean1")
mean=int(input())
print("enter mean2")
mean=int(input())
if mean1 > mean2:
    print(name1,"is better in trading than",name2)

#THREE CONDITIONS
a=10
b=20
c=30
if(a > b > c):
    print("a is greater than b and c")
elif(a>b>c):
    print("b is greater than a and c")
else:
    print("c is greater")

#ANOTHER WAY

a=50
b=20
c=30
if(a&b==c):
     print("a and b is equal to c")
elif(a&c==b):
     print("a and c is equalto b")
else:
     print("c is greater than all")

#range
listA=[1,2,3,4,5]
for i in range(1,5):
    for j in range(2,3):
        print(i,j)

#NESTED Loop
 for i in range(1,12):
     for j in range(7,9):
         print(i,j)
        
EXAMPLE 2:
group_A = ["RCB","mi","csk","dc"]
group_B = ["SRH","KKR","RR","PKS"]
for i in group_A:
    for j in group_B:
        print(i,j)
EXAMPLE 3:
group_A = ["RCB","CSK","SRH"]
group_B = ["SRH","KKR","MOM"]
for i in group_A:
    for j in group_B:
        print(i, "vs",j)
    
EXAMPLE 4:
listA=[1,2,3,4,5]
for i in range(1,5):
    for j in range(2,3):
        print(i,j)

#SELECTING GROUP
print("enter name")
name=str(input())
print("enter register number")
register_number=int(input())
print("enter total")
total=int(input())
if (total >= 490):
    print("eligible for first group")
elif total >= 450:
    print("eligible for second group")
else:
    print("last group")
       

    #dictionary
    days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]*4
    teacher=["rem","tom","pol"]
    a=0
    saturdaycount=0
    for i in days:
        if i == "sunday":
            print("sunday is holiday")
            continue
        if i == "saturday":
            saturdaycount+=1
            if saturdaycount%2==0:
                print("saturday is holiday")
                continue
        if a==3:
            a=0
        print(i,teacher[a])
        a=a+1
            
#STATISTICS
from statistics import NormalDist
nd = NormalDist(mu = 711,sigma=29)
nd.cdf(682)
nd.cdf(740)
nd.cdf(752)-nd.cdf(687)

import numpy as np
listA=[1,3,5,7,9,11,13,12,14,15,13,17]
type(listA)
e=np.array(listA) #assumption variable for convienience
type(e)
np.mean(e)
np.median(e)
e[0:8:3] #step by selection
e.mean()  
e=np.array([[2,3,4,5,6,7],[10,19,18,17,16,15]])   
e.ndim
e=np.array([[[2,3,4,5,6,7],[10,19,18,17,16,15],[1,5,8,7,9,16,]]])   
e.ndim
e[0]           
e[0,0]  
e[0,1]
e.dtype
e.shape

#IMPORTING FROM PANDAS
import pandas as pd
data=pd.read_excel("C:/Users/Dell/Documents/Book1.xlsx")
print(data.japan.mean())
print(data.japan.median())
print(data.japan.mode())

            
from statistics import NormalDist
x1=0.8413447
sigma=200
mean=2000
nd=NormalDist(mean,sigma)
nd.cdf(100-0.8413447)
    
    
    






