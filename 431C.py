from functools import lru_cache

@lru_cache(200)
def fsum(n,k):
  if k > n:
    k = n
  if n == 0:
    return 0
  paths = k
  for i in range(1,k+1):
    paths += fsum(n-i,k)
  return paths

  
# for n in range(1,4):
#   for k in range(1,4):
#     for d in range(1,k+1):
#       a = fsum(n,k)
#       b = fsum (n,d-1)
#       print(n,k,d ,f"{a}-{b}={a-b}")

fsum(3,3)