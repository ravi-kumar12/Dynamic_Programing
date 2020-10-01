# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:32:51 2020
This is greedy apporach and it is wrong one.
This will not for input like :
    Enter No of Element:3
    Enter profit And Corresponding weight:
    
    2 2
    
    2 2
    
    3.1 3
    
    Enter Capacity Of Knapsack:4
    [[3.1, 3.0, 1]]
    ELement with weight:3.0 and profit:3.1 is added 1 times
    Max Profit is:3.1
    
    Right answer should be 2 2 added twice in unbounded
    and in 0/1 (2,2) and (2,2)
Unbounded Knapsack
@author: RAVI
"""

n=int(input("Enter No of Element:"))
lst=[]
print("Enter profit And Corresponding weight:")
for i in range(n):  
    lst.append(list(map(float,input().split(" "))))
lst.sort(key=lambda x:x[1]) 
capacity=int(input("Enter Capacity Of Knapsack:"))
price_per_unit_wt=[(i/j) for i,j in lst]

i=n-1
while lst[i][1]>capacity:
    i-=1
lst1=lst[0:i+1]
price_per_unit=price_per_unit_wt[0:i+1]

ans=[]
while capacity>0:
    if capacity<lst1[0][1]:
        break
    count=0
    max_ele=max(price_per_unit)
    j=price_per_unit.index(max_ele)
    
    while capacity>=lst1[j][1]:
        capacity-=lst1[j][1]
        count+=1
    ans.append([lst1[j][0],lst1[j][1],count])
    lst2=[]
    for i in range(len(lst1)):
        if lst1[i][1]<=capacity:
            lst2.append(lst1[i])
    lst1=lst2
    if len(lst1)==0:
        break
    
    price_per_unit=price_per_unit[0:len(lst1)]
print(ans)
max_profit=0    
for i in ans:
    max_profit+=i[0]*i[2]  
for i in ans:
    print("ELement with weight:{0} and profit:{1} is added {2} times".format(i[1],i[0],i[2]))
    
print("Max Profit is:{}".format(max_profit))     








