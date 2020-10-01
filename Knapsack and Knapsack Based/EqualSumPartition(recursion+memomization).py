"""Partition problem is to determine whether a given set can be partitioned into 2 subsets such that the sum of elements in both subsets is same."""
from prettytable import PrettyTable
def EqualSumPartition(n,arr):
    if sum(arr)%2!=0:
        return False
    else:
        global l
        global x
        s=sum(arr)//2
        x=PrettyTable()
        x.field_names=[i for i in range(s+1)]
        l=[[None]*(s+1) for i in range(n+1)]
        res=SubSetSum(arr,n,s)
        if res:
            for i in range(n+1):
                x.add_row(l[i])
        return res

def SubSetSum(arr,n,s):
    global l
    if l[n][s]!=None:
        return l[n][s]
    
    if n==0 and s!=0:
        l[n][s]=False
        return False
    elif n!=0 and s==0:
        l[n][s]=True
        return True
    elif n==0 and s==0:
        l[n][s]=True
        return True
    elif arr[n-1]<=s:
        l[n][s]= (SubSetSum(arr,n-1,s-arr[n-1]) or SubSetSum(arr,n-1,s))
        return (SubSetSum(arr,n-1,s-arr[n-1]) or SubSetSum(arr,n-1,s))
    else:
        l[n][s]=SubSetSum(arr,n-1,s)
        return SubSetSum(arr,n-1,s)


n=6#int(input("Enter No of Element:"))
arr=[2,3,5,6,8,10]#list(map(int,input("Enter Element").split(" ")))
ans=EqualSumPartition(n,arr)

print(ans)
print(x)
print(l)
if ans:
    s=sum(arr)//2
    i=n
    j=s
    lst1=[]
    while s!=0:
            while i>1 and l[i][j]==l[i-1][j]:
                i-=1
            lst1.insert(0,arr[i-1])
            s-=arr[i-1]
            i-=1
            j=s
print(lst1)
lst2=arr
for i in lst1:
    lst2.remove(i)
print(lst2)        

    