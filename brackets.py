import math

counter = int(input("90909 "))


def catalan(n):
    return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))


print(catalan(counter))