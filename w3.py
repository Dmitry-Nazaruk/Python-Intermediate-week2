def fib_generator(n:int):
    lst = [0,1]
    while len(lst) <= n:
        lst.append(lst[-1] + lst[-2])
    yield lst[:n]

for i in fib_generator(10):
    print(i)
