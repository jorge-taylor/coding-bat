def array_front9(nums):
    first4 = nums[:4]
    for num in first4:
        if num == 9:
            return True
    return False
