const twoSum = function(nums, target) { // O(n) Space: #O(n)
    
    //U - Understand
    //P - Plan
    //reducer method?
    //foreach method - iter thru array, target - curr elem, does result match any other num,
        //negative ints?
    //double for loop checking two indices at a time to see if they match.

    //memorization - js object
    let cache = {};
    nums.forEach((num, i) => {
        let result = target - num;
        if (result in cache) {
            return [cache[result], i]
        } else {
            cache[num] = i
        }
    });








    // let array = [];
    // nums.forEach((num, i) => {
    //     let result = target - num;
    //     //another forEach
    //     nums.forEach((num, j) => {
    //         if (i !== j) {
    //             if (result === num) {
    //                 array = [i, j];
    //                 return;
    //             }
    //         } //else
    //     });
    //     if (array.length > 0) {
    //         return;
    //     }
    // });
    // return array;
};