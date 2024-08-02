class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        return self.bt(0, books, shelfWidth, shelfWidth, 0, 0)

    def bt(self, bookIndex, books, remainingWidth, totalWidth, currentHeight, totalHeight):
        if remainingWidth < 0:
            return float('inf')

        if bookIndex == len(books):
            return totalHeight + currentHeight
        
        sameLevel = 0
        nextLevel = 0

        sameLevel = self.bt(bookIndex + 1, books, remainingWidth - books[bookIndex][0], totalWidth, max(currentHeight, books[bookIndex][1]), totalHeight)
        nextLevel = self.bt(bookIndex + 1, books, totalWidth - books[bookIndex][0], totalWidth, books[bookIndex][1], totalHeight + currentHeight)

        return min(sameLevel, nextLevel)

        

