
n = int(input())

tab = [[0 for i in range(n)]]


def score(seq, currentScore):
  maxScore = currentScore
  print(seq)
  if not seq:
    return maxScore
  if len(seq) == 1:
    maxScore += seq[0]
    return maxScore 
  seq_set = set(seq)
  maxScorelist = []
  for i in seq_set:
    if i not in seq:
      continue
    sub_list = [j for j in seq if ((j != (i-1)) and (j != (i+1)))]
    sub_list.pop(sub_list.index(i))
    maxScore += i + score(sub_list, currentScore)
    maxScorelist.append(maxScore)
  return max(maxScorelist)

