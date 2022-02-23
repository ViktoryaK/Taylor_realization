"""
This module returns the calculation of the function of f(x) = arcsin(x) using Taylor series
"""


def factorial(n):
    """
    Function that calculates factorial n
    >>> factorial(4)
    24
    """

    result = 1.0
    for i in range(1, n+1):
        result *= i
    return result

def taylor(x, n):
    """
    The main taylor calculating function
    >>> taylor(0.5, 8)
    0.5235986637263972
    """
    x = float(x)
    n = int(n)
    result = 0
    for numb in range(0, n):
        value = factorial(2*numb) * (x**(2*numb+1))
        value = value / (4**numb * factorial(numb)**2 * (2*numb + 1))
        result += value
    return result

if __name__ == "__main__":
    print("Please, input the value of x: ")
    x = input()
    print("Please, input the number of terms(n) of the series: ")
    n = input()
    print(taylor(x, n))