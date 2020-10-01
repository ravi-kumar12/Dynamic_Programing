"""Count the number of subsets with a given difference problem"""
"""Solution: let say s1 and s2:
    s1-s2=d                    d being the different
    s1+s2=sum(arr)
    equating both statement:
        s1=(sum(arr)+d)/2
    so basically we have to find the no subset with given sum 
    s2 will adjust itself
"""
def CountingSubsetWithGivenSum(arr,n,s):
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
            l[n][s]=CountingSubsetWithGivenSum(arr,n-1,s-arr[n-1]) + CountingSubsetWithGivenSum(arr, n-1,s)
            return l[n][s]
        else:
            l[n][s]= CountingSubsetWithGivenSum(arr,n-1,s)
            return l[n][s]
            
n=3#int(input("Enter No of No:"))
arr=[3,4,6]#sorted(list(map(int,input("Enter array:").split(" "))))
d=1#int(input("Enter Different:"))
s1=(sum(arr)+d)//2
l=[[-1]*(s1+1) for i in range(n+1)]
ans=CountingSubsetWithGivenSum(arr,n,s1)
print(ans)