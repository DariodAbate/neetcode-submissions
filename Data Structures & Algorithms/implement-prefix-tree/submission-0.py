class TrieNode:
    def __init__(self, end=True):
        self.children = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.children:
                curr.children[ch] = TrieNode(False)
            curr = curr.children[ch]
            if i == len(word) - 1:
                curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, ch in enumerate(prefix):
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        