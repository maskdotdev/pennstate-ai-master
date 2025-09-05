import numpy as np

# arange creates an array from 0 - 5 (6 elements)
# the ** 2 means to raise each element to the power of 2
# so this should be an array of [0, 1, 4, 9, 16, 25]
a = np.arange(6) ** 2
print("a", a)


# creating an array from a function


def f(x: int, y: int):
    return x + y


# f is the function, (3, 3) is the shape of the array,
# 3 rows and 3 columns, and dtype is int
# the way this works is that the function is called
# for each element in the array, and the return value
# is the value of the array, so the first row should b
# [0, 1, 2]
# [1, 2, 3]
# [2, 3, 4]
# the funcitonality is simple:
# we can think of it as a matrix of size 3x3 where each
# element is the sum of the row and column
b = np.fromfunction(f, (3, 3), dtype=int)

print("b", b)


# boolean indexing
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])

# whats happening here is that when using boolean indexing
# we are selecting the rows where the names are "Bob"
# so if bob appears at index 0 and 1, then the boolean
# indexing will select the rows 0 and 1 from that array
data = np.random.randn(7, 4)

print("raw data", data)
print("data with bobs", data[names == "Bob"])
print("data with joes", data[names == "Joe"])
print("data with wills", data[names == "Will"])
