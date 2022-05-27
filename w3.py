def fib_generator(n: list):
    for i in n:
        yield i


def fib_list(n: int) -> list:
    lst = [0, 1]
    while len(lst) <= n:
        lst.append(lst[-1] + lst[-2])
    return lst[:n]

for i in fib_generator(fib_list(3)):
    print(i)