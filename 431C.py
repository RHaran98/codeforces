from functools import lru_cache

# arr = [1 for i in range(10)]
def fsum(n,k):
  if k > n:
    k = n
  if n == 0:
    return 1
  # paths = 1
  paths = 0
  # print(n,k, paths)
  for i in range(1,k+1):
    paths += (fsum(n-i,k))
  return paths

# print(fsum(3,3))
# print(fsum(3,0))
n,k,d = map(int,input().split(" "))
# a = fsum(n,k)
# b = fsum (n,d-1)
# print(n,k,d ,f"{a}-{b}={a-b}")
# print((fsum(n,k) - fsum(n,d-1))% 1000000007)
