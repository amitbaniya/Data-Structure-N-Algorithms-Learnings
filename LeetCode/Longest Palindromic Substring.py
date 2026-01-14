def lengthOfLongestPalindromeSubstring(s):

    words = []
    reverse_words = []
    max_len_word = ""

    for i in range(len(s)):
        word = s[0:i+1]
        reverse_word = word[::-1]
        words.append(word)
        reverse_words.append(reverse_word)

    word_len = len(words)
    i = 0
    j = 0
    while j < word_len:
        i = 0
        print(j)
        while i < len(words):
            print(words, reverse_words)
            if words[i] == reverse_words[i]:
                if len(max_len_word) < len(words[i]):
                    max_len_word = words[i]
                words.pop(i)
                reverse_words.pop(i)
            else:
                words[i] = words[i][1:]
                reverse_words[i] = reverse_words[i][:-1]
                i += 1
        j += 1

    return max_len_word







if __name__ == '__main__':
    print(lengthOfLongestPalindromeSubstring("zttzasdasdsknksasdasd"))
