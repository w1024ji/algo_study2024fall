def binsearch(lst, searchNum, left, right):
  while(left <= right):
      middle = (left + right) // 2
      if (lst[middle] < searchNum):
          left = middle + 1
      elif (lst[middle] > searchNum):
          right = middle - 1
      elif (lst[middle] == searchNum):
          return 1
  return 0 # 찾는 수가 없다면

# main
n = int(input())
numbersN = list(map(int, input().split()))
numbersN.sort()

m = int(input())
numbersM = list(map(int, input().split()))

for i in range(m):
  result = binsearch(numbersN, numbersM[i], 0, n-1)
  print(result)
    