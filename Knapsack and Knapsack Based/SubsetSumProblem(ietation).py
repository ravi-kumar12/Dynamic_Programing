from prettytable import PrettyTable
x=PrettyTable()
n=int(input("Enter No of Element:"))
lst=list(map(int,input("Enter Element:").split(" ")))
s=int(input("Enter sum to get:"))
x.field_names=[i for i in range(s+1)]
table=[[None]*(s+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(s+1):
        if i!=0 and j==0:
            table[i][j]=True
        elif i==0 and j!=0:
            table[i][j]=False
        elif i==0 and j==0:
            table[i][j]=True
        elif lst[i-1]<=j:
            table[i][j]=table[i-1][j-lst[i-1]] or table[i-1][j]
        else:
            table[i][j]=table[i-1][j]
for i in range(n+1):
    x.add_row(table[i])
print(x)    
ans=table[n][s]
print(ans)

if ans:
    l=[]
    i=n
    j=s
    while(s!=0):
        while table[i][j]==table[i-1][j] and (i!=1):
            i-=1
        l.insert(0,lst[i-1])
        s-=lst[i-1]
        j=s

for i in l:
    print(i)