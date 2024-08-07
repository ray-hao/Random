#
# every group of 3 we just say the hundreds, tens, ones value and add the 
# suffix at the end. 
# 
# can we just solve the problem for 3 digit numbers?
#

d = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1000: "Thousand",
    1000000: "Million",
    1000000000: "Billion"
}

thousandsGroup = {
    0: "",
    1: " Thousand",
    2: " Million",
    3: " Billion"
}

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        group = 0
        retval = ""
        while num > 0:
            if num - math.floor(num / 1000) * 1000 != 0:
                retval = self.numberToWordsHelper(num - math.floor(num / 1000) * 1000) + thousandsGroup[group] + retval
            num = math.floor(num / 1000)
            group += 1
        
        if retval[0] == " ":
            retval = retval[1:]
        if retval[-1] == " ":
            retval = retval[:len(retval) - 1]
        return retval

    def numberToWordsHelper(self, num) -> str:
        if num == 0:
            return ""
        if num <= 20:
            return " " + d[num]
        elif num <= 99:
            return " " + d[math.floor(num / 10) * 10] + self.numberToWordsHelper(num - math.floor(num / 10) * 10)
        else:
            return " " + d[math.floor(num / 100)] + " Hundred" + self.numberToWordsHelper(num - math.floor(num / 100) * 100) 
