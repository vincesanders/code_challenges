from typing import List, Iterable
from functools import reduce

class triangleSummer():
    def _load_triangle(self, triangle_file: str) -> Iterable[List[int]]:
        with open(triangle_file, 'r') as triangle_file:
            for triangle_row in triangle_file.readlines():
                out_row = triangle_row.strip().split()
                yield out_row
    
    @staticmethod
    def _triangle_reducer(top_row: List[int], bottom_row: List[int]) -> List[int]:
        for i, element in enumerate(bottom_row):
            if i == 0:
                bottom_row[i] = top_row[i] + element
            elif i == len(bottom_row) - 1:
                bottom_row[i] = top_row[i - 1] + element
            else:
                bottom_row[i] = max(top_row[i - 1], top_row[i]) + element

    def max_sum(self, triangle_file: str) -> int:
        triangle_array = self._load_triangle(triangle_file)
        reduced_triangle = reduce(self._triangle_reducer, triangle_array)
        return max(reduced_triangle)