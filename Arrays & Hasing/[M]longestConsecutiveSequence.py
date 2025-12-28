#https://leetcode.com/problems/longest-consecutive-sequence/
# Key idea*: HashSet to store nums, then expand from each num to find the longest sequence
# Time/Space*: O(n)/O(n)

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

def longest_consecutive(nums):
    num_set = set(nums)
    length = 0
    for n in num_set:
        if n-1 not in num_set:
            current_num = n
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            length = max(length, current_length)
    return length

nums = [100,4,200,1,3,2]
result = longest_consecutive(nums)
print(result)  # Output: 4