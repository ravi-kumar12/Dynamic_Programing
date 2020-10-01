# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:31:57 2020
The original problem statement is equivalent to: 
    find the number of ways to gather a subset of nums that needs to be positive (P), 
    and the rest negative (N), such that their sum is equal to target
Solution:
    Problem equivalent to Count the number of subsets with a given difference problem
    for example: for array [1,1,2,3],target sum 1
                 we have to put + and - before no so as to obtain 1
                 this can be done as:
                     +1-1-2+3=1
                     -1+1-2+3=1
                     +1+1+2-3=1
    we can also view above problem to divide no into two subset st s1-s2=d where d is 
    targetted sum.
    Hence the problem is basically find no of way two subset can be form st their different
    is d

@author: RAVI
"""

def CountingSubsetWithGivenSum(arr,n,s):
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
            l[n][s]=CountingSubsetWithGivenSum(arr,n-1,s-arr[n-1]) + CountingSubsetWithGivenSum(arr, n-1,s)
            return l[n][s]
        else:
            l[n][s]= CountingSubsetWithGivenSum(arr,n-1,s)
            return l[n][s]
            
n=5#int(input("Enter No of No:"))
arr=[1,4,6,10,12]#sorted(list(map(int,input("Enter array:").split(" "))))
d=1#int(input("Enter Targetted sum::"))
s1=(sum(arr)+d)//2
l=[[-1]*(s1+1) for i in range(n+1)]
ans=CountingSubsetWithGivenSum(arr,n,s1)
print(ans)