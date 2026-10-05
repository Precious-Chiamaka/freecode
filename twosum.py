def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return None

print(two_sum([2, 7, 11, 15], 9))
