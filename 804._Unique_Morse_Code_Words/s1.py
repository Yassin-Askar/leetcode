

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        MORSE = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
            'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
            'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
            'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
            'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--..",
        }

        transformations = []
        count = 0

        for word in words:

            w = ""

            for c in word:
                w += MORSE[c]

            if w not in transformations:
                transformations.append(w)
                count += 1

        return count


words = ["gin", "zen", "gig", "msg"]
print(Solution(). uniqueMorseRepresentations(words=words, ))
