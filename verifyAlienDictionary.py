from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # make an alphabet dictionary, key: letter, value: index
        dictionary = {}
        for i in range(len(order)):
            dictionary[order[i]] = i

        # iterate through words and check their order.
        for i in range(len(words) - 1):
            j = 0
            curWord = words[i]
            nextWord = words[i + 1]

            if dictionary[curWord[j]] < dictionary[nextWord[j]]:
                # confirmed in order
                continue
            elif dictionary[curWord[j]] > dictionary[nextWord[j]]:
                return False
            else:
                # same letter
                j += 1

                # Move through letters of two words to ensure they are in right order.
                while j < len(curWord) and j < len(nextWord):
                    if dictionary[curWord[j]] < dictionary[nextWord[j]]:
                        # confirmed in order
                        break
                    elif dictionary[curWord[j]] > dictionary[nextWord[j]]:
                        return False
                    j += 1
                
                if j > len(curWord) - 1 or j > len(nextWord) - 1:
                    # We got to the end of one word.
                    # longest word should be last
                    if len(curWord) > len(nextWord):
                        return False

        return True
