n = int(input())
ns = list(sorted((map(int, input().split()))))
m = int(input())
ms = list(sorted((map(int, input().split()))))
i = j = 0
pairs = 0
while True:
  if i >= n or j >= m:
    break
  if abs(ns[i]-ms[j]) > 1:
    if ns[i] > ms[j]:
      j+=1
    else:
      i+=1
  else:
    pairs +=1
    i+=1
    j+=1
print(pairs)