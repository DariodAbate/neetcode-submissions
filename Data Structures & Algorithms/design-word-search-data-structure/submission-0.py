class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.end = True
        
    def search(self, word: str) -> bool:

        def dfs(node, i) -> bool:
            if i == len(word):
                return node.end

            ch = word[i]
            
            if ch == ".":
                for c in node.children:
                    if dfs(node.children[c], i + 1):
                        return True
                return False
            elif ch not in node.children:
                return False
            else:
                return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)
                    

        
