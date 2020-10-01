# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:18:51 2020
Definition: Given types of items of different values and volumes, find the most
valuable set of items that fit in a knapsack of fixed volume. The number of 
items of each type is unbounded. This is an NP-hard combinatorial optimization 
problem

Time Complexity- n**2
@author: RAVI
"""

from prettytable import PrettyTable

def knapsack(element,n,wt):
    global knapsacktable
    if knapsacktable[n][wt]!=-1:
        return knapsacktable[n][wt]
    else:
        if n==0 or wt==0:
            knapsacktable[n][wt]= 0
            return 0
            
        elif element[n-1][1]<=wt:
            knapsacktable[n][wt]= max(knapsack(element,n,wt-element[n-1][1])+element[n-1][0],knapsack(element,n-1,wt))
            return knapsacktable[n][wt]
        else:
            knapsacktable[n][wt]=knapsack(element,n-1,wt)
            return knapsack(element,n-1,wt)
    

def showknapsacktable():  
        x=PrettyTable()
        x.field_names=[i for i in range(W+1)]
        for i in range(n+1):
            x.add_row(knapsacktable[i])
        print(x)     
        
def elementAdd():
        ans=[]
        max_profit=knapsacktable[n][W]
        
        i=n
        while(max_profit>0):
            j=knapsacktable[i].index(max_profit)
            count=0
            while knapsacktable[i][j]==knapsacktable[i-1][j] and i>=0:
                i-=1
            count=max_profit//lst[i-1][0]
            max_profit-=count*lst[i-1][0]
            
            ans.append([lst[i-1][0],lst[i-1][1],count])
            print(ans)
        for i in range(len(ans)):
            print("ELemnt no:{EleNo:} is added {Count} time".format(EleNo=lst.index([ans[i][0],ans[i][1]])+1,Count=ans[i][2]))
            print("Profit:{0},Weight:{1},Count:{2},TotalProfit=Profit*Count={3}".format(ans[i][0],ans[i][1],ans[i][2],ans[i][0]*ans[i][2]))
            print()
        ele=[] 
        finalans=[]
        for i in range(len(ans)):
            if ans[i]==-1:
                continue
            ele.append(ans[i][0])
            ele.append(ans[i][1])
            ele.append(ans[i][2])
            for j in range(i+1,len(ans)):
                if ans[i][0]==ans[j][0] and ans[i][1]==ans[j][1]:
                    ele[2]+=ans[j][2]
                    ans[j]=-1
                    
                
            finalans.append(ele)
            ele=[]
        print("Final Answer Is:{}".format(finalans))
        return(finalans[0:n])
def showElementAdded(elementAdded):
        x=PrettyTable()
        x.field_name=[i for i in lst]
        x.add_row(elementAdded)
        print(x)
n=int(input("Enter no of Element:"))    #no of input
lst=[]
print("Enter profit And Corresponding weight:")
for i in range(n):  
    lst.append(list(map(int,input().split(" "))))
W=int(input("Enter knapsack capacity:"))
knapsacktable=[[-1]*(W+1) for i in range(n+1)]
max_profit=knapsack(lst,n,W)
print(max_profit)
showknapsacktable()
showElementAdded(elementAdd())