"""14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    c1 = strs[0]
    c2 = strs[1]
    prefix = c1[0]
    for i in strs:
        c1_len = len(c1)
        counter = 0
        while counter < c1_len:
            if (c1[counter] and c2[counter]) and (c1[counter] == c2[counter]):
                counter += 1
                prefix += c1[counter]
            else:
                break
        c1 = strs[i + 1]
        c2 = strs[c1 + 1]


print(longestCommonPrefix(["flower", "flow", "flight"]))
