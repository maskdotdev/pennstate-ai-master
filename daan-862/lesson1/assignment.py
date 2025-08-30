# Question 1
# Please use the following codes to create a list L1:

import numpy as np

L1 = []

np.random.seed(56)

for i in np.random.randint(0, 100, 10):
    L1.extend([i] * np.random.randint(0, 100, 1)[0])

np.random.shuffle(L1)

# Please use Python to answer the following questions:
# What are the unique values? (5 points)
unique_values = np.unique()
# How many unique values? (5 points)
# Create a dictionary with the unique items in L1 as dictionary keys and their count as the dictionary values. (20 points)
# Which value appears most frequently? The manual comparison is not acceptable. (10 points)

# Question 2
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
# Write a function to calculate the mean of a list. Use this function to calculate the mean of L2 (10 points)
# Calculate the sum for elements in L2 which is larger than 500. (10 points)
