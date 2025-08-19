# Day26: Generators

# Example 1: Simple generator (Top 5 numbers)
def top_five():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

values = top_five()

print(values.__next__())
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

# Example 2: Generator for perfect squares up to 10
def per_perfect():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1

value = per_perfect()
for i in value:
    print(i)
