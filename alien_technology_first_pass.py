from typing import List
# add letters to graph
# travers graph till leaves, add from end
class Graph:
    def __init__(self):
        self.letters = {}
        self.letter_list = []
        self.letter_set = set()

    def __str__(self):
        output = '['
        for letter in self.letters:
            output += letter + ' -> ' + self.letters[letter] + ', '
        output += ']'
        return output

    def add(self, letter, letter2):
        self.letters[letter] = letter2
        if letter not in self.letter_set:
            self.letter_list.append(letter)
            self.letter_set.add(letter)
        if letter2 not in self.letter_set:
            self.letter_list.append(letter2)
            self.letter_set.add(letter2)

    def findLeaves(self):
        alphabet = ''
        visited = set()
        current = self.letter_list[0]
        i = 0
        while len(visited) < len(self.letter_list) and i < len(self.letter_list):
            if current not in visited:
                # does current have a child that has not been visited?
                if current in self.letters and self.letters[current] not in visited:
                    # move to child
                    if self.letters[current] in self.letters and current == self.letters[self.letters[current]]:
                        return ''
                    current = self.letters[current]
                else:
                    # current is a leaf
                    visited.add(current)
                    alphabet = current + alphabet
            else:
                if self.letter_list[i] in visited:
                    i += 1
                    current = self.letter_list[i]
                else:
                    current = self.letter_list[i]

        return alphabet

class Solution:
    def generateGraph(self, words, graph):
        for i in range(len(words) - 1):
            # check if first letters of 2 neighboring words are the same.
            if words[i][0] == words[i + 1][0]:
                if min(len(words[i]), len(words[i + 1])) > 1:
                    digit = 1
                else:
                    graph.letter_list.append(words[i])
                    graph.letter_set.add(words[i])
                    continue
                foundLetter = False
                # go to the next letter
                while not foundLetter or digit >= min(len(words[i]), len(words[i + 1])):
                    if words[i][digit] == words[i + 1][digit]:
                        digit += 1
                        continue
                    else:
                        if words[i][digit] not in graph.letters:
                            graph.add(words[i][digit], words[i + 1][digit])
                        foundLetter = True
            else:
                # This is our condition to check if the order is invalid
                if words[i][0] in graph.letters and words[i][0] != words[i - 1][0]:
                    return ''
                elif words[i][0] in graph.letters:
                    continue
                else:
                    graph.add(words[i][0], words[i + 1][0])
    
    def alienOrder(self, words: List[str]) -> str:
        graph = Graph()
        if self.generateGraph(words, graph) == '':
            return ''
        return graph.findLeaves()

words = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]

words2 = ['z', 'x', 'z']

words3 = ['z', 'z']

words4 = ["zy","zx"]

solution = Solution()

print(solution.alienOrder(words))
print(solution.alienOrder(words2))
print(solution.alienOrder(words3))
print(solution.alienOrder(words4))