from prettytable import PrettyTable
def SubSetSum(arr,n,s):
    for i in range(n+1):
        for j in range(s+1):
            if i==0 and j==0:
                l[i][j]=True
            elif i!=0 and j==0:
                l[i][j]=True
            elif i==0 and j!=0:
                l[i][j]=False
            elif arr[i-1]<=j:
                l[i][j]=l[i-1][j-arr[i-1]] or l[i-1][j]
            else:
                l[i][j]=l[i-1][j]
                
def PrintEle(s1):
    ans1=[]
    i=n
    while s1!=0:
        j=s1
        while l[i][j]==l[i-1][j] and i!=0:
            i-=1
        ans1.append(arr[i-1])
        s1-=arr[i-1]
        i-=1
        
    for i in ans1:
        arr.remove(i)
        
    print(ans1,arr)      
    
    
n=int(input("Enter No Of Number in array:"))
arr=sorted(list(map(int,input("Enter Array Of Element:").split(" "))))
arr_range=sum(arr)//2
l=[[None]*(arr_range+1) for i in range(n+1)]
SubSetSum(arr,n,arr_range)

x=PrettyTable()
x.field_names=[i for i in range(arr_range+1)]
for i in l:
    x.add_row(i)
print(x)

for i in l[n][::-1]:
    if i==True:
        s1=len(l[n])-l[n].index(i)-1
        break
#s2=sum(arr)-s1
print("Min Difference B/t Subset:{}".format(sum(arr)-2*s1))    #s2-s1=sum(arr)-s1-s1=sum(arr)-2s1
print("SubArrays are:")     
PrintEle(s1)