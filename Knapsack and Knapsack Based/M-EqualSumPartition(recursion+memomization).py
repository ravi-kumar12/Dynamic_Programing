"""Partition problem is to determine whether a given set can be partitioned into m
no of subsets such that the sum of elements in both subsets is same
Time Complexity- m*n**2
m>=1 (u can edit a little for m=0)"""


def EqualSumPartition(n,arr,m):
    global l
    req_arrays=[]
    counter=0
    while len(arr)!=0 and m!=0:
        if m==1:
            req_arrays.append(arr)
            counter=1
            break
        elif sum(arr)%m!=0:
            print("ravi1")
            return False
        else:
            s=sum(arr)//m
            l=[[None]*(s+1) for i in range(n+1)]
            res=SubSetSum(arr,n,s)
            if res==False:
                print("ravi2")
                return False
            if res:
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
                req_arrays.append((lst1))
                print(lst1)
                for i in lst1:
                    arr.remove(i)
                print(arr)
                n=n-len(lst1)
                m=m-1
            
    if counter==1:
        for i in req_arrays:
            print(i)
        return True
    else:
        return False
                   

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
    


n=5#int(input("Enter No of Element:"))
arr=[1,2,3,4,5,5,6,7,8,9,10]#sorted(list(map(int,input("Enter Element:").split(" "))))
m=6#int(input("no of subset to get:"))
ans=EqualSumPartition(n,arr,m)
print(ans)