n = int(input())
ns = list(sorted((map(int, input().split()))))
m = int(input())
ms = list(sorted((map(int, input().split()))))
clip = lambda x, l, u: max(l, min(u, x))
boys = [0]*102
girls = [0]*102
matrix = [boys,girls]
for i in ns:
  matrix[0][i] += 1

for i in ms:
  matrix[1][i] += 1

pairs = 0
i = j = 0
i_clip = ns[-1] + 1
j_clip = ms[-1] + 1
matrix[0] = matrix[0][:max(i_clip, j_clip)+1]
matrix[1] = matrix[1][:max(i_clip,j_clip)+1]
# print(matrix)
while True:
  # print(i,j, pairs)
  if i <i_clip or j < j_clip:
    if matrix[0][i] == 0 and i != i_clip:
      i+= 1
      #print("eenie")
      continue
    try:
      if matrix[1][j] == 0 and j != j_clip:
        j+=1
        #print("meenie")
        continue
      if matrix[0][j-1] == 0 and \
    matrix[0][j] == 0 and \
    matrix[0][j+1] == 0:
          #print("mynie")
          j += 1
          continue
      if matrix[1][i-1] == 0 and \
    matrix[1][i] == 0 and \
    matrix[1][i+1] == 0:
          #print("mooh")
          i += 1
          continue
    except:
      break
  else:
    break
    
  if matrix[0][i] > matrix[1][j]:
    matrix[0][i] -= matrix[1][j]
    pairs += matrix[1][j]
    matrix[1][j] = 0
    j +=1

  if matrix[0][i] <= matrix[1][j]:
    matrix[1][j] -= matrix[0][i]
    pairs += matrix[0][i]
    matrix[0][i] = 0
    i +=1
  
print(pairs)