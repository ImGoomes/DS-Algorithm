def highestNumber(list):
  if(len(list) == 1):
    return list[0]
  elif (list[0] > list[1]):
    list.pop(1)
    return highestNumber(list)
  else:
    list.pop(0)
    return highestNumber(list)

print(highestNumber([4,1,9,7,14,2]))
