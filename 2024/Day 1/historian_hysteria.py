# -*- coding: utf-8 -*-
"""historian_hysteria.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a3WGDa3ZcY2intOsd4kNiPvRwdB2Elrt
"""

import numpy as np
import pandas as pd

data = np.loadtxt("actual_input.txt")
left = data[:, 0]
right = data[:, 1]

left_sorted = np.sort(l1)
right_sorted = np.sort(l2)

part1 = np.sum(np.absolute(left_sorted - right_sorted))
print(part1)

from collections import Counter

left_list = left.tolist()
right_list = right.tolist()
right_counter = Counter(right)

part2 = sum(num_left * right_counter.get(num_left, 0) for num_left in left_list)
print(part2)
