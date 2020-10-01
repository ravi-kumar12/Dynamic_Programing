def SubSetSum(arr,n,s):
    if n==0 and s!=0:
        return True
    elif n!=0 and s==0:
        return False
    elif n==0 and s==0:
        return True
    elif arr[n-1]<=s:
        return(SubSetSum(arr,n-1,s-arr[n-1]) or SubSetSum(arr,n-1,s))
    else:
        return SubSetSum(arr,n-1,s)
    
n=int(input("Enter No of Element:"))
lst=list(map(int,input("Enter Element:").split(" ")))
s=int(input("Enter sum to get:"))
ans=SubSetSum(lst,n,s)
print(ans)