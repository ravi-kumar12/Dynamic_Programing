def knapsack(element,n,wt):
    if n==0 or wt==0:
        return 0
    elif element[n-1][1]<=wt:
         return max(knapsack(element,n-1,wt-element[n-1][1])+element[n-1][0],knapsack(element,n-1,wt))
    else:
        return knapsack(element,n-1,wt)
        

n=int(input("Enter no of Element:"))    #no of input
lst=[]
print("Enter profit And Corresponding weight:")
for i in range(n):  
    lst.append(list(map(int,input().split(" "))))
W=int(input("Enter knapsack capacity:"))
max_profit=knapsack(lst,n,W)
print(max_profit)