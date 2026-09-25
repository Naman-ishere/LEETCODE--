def smallestIndex(nums):
    # Required variables and misc processes
    checked_cases = []
    nums = [str(x) for x in nums]
    # Finding the appropriate numbers and adding them to the solution(checked_cases) list 
    for num in nums:
        num = list(num)    # Picked up one element from the nums and then converted that single element into the list so that I can iterate through it
        num = [int(x) for x in num]     # Converted the digits into integer from string
        sum_digs = 0
        for i in num:
            sum_digs = i + sum_digs
        if sum_digs == nums.index(num):
            checked_cases.append(num)
            nums.remove(num)
        else:
            continue
    # Checking for the number with the smallest index 
    if len(checked_cases) > 0:
        smallest_num = nums[0]
        for i in checked_cases:
            if i < smallest_num:
                smallest_num = i
            else:
                continue 
        return smallest_num
    else:
        return -1

nums = [1, 2, 1]
smallestIndex(nums)