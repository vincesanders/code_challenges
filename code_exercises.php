<?php

/**
 * This is open book --- Hooray!
 * No, really - let's not think of this as a test, but just an assessment 
 * and ability for us to gauge some of your thought process, and approach to coding.
 *
 * Use whatever resources you'd like, and limit your time. This shouldn't be something
 * you spend all afternoon on, but maybe 10-15 minutes per exercise.
 *
 * hint: It may make sense to create a class of helpers to organize this
 */

/**************
 * EXERCISE 1 *
 **************/

/**
 * Write a method or function which returns
 * the sum of two integers, with the caveat that if
 * the two integers are identical, the function
 * returns the integer's square.
 *
 * Input vals:
 * 1,2; 2,9; 4,4; 0,-5
 */

function addOrSquare($int1, $int2) {
    if ($int1 === $int2) {
        return $int1 * $int2; //square
    } else {
        return $int1 + $int2;
    }
}

/**************
 * EXERCISE 2 *
 **************/

/**
 * Write a method or function which takes a string and an integer
 * as arguments, and removes the character in the string whose place 
 * equals the integer.
 *
 * Bonus: Add the ability to remove a range of characters, given a 
 * second integer.
 *
 * Input values:
 * "ColoradoPublicRadio", 2; "ColoradoPublicRadio", 18; "ColoradoPublicRadio", 1 
 */

function removeChar($str, $int) {
    return substr($str, 0, $int).substr($str, $int + 1);
}


/**************
 * EXERCISE 3 *
 **************/

/**
 * Write a method or function which returns the Fibonacci sequence to 'n' places, 
 * where 'n' is an integer passed into the function as an integer.
 * This one's just in here for nostalgia, since there was a time when you couldn't avoid
 * this as an interveiw question. Have some fun with it, and if it's too easy, feel free to 
 * show off and add start/end ranges, or feel free to make both an "elegant" and an "expensive" solution.
 */
//Simple O(n)
function fibonacci($n) {
    if ($n <= 1) {
        return $n;
    }
    $n1 = 0;
    $n2 = 1;
    for ($i = 2; $i <= $n; $i++) {
        $temp = $n2;
        $n2 = $n1 + $n2;
        $n1 = $temp;
    }
    return $n2;
}

//More interesting algorithm utilizing memorization and recursion.
$cache = array();
function fib($n, $cache) {
    if ($n <= 1) {
        return $n;
    }
    if (array_key_exists($n, $cache)) {
        return $cache[n];
    }
    $cache[$n] = fib($n - 1, $cache) + fib($n - 2, $cache);
    return $cache[$n];
}
?>
