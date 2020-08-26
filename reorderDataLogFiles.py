from operator import itemgetter
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for i in range(len(logs)):
            # remove identifier
            log = self.removeIdentifier(logs[i])

            #check if digits or alpha
            if self.isDigitalLog(log):
                digits.append(logs[i])
            else:
                #create a tuple with the first item being the log without the identifier
                letters.append((log, logs[i]))

        letters.sort()
        for i in range(len(letters)):
            letters[i] = letters[i][1]
                
        return letters + digits
    
    def removeIdentifier(self, letter: str) -> str:
        # remove identifier, find the first space
        i = 0
        while i < len(letter):
            if letter[i] != ' ':
                i += 1
            else:
                # we found a space
                i += 1
                break
                
        return letter[i:]

    def isDigitalLog(self, log: str) -> bool:
        for i in range(len(log)):
            if not log[i].isdigit() and log[i] != ' ':
                return False

        return True

solution = Solution()

log1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
log2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

print(solution.reorderLogFiles(log2))