# Day25: Iterators

# Iterator is an object that allows the programmer to traverse through the
# sequence of data without having to store the entire data in memory.

num = [1, 2, 3]

# Using an iterator explicitly
iterator = iter(num)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# Making own for loop
def own_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

# Creating my own range
class own_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return own_range_iterator(self)


class own_range_iterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current = self.iterable.start
        self.iterable.start += 1
        return current


# Testing custom range
for i in own_range(1, 11):
    print(i)
