def front3(str):
  length = len(str)
  limit = 3
  if length < limit:
    limit = length
  front = str[:limit]
  return front + front + front