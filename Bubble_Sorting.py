# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
#
#
# if __name__ == "__main__":
#     num = int(input("Enter a non-negative integer: "))
#     res = factorial(num)
#     print(res)

# using recursion
def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


if __name__ == "__main__":
    fact_input = int(input("Enter a number: "))
    result = fact(fact_input)
    print(result)
