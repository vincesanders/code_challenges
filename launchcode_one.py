#
# Complete the 'containsValidBraces' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING testString as parameter.
#

def containsValidBraces(testString):
    # Write your code here

    # Space: O(n) n = length of string
    # The worst case scenario: All of the string would be brackets that are unmatched and stack would be length n.
    
    # Time: O(n) n = length of string

    # This dictionary's purpose is to make it easier to check for a matching bracket.
    bracket_dict = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    # This set is used to isolated the characters of the string we're interested in.
    # if the char isn't in this set, we don't care about it.
    possible_matches = {'[',']','(',')','{', '}'}

    # create a stack to keep track of unmatched brackets.
    stack = []

    # interate through the string character by character.
    for char in testString:

        # check if the char is a bracket.
        # If not, continue to next character.
        if char not in possible_matches:
            continue

        # If our stack is empty, we don't have anything to compare it to,
        # so we know we have to add it to the stack and no other action is necessary.
        if len(stack) is 0:
            stack.append(char)
        else:
            # compare the new bracket to bracket at top of stack
            # if the bracket at the top of the stack is an opening bracket AND
            # char is the corresponding closing bracket, pop the bracket off the stack.
            if stack[len(stack) - 1] in bracket_dict and bracket_dict[stack[len(stack) - 1]] is char:
                # if match pop bracket off stack
                stack.pop()

            # if not match, add bracket to stack
            else:
                stack.append(char)

    # if there are still brackets left in the stack that means 
    # there wasn't a matching closing bracket for each opening bracket and 
    # we should return invalid.
    # Otherwise, we return valid.
    if len(stack) > 0:
        return 'invalid'
    else:
        return 'valid'