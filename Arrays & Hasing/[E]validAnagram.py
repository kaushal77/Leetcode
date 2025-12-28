#easy
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

#https://leetcode.com/problems/valid-anagram/
#Time/Space*: O(n)/O(1)

from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

result1 = is_anagram("anagram", "nagaram")
print(result1)

result2 = is_anagram("rat", "car")
print(result2)