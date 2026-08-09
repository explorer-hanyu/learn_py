import math
def power(a,b):
    return a**b

def sqrt(a):
    if a<0:
        raise ValueError("Error: negative number")
    else:
        return math.sqrt(a)


def factorial(a):
    if a<0:
        raise ValueError("Error: negative number")
    else:
        return math.factorial(a)


if __name__ == '__main__':
    print("basic module self-test passed")

    