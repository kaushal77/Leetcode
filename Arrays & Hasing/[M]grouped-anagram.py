#medium

#https://leetcode.com/problems/group-anagrams/
#Key idea*: Key by sorted tuple or 26-count signature
#Time/Space*: O(n*k log k) or O(n*k)/O(n*k)

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

def group_anagrams(strs):
    result = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        result[key].append(s)
    return list(result.values())

strs = ["","eat","tea","tan","ate","nat","bat"]
result = group_anagrams(strs)
print(result)