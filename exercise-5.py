import math;
import random;
import statistics as statistic;

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

from typing import List;

# import _function;
# _function.has_key();
# _function.set_array_number_decimal();
# _function.set_array_number();
# _function.set_array_random();
# _function.set_array_sort();
# _function.set_database_filter();
# _function.set_divider();
# _function.set_format();
# _function.set_join();
# _function.set_range();

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

# 

is_value = 15;
if (is_value > 10): print("Esta é uma venda de alto valor.");
elif (is_value > 5): print("Esta é uma venda de valor médio.");
else: print("Esta é uma venda de baixo valor.");
set_divider();

# 

is_value = "Café";
if (is_value == "Café"): print("É uma venda de Café.");
if (is_value != "Leite"): print("Não é uma venda de Leite.");
set_divider();

# 

is_product = [ 'Café', 'Açúcar', 'Leite', 'Pão', 'Manteiga', 'Café', 'Leite', 'Pão', 'Açúcar', 'Café' ];
is_product.sort();
is_database = pd.DataFrame({ 'product' : is_product });
is_everyone = { 'length' : len(is_database['product']) };
is_database['commission'] = set_array_number_decimal({ **is_everyone, 'min' : 0.5, 'max' : 1.5 });
is_database['stock'] = set_array_number({ **is_everyone, 'min' : 1, 'max' : 100 });
is_database['value'] = set_array_number_decimal ({ **is_everyone, 'min' : 6, 'max' : 12 });
print(is_database);
set_divider();

# 

is_name = [ 'Rex', 'Luna', 'Fido', 'Nina', 'Thor', 'Mimi' ];
is_database = pd.DataFrame({
    'name' : set_array_sort(is_name),
});
is_length = len(is_database['name']);
is_everyone = { 'length' : is_length };
is_database['age'] = set_array_number({ **is_everyone, 'min' : 1, 'max' : 12 });
is_database['specie'] = set_array_random([ 'Cachorro', 'Gato' ], is_length);
is_database['vaccinated'] = set_array_random([ True, False ], is_length);
is_database['weight'] = set_array_number({ **is_everyone, 'min' : 4, 'max' : 30 });
print(is_database);
set_divider();

# 

set_database_filter(is_database[
    (is_database['age'] > 7)
]);
set_database_filter(is_database[
    (is_database['specie'] == 'Gato')
]);
set_database_filter(is_database[
    (is_database['vaccinated'] == True)
]);
set_database_filter(is_database[
    (is_database['weight'] > 20)
]);

# 

is_product = [ 'Arroz', 'Feijão', 'Óleo', 'Sal', 'Macarrão', 'Café' ];
is_database = pd.DataFrame({
    'product' : set_array_sort(is_product),
});
is_length = len(is_database['product']);
is_everyone = { 'length' : is_length };
is_database['category'] = set_array_random([ 'Grãos', 'Mercearia' ], is_length);
is_database['stock'] = set_array_number({ **is_everyone, 'min' : 1, 'max' : 100 });
is_database['price'] = set_array_number_decimal({ **is_everyone, 'min' : 5, 'max' : 25 });
print(is_database);
set_divider();

# 

set_database_filter(is_database[
    (is_database['stock'] < 10)
]);
set_database_filter(is_database[
    (is_database['category'] == 'Mercearia')
]);
set_database_filter(is_database[
    (is_database['category'] == 'Grãos') & (is_database['price'] < 10)
]);

# 

is_name = [ 'Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa', 'Fábio' ];
is_database = pd.DataFrame({
    'name' : set_array_sort(is_name),
});
is_length = len(is_database['name']);
is_everyone = { 'length' : is_length };
is_database['absence'] = set_array_number({ **is_everyone, 'min' : 0, 'max' : 10 });
is_database['note'] = set_array_number_decimal({ **is_everyone, 'min' : 0, 'max' : 10 });
is_database['register'] = set_range(100, is_length);
print(is_database);
set_divider();

# 

set_database_filter(is_database[
    (is_database['note'] > 7)
]);
set_database_filter(is_database[
    (is_database['absence'] > 5)
]);
set_database_filter(is_database[
    (is_database['absence'] == 1) & (is_database['note'] > 9)
]);

# 

is_seller = [ 'Rafael', 'Bia', 'Carlos', 'Rafael', 'Bia', 'Carlos' ];
is_seller.sort();
is_database = pd.DataFrame({ 
    'seller': is_seller,
}); 
is_length = len(is_database['seller']);
is_everyone = { 'length' : is_length };
is_region = [ 'South', 'Southeast', 'Northeast', 'Southeast', 'South', 'Southeast' ];
is_database['region'] = set_array_random(set_array_sort(is_region), is_length);
is_database['type'] = set_array_random([ 'online', 'in-person' ], is_length);
is_database['value'] = set_array_number({ **is_everyone, 'min' : 1000, 'max' : 2000 });
print(is_database);
set_divider();

# 

set_database_filter(is_database[
    (is_database['seller'] == 'Bia')
]);

set_database_filter(is_database[
    (is_database['value'] > 1400)
]);

set_database_filter(is_database[
    (is_database['value'] == 'South') & (is_database['region'] == 'Southeast')
]);

set_database_filter(is_database[
    (is_database['type'] != 'online')
]);

# 

is_seller = [ 'Rafael', 'Bia', 'Carlos', 'Rafael', 'Bia', 'Carlos' ];
is_seller.sort();
is_database = pd.DataFrame({ 
    'seller': is_seller,
}); 
is_length = len(is_database['seller']);
is_everyone = { 'length' : is_length };
is_region = [ 'Center', 'Beach', 'Center', 'North', 'Beach', 'South' ];
is_database['area'] = set_array_number({ **is_everyone, 'min' : 50, 'max' : 200 });
is_database['region'] = set_array_random(set_array_sort(is_region), is_length);
is_database['room'] = set_array_number({ **is_everyone, 'min' : 1, 'max' : 5 });
is_database['type'] = set_array_random([ 'Apartment', 'House' ], is_length);
is_database['value'] = set_array_number({ **is_everyone, 'min' : 1000, 'max' : 2000 });
print(is_database);
set_divider();