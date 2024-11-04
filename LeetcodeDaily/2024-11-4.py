class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        ptr = 0
        while ptr < len(word):
            counter = 0
            char = word[ptr]
            while ptr < len(word) and (word[ptr] == char) and counter < 9:
                counter += 1
                ptr += 1
            
            comp += str(counter) + str(char)

        return comp
        
