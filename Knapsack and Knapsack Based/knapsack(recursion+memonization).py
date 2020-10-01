from prettytable import PrettyTable

def knapsack(element,n,wt):
    global knapsacktable
    if knapsacktable[n][wt]==-1:
        if n==0 or wt==0:
            knapsacktable[n][wt]= 0
            return 0
            
        elif element[n-1][1]<=wt:
            knapsacktable[n][wt]= max(knapsack(element,n-1,wt-element[n-1][1])+element[n-1][0],knapsack(element,n-1,wt))
            return max(knapsack(element,n-1,wt-element[n-1][1])+element[n-1][0],knapsack(element,n-1,wt))
        else:
            knapsacktable[n][wt]=knapsack(element,n-1,wt)
            return knapsack(element,n-1,wt)
    else:
        return knapsacktable[n][wt]

def showknapsacktable():  
        x=PrettyTable()
        x.field_names=[i for i in range(W+1)]
        for i in range(n+1):
            x.add_row(knapsacktable[i])
        print(x)     
        
def elementAdd():
        ans=[0]*(n+1)
        max_profit=knapsacktable[n][W]
        i=n
        while(max_profit>0):
            j=knapsacktable[i].index(max_profit)
            while knapsacktable[i][j]==knapsacktable[i-1][j] and i>=0:
                i-=1
            ans[i]=1
            max_profit-=lst[i-1][0]
            i-=1
        for i in range(len(ans)):
            if ans[i]==1:
                print("ELemnt {} is added".format(i))
            
        return(ans[1:n+1])
def showElementAdded(elementAdded):
        x=PrettyTable()
        x.field_name=[i for i in lst]
        x.add_row(elementAdded)
        print(x)
n=4#int(input("Enter no of Element:"))    #no of input
lst=[[5,2],[2,3],[3,4],[5,5]]
#print("Enter profit And Corresponding weight:")
#for i in range(n):  
#    lst.append(list(map(int,input().split(" "))))
W=7#int(input("Enter knapsack capacity:"))
knapsacktable=[[-1]*(W+1) for i in range(n+1)]
max_profit=knapsack(lst,n,W)
print(max_profit)
showknapsacktable()
showElementAdded(elementAdd())