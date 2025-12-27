def two_sum(nums, target):
    seen = {}
    for i,x in enumerate(nums):
        if target - x in seen:
            return [seen[target-x],i]
        seen[x] = i
    return []

result = two_sum([2,7,11,15],9)
print(result)