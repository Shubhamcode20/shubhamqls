n=int(input())
for i in range(0,n):
    k=input()
    count1=0
    count2=0
    l =[int(x) for x in str(k)]
    for j in range(0,len(l)-1):
        if l[j]<l[j+1]:
            count1+=1
            continue
        elif l[j]>l[j+1]:
            count2+=1
            continue

    if count1==len(l)-1 or count2==len(l)-1:
        print("Not a Special Chemical")
    else:
        print("Special Chemical")