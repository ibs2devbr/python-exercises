import math;
import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import random;
import seaborn as sns;
import statistics as statistic;

def has_key (input = {}, key = ''): return key in input;

def set_array_number (input = {}):
    proper = {
        'length' : input['length'] if has_key(input, 'length') else 10,
        'min' : input['min'] if has_key(input, 'min') else 1,
        'max' : input['max'] if has_key(input, 'max') else 10,
    };
    result = [];
    for _ in range(proper['length']):
        result.append(random.randint(proper['min'], proper['max']));
    result = sorted(result);
    return result;

array_number = set_array_number ({
    'length' : 15,
    'max' : 25,
});

def is_mean (input = []): return sum (input) / len (input);

def is_var (input = []):
  array = [];
  for current_number in input: array.append ((current_number - is_mean (input)) ** 2);
  return is_mean (array);

def is_std (input = []): return math.sqrt (is_var (input));

def is_max (input = []):
    if not input:
        raise ValueError("a lista está vazia.");
    maximum_number = input[0];
    for current_number in input:
        if current_number > maximum_number:
            maximum_number = current_number;
    return maximum_number;

def is_min (input = []):
    if not input:
        raise ValueError("A lista está vazia.");
    minimum_number = input[0];
    for current_number in input:
        if current_number < minimum_number:
            minimum_number = current_number;
    return minimum_number;

def set_join (input = [], between = ', '): return (between.join(np.array(input).astype(str)));

print((f"array: {set_join(array_number)}.").title());
print((f"max: {is_max(array_number):.2f}.").title());
print((f"mean: {is_mean(array_number):.2f}.").title());
print((f"min: {is_min(array_number):.2f}.").title());
print((f"std: {is_std(array_number):.2f}.").title());
print((f"var: {is_var(array_number):.2f}.").title());