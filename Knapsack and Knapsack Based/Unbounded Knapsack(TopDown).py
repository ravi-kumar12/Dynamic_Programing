# -*- coding: utf-8 -*-
"""
Definition: Given types of items of different values and volumes, find the most
valuable set of items that fit in a knapsack of fixed volume. The number of 
items of each type is unbounded. This is an NP-hard combinatorial optimization 
problem

Time Complexity- n**2

"""

from prettytable import PrettyTable

class knapsack:
    
    def __init__(self,n,lst,w):
        self.n=n
        self.lst=lst
        self.w=w
        self.knapsacktable=self.knapsacktablecreate()
        self.elementAdded=self.elementAdd()
        self.maxprofit=self.knapsacktable[self.n][self.w]
    
    def knapsacktablecreate(self):
        l=[[-1]*(self.w+1) for i in range(self.n+1)]
        for i in range(self.n+1):
            for j in range(self.w+1):
                if (i==0) or (j==0):
                    l[i][j]=0           #initialising 0 for w=0 and n=0
                elif self.lst[i][1]<=j:#equivalent to self.w and j-self.lst[i][1]>=0:
                    l[i][j]=max(l[i][j-self.lst[i][1]]+self.lst[i][0],l[i-1][j]) #basic algo,list is preinitialise with [0,0]
                else:                                                            #so no j-self.lst[i-1][1]
                    l[i][j]=l[i-1][j]
        return(l)
    def elementAdd(self):
        ans=[]
        max_profit=self.knapsacktable[self.n][self.w]
        
        i=self.n
        while(max_profit>0):
            j=self.knapsacktable[i].index(max_profit)
            count=0
            while self.knapsacktable[i][j]==self.knapsacktable[i-1][j] and i>=0:
                i-=1
            count=max_profit//lst[i][0]
            max_profit-=count*lst[i][0]
            
            ans.append([self.lst[i][0],self.lst[i][1],count])
            
            
        for i in range(len(ans)):
            print("ELemnt no:{EleNo:} is added {Count} time".format(EleNo=self.lst.index([ans[i][0],ans[i][1]]),Count=ans[i][2]))
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
        
        
        
    def showknapsacktable(self):  
        x=PrettyTable()
        x.field_names=[i for i in range(self.w+1)]
        for i in range(self.n+1):
            x.add_row(self.knapsacktable[i])
        print(x)
    
    def showElementAdded(self):
        x=PrettyTable()
        x.field_name=[i for i in lst]
        x.add_row(self.elementAdded)
        print(x)

n=int(input("Enter no of Element:"))    #no of input
lst=[[0,0]]
print("Enter profit And Corresponding weight:")
for i in range(n):  
    lst.append(list(map(int,input().split(" "))))
W=int(input("Enter knapsack capacity:"))      #weight capability of knapsack
knapsack1=knapsack(n,lst,W)
print("KnapsackTable:")
knapsack1.showknapsacktable()
print("Element Added")
knapsack1.showElementAdded()
print("Max Profit=",knapsack1.maxprofit)