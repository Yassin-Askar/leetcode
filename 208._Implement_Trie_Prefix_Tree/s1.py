class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False



class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node= node.children.get(c)
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node= node.children.get(c)
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


print(Solution(). __init__())