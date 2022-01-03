def sum67(nums):
  total = 0
  ignoring = False
  
  for i in range(len(nums)):
    if nums[i] == 6:
      ignoring = True
      
    if not ignoring:
      total += nums[i]
  
    if nums[i] == 7:
      ignoring = False
      
  return total
