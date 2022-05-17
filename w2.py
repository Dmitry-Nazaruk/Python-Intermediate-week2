class ReverseIter:
    def __init__(self, lst:list):
        self.lst = lst

    def __iter__(self):
        self.c = 0
        return self

    def __next__(self):
        if abs(self.c) < len(self.lst):
            self.c -= 1
            return self.lst[self.c]
        else:
            raise StopIteration

a = ReverseIter(["a","b","c"])
for i in a:
    print(i)