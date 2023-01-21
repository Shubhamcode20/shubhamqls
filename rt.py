def find_max(arr):
    res = arr[0]
    for i in arr:
        if res<i:
            res=i
    return res

n=int(input())
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
print(find_max(arr))