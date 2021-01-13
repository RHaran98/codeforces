n = int(input())

arr = list(map(int, input().split()))
max_val = max(arr)

cache = [0]*(max_val+1)
for i in arr:
  cache[i] += 1

ans = 0
for i in range(len(cache)):
  if cache[i]:
    ans+=cache[i]
  cache[i] = ans

q = int(input())
for i in range(q):
  m = min(int(input()),max_val)
  # print(cache)
  print(cache[m])
