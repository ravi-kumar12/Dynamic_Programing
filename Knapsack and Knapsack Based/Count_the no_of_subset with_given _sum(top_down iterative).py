from prettytable import PrettyTable
def CountSubset(arr,n,s,l):
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

"""def PrintingSubset(arr,n,s):
    req_list=[]
    while (len(arr)!=0):
        l=[[-1]*(s+1) for i in range(n+1)]
        CountSubset(arr,n,s,l)
        i=n
        j=s
        lst=[]
        while s!=0:
            while l[i][j]==l[i-1][j]:
                i-=1
            lst.append(arr[i-1])        #not working
            j=s-arr[i-1]                #subset generation can be done by back tracking algo
            i-=1
        req_list.append(lst)
        for i in lst:
            arr.remove(i)
        n-=len(lst)
      
    for i in req_list:
        print(i)"""        
    

n=7#int(input("Enter No of Element:"))
arr=[2,3,5,6,8,10,15]#sorted(list(map(int,input().split())))
s=15#int(input("Enter sum to get:"))
l=[[-1]*(s+1) for i in range(n+1)]
ans=CountSubset(arr,n,s,l)
print(ans)

x=PrettyTable()
x.field_names=[i for i in range(s+1)]
for i in l:
    x.add_row(i)
print(x)
#PrintingSubset(arr,n,s)  not working

