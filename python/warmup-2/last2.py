def last2(str):
  init = str[:-2]
  tail = str[-2:]
  count = 0
  for i in range(len(init)):
    if str[i:i+2] == tail:
      count += 1
  return count