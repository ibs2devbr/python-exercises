import math;
import random;
import statistics as statistic;

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

from typing import List;

is_divider = 100;

def has_key(input = {}, key = ''): return key in input;

def set_array_number_decimal(input = {}):
    proper = {
        'length' : input.get('length', 10),
        'min' : input.get('min', 40),
        'max' : input.get('max', 50),
    };
    is_result = [];
    is_multiplier = 10 ** 1;
    proper['min'] = (proper['max'] + proper['length']) if proper['min'] >= proper['max'] else proper['min'];
    proper['max'] = (proper['min'] + proper['length']) if proper['max'] <= proper['min'] else proper['max'];
    is_whole = range(int(proper['min'] * is_multiplier), int(proper['max'] * is_multiplier) + 1, 1);
    is_final = [ valor / is_multiplier for valor in is_whole ];
    for _ in range(proper['length']):
        is_result.append(random.choice(is_final));
    is_result = sorted(is_result);
    return is_result;

def set_array_number(input = {}):
    proper = {
        'length' : input.get('length', 15),
        'min' : input.get('min', 1),
        'max' : input.get('max', 15),
    };
    result = [];
    proper['min'] = (proper['max'] + proper['length']) if proper['min'] >= proper['max'] else proper['min'];
    proper['max'] = (proper['min'] + proper['length']) if proper['max'] <= proper['min'] else proper['max'];
    for _ in range(proper['length']):
        result.append(random.randint(proper['min'], proper['max']));
    result = sorted(result);
    return result;

def set_array_random(array: List[str], number: int) -> List[str]:
    return random.choices(array, k=number);

def set_array_sort(input = []):
    is_array = set(input);
    is_array = list(is_array);
    is_array.sort();
    return is_array;

def set_database_filter(input):
    if isinstance(input, pd.DataFrame):
        if not input.empty:
            print(input);
            set_divider();

def set_divider():
    global is_divider;
    print("-" * is_divider);

def set_format(input = []): return f"r${input:.2f}".replace('.', ',');

def set_join(input = [], between = ', '): return (between.join(np.array(input).astype(str)));

def set_range(start = 0, end = 0):
    return range(start, start + end);