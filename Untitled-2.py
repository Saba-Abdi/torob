t = int(input())
for _ in range(t):
    n = int(input())
    matrix1 = [input() for _ in range(n)]
    matrix2 = [input() for _ in range(n)]
    a=0
    for i in matrix1:
        if i[::-1] in matrix2:
            a+=1
        else:
            a=a
    if a==len(matrix1):
        print("YES")
    else:
        print("NO")

