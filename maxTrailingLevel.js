function maxTrailing(levels) {
    // Write your code here
    //find greatest max - min
    let result = -1
    const cache = {}

    //naive
    for (let i = 0; i < levels.length; i++) {
        for (let j = i + 1; j < levels.length; j++) {
            if ([i, j] in cache) {
                continue
            }
            const difference = levels[j] - levels[i];
            if (difference < 1) {
                cache[i, j] = -1
            } else {
                if (difference > result) {
                    result = difference
                }
                cache[i, j] = difference
            }
        }
    }

    return result
}