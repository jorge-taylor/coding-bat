def centered_average(nums):
  total = 0
  min_ = nums[0]
  max_ = nums[0]
  
  for num in nums:
    total += num
    
    if num < min_:
      min_ = num
    if num > max_:
      max_ = num
      
  return int((total - max_ - min_) / (len(nums) - 2))
    
