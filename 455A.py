def test():
  n = int(input())
  seq = list(map(int, input().split()))

  counts = {}
  for i in seq:
    counts[i] = counts.get(i,0) + 1
  keys = sorted(list(counts.keys()))
  # if len(keys) == 1:
  #   print(keys[0]*counts[keys[0]])
  #   return
  tab = [0 for i in range(max(keys)+1)]
  # tab[0] = counts.get(0,0)*0
  # tab[1] = counts.get(1,0)*1
  # tab[1] += tab[0] if abs(keys[0] - keys[1]) != 1 else 0
  # if len(keys) == 2:
  #   print(max(*tab))
  #   return
  # for i in range(2,len(tab)):
  #   print(i,keys[i])
  for i in range(1,len(tab)):
    # if abs(keys[i] - keys[i-1]) != 1:
    #   tab[i] = counts[keys[i]] * keys[i] + tab[i-1]
    # else:
    tab[i] = max(counts.get(i,0)*(i) + tab[i-2], tab[i-1])

  print(tab[-1])

test()