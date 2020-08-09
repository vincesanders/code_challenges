// Complete the braces function below.
function braces(values) {

    const braces = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    return values.map(string => {
        const stack = []
        const s = string.split('')
        s.forEach(char => {
            if (char in braces) {
                // opening bracket
                stack.push(char)
            } else {
                // closing bracket
                if (char == braces[stack[stack.length - 1]]) {
                    stack.pop()
                } else {
                    stack.push(char)
                }
            }
        })
        if (stack.length > 0) {
            return 'NO'
        } else {
            return 'YES'
        }
    })
}