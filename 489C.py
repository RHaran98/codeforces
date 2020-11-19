def test():
  m,s = map(int,input().split())
  if s > 9*m:
    print("-1 -1")
    return

  elif s == 0:
    print("-1 -1")
    return
  if s <= m:
    min_num = "1" + ("0"*(m - s)) + "1"*(s-1)
    max_num = "9"*(s//9) + str(s%9)*(s%9!=0)
    max_num = max_num.ljust(m,"0")
  else:
    max_num = "9"*(s//9) + str(s%9)*(s%9!=0)
    max_num = max_num.ljust(m,"0")
    if max_num[-1] == "0":
      max_num_sub = "9"*((s-1)//9) + str((s-1)%9)*((s-1)%9!=0)
      max_num_sub = max_num_sub.ljust(m-1,"0")
      min_num = "1" + max_num_sub[::-1]
    else:
      min_num = max_num[::-1]
    # nzero = m-(s//9 + (s%9!=0))
    # min_num = max_num[::-1]
    # if max_num[-1] == "0":
      # # min_num = min_num[:nzero] + str(int(min_num[nzero]) - 1) + min_num[nzero+1:]
      # min_num = "1" + min_num[1:] 
  print(min_num,max_num)


test()

# for m in range(1):
# m = 1
# for s in range(20):
#   print ("->",s,s+1)
#   test(s,s+1)