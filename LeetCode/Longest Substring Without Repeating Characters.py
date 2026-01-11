def lengthOfLongestSubstring(self, s):
    viewed = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        print(s[left], s[right])
        while s[right] in viewed:
            del viewed[s[left]]
            left += 1

        viewed[s[right]] = right
        print(right-left +1)
        max_len = max(max_len, right - left + 1)
    return max_len



if __name__ == '__main__':
    print(lengthOfLongestSubstring("Hello", "pwwkew "))
