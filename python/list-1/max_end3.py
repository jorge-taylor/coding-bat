def max_end3(nums):
  if nums[0] > nums[-1]:
    largest = nums[0]
  else:
    largest = nums[-1]
    
  return [largest, largest, largest]
