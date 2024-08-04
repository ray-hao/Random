class Trie:

    def __init__(self):
        self.root = ([None] * 26, False)

    def insert(self, word: str) -> None:
        current = self.root
        prev = None
        for index, char in enumerate(word):
            prev = current
            charNum = ord(char) - 97
            if current[0][charNum]:
                current = current[0][charNum]
                if index == len(word) - 1:
                    prev[0][charNum] = (current[0], True)
            else:
                newArr = ([None] * 26, False)
                if index == len(word) - 1:
                    newArr = ([None] * 26, True)
                current[0][charNum] = newArr
                current = current[0][charNum]

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            charNum = ord(char) - 97
            if current[0][charNum]:
                current = current[0][charNum]
            else:
                return False
        if current[1]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            charNum = ord(char) - 97
            if current[0][charNum]:
                current = current[0][charNum]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
