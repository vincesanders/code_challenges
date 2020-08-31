# Args:
#    matrix: an NxN list of lists containing the matrix to check
# Returns:
#    The string "VALID" if matrix contains a valid sub-sudoku solution, and
#    "INVALID" otherwise
def isRowsValid(matrix, numSet): #O(n^2)
  for i in range(len(matrix)):
    # cast each row to a set and see if it matches 
    # the numSet created in check_sub_sudoku
    if set(matrix[i]) != numSet:
      return False
    return True

def isColumnsValid(matrix, numSet): #O(n^2)
  for i in range(len(matrix)):
    # cast each column to a set and see if it matches 
    # the numSet created in check_sub_sudoku
    if {s[i] for s in matrix} != numSet:
      return False
  return True

def check_sub_sudoku(mat): # Overall: runtime - O(n^2), space: O(n)
  # Your code here.
  # Create a set of numbers that sould be in each row and column
  numSet = {s for s in range(1, len(mat) + 1)} #O(n)

  if isRowsValid(mat, numSet) and isColumnsValid(mat, numSet):
    return "VALID"
  return "INVALID"