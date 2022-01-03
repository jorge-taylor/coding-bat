def sum13(nums):
    total = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i+1 < len(nums):
                nums[i+1] = 0
        else:
            total += nums[i]

    return total
