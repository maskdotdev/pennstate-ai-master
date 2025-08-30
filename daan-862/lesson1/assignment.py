import numpy as np

L1 = []

np.random.seed(56)

for i in np.random.randint(0, 100, 10):
    L1.extend([i] * np.random.randint(0, 100, 1)[0])

np.random.shuffle(L1)

# unique values
print("unique values:",np.unique(L1))
print("total unique values:",len(np.unique(L1)))

# dict of unique items, unique items as keys, counts as values
print("dict of unique items, unique items as keys, counts as values:")
print(dict(zip(np.unique(L1), np.bincount(L1))))

# most frequent value
print("most frequent value:")
print(np.bincount(L1).argmax())

