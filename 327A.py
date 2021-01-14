n = int(input())
a = list(map(int,input().split()))

s_ind = e_ind = 0
best_gain = 0
best_s, best_e = -1,-1
current_gain = 0
for i in range(n):
  if current_gain < 0:
    s_ind = i
    end_ind = i
    current_gain = 0

  if a[i] == 0:
    e_ind = i
    current_gain += 1
  else:
    e_ind = i
    current_gain -= 1
  # print(current_gain, s_ind, e_ind)

  if current_gain > best_gain:
    best_gain = current_gain
    best_s = s_ind
    best_e = e_ind

i = best_s
while i <= best_e:
  a[i] = 1 - a[i]
  i += 1
# print(best_s,best_e,best_gain)
# print(a[:best_s],a[best_e+1:])
print(sum(a))
