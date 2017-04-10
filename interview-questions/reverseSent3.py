class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        newWords = []

        for word in words:
            newWord = []

            for char in word:
                newWord.append("-1")
                newWord[1]

            newWords.append(str(newWord))
        print(newWords)
