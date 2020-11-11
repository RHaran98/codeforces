n,a,b,c = list(map(int,input().split()))
l = max(n,a,b,c) 
tabs = [0 for i in range(l+1)]


a,b,c = sorted([a,b,c])


# for i in range(c):
#   tabs[i] = -1

tabs[a] = tabs[b] = tabs[c] = 1


for i in range(n+1):
  if (i <= a):
    continue
  max_value = max(tabs[max(i-a,0)],tabs[max(i-b,0)],tabs[max(i-c,0)])
  if max_value == 0:
    continue
  tabs[i] = 1 + max_value
  # print(tabs)
print(tabs[n])

