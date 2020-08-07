
from typing import List
from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adjacency_list = defaultdict(set)
        # set containing all the letters in the words
        in_degree = Counter({char : 0 for word in words for char in word})
                
        # Step 1: We need to populate adjacency_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for letter1, letter2 in zip(first_word, second_word):
                if letter1 != letter2:
                    if letter2 not in adjacency_list[letter1]:
                        adjacency_list[letter1].add(letter2)
                        in_degree[letter2] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""
        
        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        alphabet = ''
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        while queue:
            letter = queue.popleft()
            alphabet += letter
            for char in adjacency_list[letter]:
                in_degree[char] -= 1
                if in_degree[char] == 0:
                    queue.append(char)
                    
        # If not all letters are in alphabet, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(alphabet) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return alphabet