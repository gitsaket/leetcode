def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    stack = {}
    l_c, max_l = 0, 0
    for r_c, c in enumerate(s):
        if c in stack and stack[c] >= l_c:
            l_c = stack[c] + 1
        max_l = max(max_l, r_c - l_c + 1)
        stack[c] = r_c

    return max_l


# Example usage:
if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(None, s))  # Output: 3
    s = "bbbbb"
    print(lengthOfLongestSubstring(None, s))  # Output: 1
    s = "pwwkew"
    print(lengthOfLongestSubstring(None, s))  # Output: 3
