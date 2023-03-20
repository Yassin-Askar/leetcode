class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionaryset = set(dictionary)
        l = 0
        for word in sentence.split(" "):
            r = 0
            while r < len(word)-1:
                if r == 1:
                    print(1)
                    print(word[:r])
                if word[:r] in dictionaryset:
                    sentence = sentence.replace(word, word[:r])
                    break
                r += 1
        return sentence


dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(Solution(). replaceWords(dictionary=dictionary, sentence=sentence, ))
