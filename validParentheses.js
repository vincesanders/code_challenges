/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function(s) {
    const parensDict = {'(': ')', '{': '}', '[': ']'};
    const stack = [];

    for (let i = 0; i < s.length; i++) {
        const char = s.charAt(i);
        if (stack.length === 0) {
            stack.push(char);
            continue;
        } else if (char in parensDict) {
            //This is a opening paren
            stack.push(char)
        } else {
            //closing paren
            const topOfStack = stack[stack.length - 1]

            if (char === parensDict[topOfStack]) {
                //char matches the closing paren needed to close the current paren at top of stack.
                stack.pop();
            } else {
                stack.push(char);
            }
        }
    }

    if (stack.length > 0) {
        return false;
    }
    return true;
};