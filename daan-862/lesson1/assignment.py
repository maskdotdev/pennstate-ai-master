# Question 1
# Please use the following codes to create a list L1:

from collections import Counter
import numpy as np


def q1():
    L1 = []

    np.random.seed(56)

    for i in np.random.randint(0, 100, 10):
        L1.extend([i] * np.random.randint(0, 100, 1)[0])

    np.random.shuffle(L1)

    # Please use Python to answer the following questions:
    # What are the unique values? (5 points)
    unique_values = np.unique(L1)
    print("the unique values are: ", unique_values)

    # How many unique values? (5 points)
    print(f"there are {len(unique_values)} unique values")

    # Create a dictionary with the unique items in L1 as dictionary keys and their count as the dictionary values. (20 points)
    count_dict = dict(Counter(L1))
    print("count_dict: ", count_dict)

    # Which value appears most frequently? The manual comparison is not acceptable. (10 points)
    max_value = max(count_dict, key=count_dict.get)
    print(f"the value that appears most frequently is: {max_value}")

    # it would be much nicer doing something like:
    key, count = Counter(L1).most_common(1)[0]
    print(f"the value that appears most frequently is: {key} with a count of {count}")


# Write a function to calculate the mean of a list. Use this function to calculate the mean of L2 (10 points)
def manual_mean(L2: list[int]) -> float:
    """takes an arary and divides the sum of the array by the total number of elements in the array"""
    element_count: int = 0
    element_total_sum: int = 0
    for i in L2:
        element_count += 1
        element_total_sum += i
    return element_total_sum / element_count


# Question 2
def q2():
    # A list:
    L2 = [
        879,
        394,
        235,
        580,
        628,
        81,
        206,
        238,
        927,
        853,
        622,
        603,
        110,
        143,
        824,
        324,
        343,
        506,
        634,
        325,
        258,
        900,
        960,
        286,
        449,
        890,
        921,
        170,
        888,
        851,
    ]

    # Please use Python to answer the following questions (Do not use built-in sum and mean functions):
    # Use a while loop to calculate the sum of the even numbers in L2. (10 points)

    ### SOLUTION ###
    sum_even = 0
    for i in L2:
        if i % 2 == 0:
            sum_even += i
    # pythonic way to do the above:
    # sum_even = sum(i for i in L2 if i % 2 == 0)
    print(f"the sum of the even numbers in L2 is: {sum_even}")
    ### END SOLUTION ###

    # Write a function to calculate the mean of a list. Use this function to calculate the mean of L2 (10 points)
    ### SOLUTION ###
    actual_mean = manual_mean(L2)
    # pythonic way to do the above:
    # actual_mean = sum(i for i in L2) / len(L2) or using the mean function from statistics module
    print(f"the actual mean of L2 is: {actual_mean}")
    ### END SOLUTION ###

    # Calculate the sum for elements in L2 which is larger than 500. (10 points)
    ### SOLUTION ###
    sum_larger_than_500 = 0
    for i in L2:
        if i > 500:
            sum_larger_than_500 += i
    # pythonic way to do the above:
    # sum_larger_than_500 = sum(i for i in L2 if i > 500)
    print(
        f"the sum of elements in L2 which is larger than 500 is: {sum_larger_than_500}"
    )
    ### END SOLUTION ###


# Question 3
# Implement the function pow(x, n), which calculates x raised to the power n (xn). Please don't use x**n. (20pts)
### SOLUTION ###
def manual_pow(base: int, exponent: int) -> int | float:
    """calculates x raised to the power n
    args:
        base: int
        exponent: int
    result: int | float = 1
    """
    result: int | float = 1
    current_exponent: int = exponent
    if exponent < 0:
        current_exponent = exponent * -1

    for _ in range(current_exponent):
        result *= base

    return 1 / result if exponent < 0 else result


def q3():
    # Calculate pow(2, 10) and pow(3, -3). (10 pts)
    print(f"pow(2, 10) is: {manual_pow(2, 10)}")
    print(f"pow(3, -3) is: {manual_pow(3, -3)}")
    print(f"pow(5, 0) is: {manual_pow(5, 0)}")
    print(f"pow(3, -2) is: {manual_pow(3, -2)}")


### END SOLUTION ###


if __name__ == "__main__":
    q1()
    q2()
    q3()
