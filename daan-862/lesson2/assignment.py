import numpy as np

# Question 1
# Perform the following actions:
#
# Use the randn function to create an array with a dimension of 5X5 and use a for loop to calculate the sum of all elements in the diagonal of the array. (25 points)

# using seed to get consistent results, and validate the results
np.random.seed(123)
arr = np.random.randn(5, 5)


def print_spacer(name: str = ""):
    print(f"\n================={name}=======================\n")


def print_initial_data(arr: np.ndarray):
    for index, row in enumerate(arr):
        print(f"row {index} is {row}")


print_spacer("INITIAL DATA")
print_initial_data(arr)
print_spacer()


def calculate_diagonal(arr: np.ndarray):
    """calculate primary and secondary diagonal sums

    Args:
        arr (np.ndarray): 2D array

    Returns:
        float: primary diagonal sum
        float: secondary diagonal sum
        float: sum of primary and secondary diagonals
    """
    # these are the lists that will hold the values of the diagonals
    # no real value, except for clarity of validation
    primary_diag = []
    secondary_diag = []

    primary_diag_sum = 0
    secondary_diag_sum = 0

    arr_len = len(arr)

    for i in range(arr_len):
        # the main diagonal is pretty simple since you just need
        # to use the same index for both the row and column
        primary_diag_sum += arr[i, i]

        # Wasnt sure if this was necessary, but I added it jus in case,
        # at first I was a bit confused, but after thinking through it
        # the simple way to solve this is to just use the same index for
        # the row and and for the column we just need the total number of
        # elements in the array, and then subtract one so we have the
        # correct index, once we have the correct index we can substract the
        # index of the row, and we get the correct index for the column,
        # basically reverse the indexing.
        # This would go like row_index = 0, array_length = 5, we substract one
        # so we can do 0-4 indexing on the column, now we just substrcat 4 - 0, 4 - 1,
        # etc, effectively getting the secondary diagonal
        secondary_diag_sum += arr[i, (arr_len - 1) - i]

        # mainly for validation/debugging
        primary_diag.append(arr[i, i])
        secondary_diag.append(arr[i, (arr_len - 1) - i])

    # basically if the length of the array is odd, the reason for odds,
    # is because we can find perfect center that overlaps, then we need to subtract
    # the element at the middle of the array, that way we dont double count
    both = primary_diag_sum + secondary_diag_sum
    if arr_len % 2 == 1:
        # substract the element at the middle of the array
        both -= arr[arr_len // 2, arr_len // 2]

    print_spacer("PRIMARY DIAGONAL")
    print(f"primary diagonal is {primary_diag}")
    print_spacer("SECONDARY DIAGONAL")
    print(f"secondary diagonal is {secondary_diag}")
    print_spacer()
    return (
        primary_diag_sum,
        secondary_diag_sum,
        both,
    )


p_sum, s_sum, total_sum = calculate_diagonal(arr)
print_spacer("DIAGONAL SUMS")
print(f"primary diagonal sum is {p_sum}")
print(f"secondary diagonal sum is {s_sum}")
print(f"total sum is {total_sum}")
print_spacer()


# Choose any three functions to apply to this array. (25 points)

print_spacer("ARRAY OPERATIONS")
print("array sum", np.sum(arr))
print("array mean", np.mean(arr))
print("array std", np.std(arr))
print_spacer()

# Question 2
# Perform the following actions:
#
# Use x = np.random.randint(0, 1000, size = (10, 10)) to generate 10x10 array and use a for loop to find out how many even numbers are in it. (25 points)

arr2 = np.random.randint(0, 1000, size=(10, 10))


def count_even_numbers(arr: np.ndarray):
    """count even numbers in array

    Args:
        arr (np.ndarray): 2D array

    Returns:
        int: number of even numbers
    """
    even_numbers = 0
    for row in arr:
        for col in row:
            if col % 2 == 0:
                even_numbers += 1
    # pythonic way to do this
    # even_numbers = sum(1 for row in arr for col in row if col % 2 == 0)
    return even_numbers


print_spacer("COUNT EVEN NUMBERS")
print(f"number of even numbers is {count_even_numbers(arr2)}")
print_spacer()


# Randomly generate an 8x9 array from a normal distribution with mean = 1, sigma = 0.5.

arr3 = np.random.normal(1, 0.5, size=(8, 9))

print_spacer("ARRAY 3")
print_initial_data(arr3)
print_spacer()


# Calculate the mean of elements whose indexes have a relation of (i+j)%5 == 0  (i is row index and j is column index).
def find_mean(arr: np.ndarray):
    """find mean of elements whose indexes have a relation of (i+j)%5 == 0

    Args:
        arr (np.ndarray): 2D array

    Returns:
        float: mean of elements whose indexes have a relation of (i+j)%5 == 0
    """
    mean = 0
    element_count = 0
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(len(arr[i])):
            row = i
            col = j
            if (row + col) % 5 == 0:
                mean += arr[row, col]
                element_count += 1
    return mean / element_count


print_spacer("FIND MEAN")
print(
    f"mean of elements whose indexes have a relation of (i+j)%5 == 0 is {find_mean(arr3)}"
)
print_spacer()
