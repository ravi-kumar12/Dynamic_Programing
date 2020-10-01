# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:13:34 2020
# =============================================================================
# Coin change problem: Maximum number of ways
# =============================================================================
Problem is basically combination of Unbounded Knapsack and cound the no of subset
Recursion+Momonisation
Time complexity- n**2
@author: RAVI
"""

from prettytable import PrettyTable
def CountWay(arr,n,s):
    if l[n][s]!=-1:
        return l[n][s]
    else:
        if n==0 and s!=0:
            l[n][s]=0
            return 0
        elif n!=0 and s==0:
            l[n][s]=1
            return 1
        elif n==0 and s==0:
            l[n][s]=1
            return 1
        elif arr[n-1]<=s:
            l[n][s]=CountWay(arr,n,s-arr[n-1])+CountWay(arr,n-1,s)
            return l[n][s]
        else:
            l[n][s]=CountWay(arr,n-1,s)
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