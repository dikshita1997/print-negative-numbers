#l=[12,10,-1,90,-7,-9]
n=int(input("Enter the number of elements"))
lst=[]
for j in range(0, n):
    num=int(input())
    lst.append(num)
print(lst)
for i in lst:
    if i<0:
        print(i)
