from typing import List

class Solution:
    def destroyIslands(self, grid, i, j): # recursive
        # Make sure we're in the boundries of our grid.
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return 0

        grid[i][j] = '0'

        #visit its neighbors
        self.destroyIslands(grid, i + 1, j)
        self.destroyIslands(grid, i - 1, j)
        self.destroyIslands(grid, i, j + 1)
        self.destroyIslands(grid, i, j - 1)

        # return 1 for the original island found in numIslands function
        return 1

    def numIslands(self, grid: List[List[str]]) -> int: # time: O(r*c), space: O(r*c)
        if grid is None or len(grid) == 0:
            return 0

        numOfIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    # We have an island
                    # recurse through neighbors to eliminate the rest of the island
                    # to make sure it isn't counted again.
                    numOfIslands += self.destroyIslands(grid, i, j)

        return numOfIslands