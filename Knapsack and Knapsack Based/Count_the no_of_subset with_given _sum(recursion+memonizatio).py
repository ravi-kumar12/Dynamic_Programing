from prettytable import PrettyTable
def CountSubset(arr,n,s):
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
            l[n][s]=CountSubset(arr,n-1,s-arr[n-1])+CountSubset(arr,n-1,s)
            return l[n][s]
        else:
            l[n][s]=CountSubset(arr,n-1,s)
            return l[n][s]
        
n=3#int(input("Enter No of Element:"))
arr=[3,4,6]#sorted(list(map(int,input().split())))
s=7#int(input("Enter sum to get:"))
l=[[-1]*(s+1) for i in range(n+1)]
ans=CountSubset(arr,n,s)
print(ans)

x=PrettyTable()
x.field_names=[i for i in range(s+1)]
for i in l:
    x.add_row(i)
print(x)