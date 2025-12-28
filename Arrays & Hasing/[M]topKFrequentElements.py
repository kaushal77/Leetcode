#https://leetcode.com/problems/top-k-frequent-elements/
# Key idea*: Counter + heap/bucket
# Time/Space*: O(n)/O(n) -->Bucket sort approach

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]
# k is ranged from 1 to the number of unique elements in the array.

from collections import Counter
def top_k_frequent(nums, k):
    cnt = Counter(nums)
    freq = [[] for _ in range(len(nums)+ 1)]

    for n, c in cnt.items():
        freq[c].append(n)
    
    result = []

    for i in range(len(freq),-1,-1):
        for n in freq[i]:
            result.append(n)
            if(len(result) == k):
                return result

nums = [1,1,1,2,2,3]
k = 2
result = top_k_frequent(nums, k)
print(result)

nums = [1]
k = 1
result = top_k_frequent(nums, k)
print(result)

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
result = top_k_frequent(nums, k)
print(result)