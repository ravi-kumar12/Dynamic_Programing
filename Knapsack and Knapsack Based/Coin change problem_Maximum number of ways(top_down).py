# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:52:47 2020
# =============================================================================
# Coin change problem: Maximum number of ways
# =============================================================================
Problem is basically combination of Unbounded Knapsack and cound the no of subset
Top Down
Time complexity- n**2
@author: RAVI
"""

from prettytable import PrettyTable
def CountWay(arr,n,s):
    for i in range(n+1):
        for j in range(s+1):
            if i==0 and j!=0:
                l[i][j]=0
            elif i!=0 and j==0:
                l[i][j]=1
            elif i==0 and j==0:
                l[i][j]=1
            elif arr[i-1]<=j:
                l[i][j]=l[i-1][j-arr[i-1]]+l[i-1][j]
            else:
                l[i][j]=l[i-1][j]
    return l[n][s]

n=int(input("Enter No of Coin type:"))
arr=sorted(list(map(int,input("Enter Coin Value:").split())))
s=int(input("Enter sum to get:"))
l=[[-1]*(s+1) for i in range(n+1)]
ans=CountWay(arr,n,s)
print(ans)

x=PrettyTable()
x.field_names=[i for i in range(s+1)]
for i in l:
    x.add_row(i)
print(x)