# def recursiveMethod(n):
#     if n < 1:
#         print("n is less than 1")
#     else:
#         recursiveMethod(n - 1)
#         print(n)
#
#
# recursiveMethod(5)


# def powerof(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerof(n-1)
#         return power * 2
#
#
# powerof(4)


# def power_of_the_int(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i = i + 1
#         return power


# power_of_the_int(5)

# -------------------------------------------------------------------------------

# RECURSION

# RECURSIVE CASE :return n * factorial(n - 1)
# BASE CASE : if n in [0, 1]
# UNINTENTIONAL CASE - THE CONSTRAINTS : assert 0 <= n == int(n), 'The number Must be positive integer only'

# def factorial(n):
#     assert 0 <= n == int(n), 'The number Must be positive integer only'
#     if n in [0, 1]:
#         return 1
#
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(4))


# RECURSIVE CASE :return fibonacci(n - 1) + fibonacci(n - 2)
# BASE CASE : if n in [0, 1]
# UNINTENTIONAL CASE - THE CONSTRAINTS : assert 0 <= n == int(n), 'The number Must be positive integer only'


# def fibonacci(n):
#     assert 0 <= n == int(n), 'The number Must be positive integer only'
#     if n in [0, 1]:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# a = int(input("Enter a number to get it's fibonacci value : "))
#
# print(fibonacci(a))

# taking input number and adding the sum of digits

# method 1

# def digiSum(n):
#     assert 0 <= n == int(n), 'Please enter a positive integer'
#     str_list_n = list(str(n))
#     int_a = ([int(x) for x in str_list_n])
#     return sum(int_a)
#
#
# print(digiSum(123))


# method2

# def digitSum(n):
#     assert 0 <= n == int(n), "Please enter positive integer"
#
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + digitSum(int(n / 10))
#
#
# user_input = input("Enter a positive integer :")
# print(digitSum(user_input))

# CALCULATING THE POWER OF A NUMBER

# def power(base, exp):
#     assert 0 <= exp == int(exp), "exponent should be a positive integer"
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return base
#     return base * power(base, exp - 1)
#
#
# print(power(10,50))

# GREATEST COMMON DIVISOR => GCD

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The number must be integer'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 28))
