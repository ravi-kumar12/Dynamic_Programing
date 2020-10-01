# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 07:23:30 2020
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
from prettytable import PrettyTable
from sys import maxsize

def MinCoinChange(arr,n,s):
    if l[n][s]!=-1:
        return l[n][s]
    else:
        if n==0 and s!=0:
            l[n][s]=maxsize
            return l[n][s]
        elif n!=0 and s==0:
            l[n][s]=0
            return l[n][s]
        elif n==0 and s==0:
            l[n][s]=maxsize
            return l[n][s]
        elif arr[n-1]<=s:
            l[n][s]=min(MinCoinChange(arr,n,s-arr[n-1])+1,MinCoinChange(arr,n-1,s))
            return l[n][s]
        else:
            l[n][s]=MinCoinChange(arr,n-1,s)
            return l[n][s]


n=int(input("No Of Type of Coin:"))
arr=sorted(list(map(int,input("Enter Coin Type:").split(" "))))
s=int(input("Enter Total Cash to Make:"))
l=[[-1]*(s+1) for i in range(n+1)]

ans=MinCoinChange(arr,n,s)
print("Min no Of Coin:{}".format(ans))
"""x=PrettyTable()
x.field_names=[i for i in range(s+1)]
for i in range(n+1):
    x.add_row(l[i])
print(x)"""