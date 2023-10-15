n = int(input())
lst=[]
nokhod=1
for i in range(n):
  a = input().split()
  lst.append(a)
for i in lst:
  if int(i[0])==nokhod:
    nokhod=int(i[1])
  elif int(i[1])==nokhod:
    nokhod=int(i[0])
  else:
    nokhod = nokhod

print(nokhod)
