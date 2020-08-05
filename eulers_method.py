'''
 Given the differential equation f'(x) = x^x, write a function that uses Euler's method to approximate the value of f(x1) given an initial condition (x0, f(x0)) and the value of x1.

 f'(x) = x^x
 f(x0) = x0
 f(x1) = ?
 y(n+1) = y(n) + h * f'(x)
'''

def eulers_method(init_cond, x1):
    # assuming init_cond is a tuple containing (x0, f(x0))
    x = init_cond[0] # x0
    y = init_cond[1] # y0
    # value to step by (smaller gives a more accurate approximation)
    step = 0.1

    while x < x1:
        y = y + step * pow(x, x)
        x = x + step

    print(f'The approximate value of f({x1}) is: {y}')

    return y