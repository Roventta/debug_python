def fib(n):
    if n <= 1:
        return n

    a = fib(n - 1)
    b = fib(n - 2)

    return a + b



# codes start to run from here

# some meaningless line below for testings
one = 1
two = 2
three = one + two

i = 3
print("calculating fib", i, ": ")
result = fib(i)
print(result)