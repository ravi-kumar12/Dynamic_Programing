from prettytable import PrettyTable
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
    
n=int(input("Enter No of Element:"))
lst=list(map(int,input("Enter Element:").split(" ")))
s=int(input("Enter sum to get:"))
l=[[None]*(s+1) for i in range(n+1)]
ans=SubSetSum(lst,n,s)
print(ans)
x=PrettyTable()
x.field_names=[i for i in range(s+1)]
for i in range(n+1): 
    x.add_row(l[i])
print(x)

if ans:
    eleadd=[]
    i=n
    j=s
    while(s!=0):
        while l[i][j]==l[i-1][j] and (i!=1):
            i-=1
        eleadd.insert(0,lst[i-1])
        s-=lst[i-1]
        j=s
        i-=1

    for i in eleadd:
        print(i)
        
    
    
    
    
    
    
    
    
    
    
    
    