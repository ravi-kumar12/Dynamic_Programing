# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:21:50 2020
# =============================================================================
# Coin change problem: Minimum number of coins
#
#Problem statement: The problem statement is: If we want to make change for a 
#                   given value (N) of cents, and we have an infinite supply of
#                   each of C = { C 1 C_{1} C1​, C 2 C_{2} C2​, … , C M C_{M} CM​}
#                   valued coins, what is the minimum number of coins required 
#                    to make the change?
#Hint: Unbounded Knapsack with min finding
#Time Complexity-n**2
# =============================================================================
@author: RAVI
"""
from sys import maxsize
#from prettytable import PrettyTable


def MinCoinChange(arr,n,s):
    for i in range(n+1):
        for j in range(s+1):
            if i==0 and j!=0:
                l[i][j]=maxsize
            elif i==0 and j==0:
                l[i][j]=0 # or sys.maxsize
            elif i!=0 and j==0:
                l[i][j]=0
            elif arr[i-1]<=j:
                l[i][j]=min((l[i][j-arr[i-1]]+1),(l[i-1][j]))
            else:
                l[i][j]=l[i-1][j]
    return l[n][s]

"""def TableCreation():
    x=PrettyTable()
    x.field_names=[i for i in range(s+1)]
    for i in range(n+1):
       x.add_row(l[i])
    return x"""
    


n=int(input("No Of Type of Coin:"))
arr=sorted(list(map(int,input("Enter Coin Type:").split(" "))))
s=int(input("Enter Total Cash to Make:"))
l=[[-1]*(s+1) for i in range(n+1)]

ans=MinCoinChange(arr,n,s)
print(ans)
 
#y=TableCreation()
#print(y)
