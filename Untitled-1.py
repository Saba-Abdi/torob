t = int(input())
lst=[]
for i in range(t):
    a=input().split()
    lst.append(a)
for i in lst:
    if len(i[0]) != len(i[1]):
        print("NO")
    else:
        if i[0][::-1] == i[1]:
            print("YES")
        elif i[1] in i[0]+i[0]:
            print("YES")
        elif i[1] in i[0][::-1]+i[0][::-1]:
            print("YES")
        else:
            print("NO")
            