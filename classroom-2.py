import math;
import random;
import statistics as statistic;

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

from typing import List;

def has_key (input = {}, key = ''): return key in input;

def set_array_number (input = {}):
    proper = {
        'length' : input.get('length', 10),
        'min' : input.get('min', 1),
        'max' : input.get('max', 10),
    };
    is_result = [];
    for _ in range(proper['length']):
        is_result.append(random.randint(proper['min'], proper['max']));
    is_result = sorted(is_result);
    return is_result;

is_array_number = set_array_number ({
    'length' : 15,
    'max' : 25,
});

def is_mean (input = []): return sum (input) / len (input);

def is_var (input = []):
  array = [];
  for is_current_number in input: array.append ((is_current_number - is_mean (input)) ** 2);
  return is_mean (array);

def is_std (input = []): return math.sqrt (is_var (input));

def is_max (input = []):
    if not input:
        raise ValueError("a lista está vazia.");
    is_maximum_number = input[0];
    for is_current_number in input:
        if is_current_number > is_maximum_number:
            is_maximum_number = is_current_number;
    return is_maximum_number;

def is_min (input = []):
    if not input:
        raise ValueError("A lista está vazia.");
    is_minimum_number = input[0];
    for is_current_number in input:
        if is_current_number < is_minimum_number:
            is_minimum_number = is_current_number;
    return is_minimum_number;

def set_join (input = [], between = ', '): return (between.join(np.array(input).astype(str)));

print((f"array: {set_join(is_array_number)}.").title());
print((f"max: {is_max(is_array_number):.2f}.").title());
print((f"mean: {is_mean(is_array_number):.2f}.").title());
print((f"min: {is_min(is_array_number):.2f}.").title());
print((f"std: {is_std(is_array_number):.2f}.").title());
print((f"var: {is_var(is_array_number):.2f}.").title());