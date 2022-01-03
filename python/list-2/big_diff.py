def big_diff(nums):
  min_ = nums[0]
  max_ = nums[0]
  for num in nums:
    if num < min_:
      min_ = num
    if num > max_:
      max_ = num
      
  return max_ - min_
