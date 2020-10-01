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
                elif self.lst[i][1]<=j:#self.w and j-self.lst[i][1]>=0:
                    l[i][j]=max(l[i-1][j-self.lst[i][1]]+self.lst[i][0],l[i-1][j]) #basic algo
                else:
                    l[i][j]=l[i-1][j]
        return(l)
    def elementAdd(self):
        ans=[0]*(self.n+1)
        max_profit=self.knapsacktable[self.n][self.w]
        i=n
        while(max_profit>0):
            j=self.knapsacktable[i].index(max_profit)
            while self.knapsacktable[i][j]==self.knapsacktable[i-1][j] and i>=0:
                i-=1
            ans[i]=1
            max_profit-=self.lst[i][0]
            i-=1
        for i in range(len(ans)):
            if ans[i]==1:
                print("ELemnt {} is added".format(i))
            
        return(ans[1:n+1])
        
        
        
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