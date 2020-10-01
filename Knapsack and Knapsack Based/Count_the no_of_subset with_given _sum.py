def CountSubset(arr,n,s):
    if n==0 and s!=0:
        return 0
    elif n!=0 and s==0:
        return 1
    elif n==0 and s==0:
        return 1
    elif arr[n-1]<=s:
        return (CountSubset(arr,n-1,s-arr[n-1]))+(CountSubset(arr,n-1,s))
    else:
        return CountSubset(arr,n-1,s)
        
n=6#int(input("Enter No of Element:"))
arr=[2,3,5,6,8,10]#sorted(list(map(int,input().split())))
s=10#int(input("Enter sum to get:"))
ans=CountSubset(arr,n,s)
print(ans)