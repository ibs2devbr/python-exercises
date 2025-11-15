import math;
import random;
import statistics as statistic;

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

from typing import List;

def has_key (input = {}, key = ''): return key in input;

def set_array_number(input = {}):
    proper = {
        'length' : input.get('length', 10),
        'min' : input.get('min', 1),
        'max' : input.get('max', 10),
    };
    is_result = [];
    for _ in range(proper['length']): is_result.append(random.randint(proper['min'], proper['max']));
    is_result = sorted(is_result);
    return is_result;

def set_join(input = [], between = ', '): return (between.join(np.array(input).astype(str)));

def set_divider(input = '='):
    is_divider = 150;
    if (input == '='): is_text = "\n" + input * is_divider + "\n";
    elif (input != '='): is_text = input * is_divider;
    print(is_text);

def get_attrib_obj (input = []):
    return {
        'ampleness' : round(input.max() - input.min(), 2),
        'max' : round(input.max(), 2),
        'mean' : round(statistic.mean(input), 2),
        'median' : round(input.median(), 2),
        'min' : round(input.min(), 2),
        'std' : round(input.std(), 2),
        'sum' : round(input.sum(), 2),
        'var' : round(input.var(), 2),
    };

def get_attrib (input = []):
    proper = {
        'key' : input.get('key', ''),
        'database' : input.get('database', []),
    };
    is_bullet = '-' * 5 + ' ';
    if (proper['key'] != ''): print((f"{proper['key']}:").title());
    for is_key, is_value in get_attrib_obj(proper['database']).items():
        print((f"{is_bullet}{is_key} : {is_value:.2f}.").title());

is_database = pd.DataFrame({
    'investment' : set_array_number ({ 'min' : 100, 'max' : 1000 }),
    'visitor' : set_array_number ({ 'min' : 300, 'max' : 3000 }),
});

print(is_database);

set_divider('-');
    
print((f"investment: {set_join (is_database['investment'])}.").title());
print((f"visitor: {set_join (is_database['visitor'])}.").title());

set_divider('-');

get_attrib({
    'key' : 'investment',
    'database' : is_database['investment'],
});

set_divider('-');

get_attrib({
    'key' : 'visitor',
    'database' : is_database['visitor'],
});

set_divider();

def set_chart (input = []):
    proper = {
        'data' : input.get('data', []),
        'theme' : input.get('theme', 'boxplot'),
        'title' : input.get('title', 'Eficiência'),
        'xlabel' : input.get('xlabel', 'Transportadora'),
        'ylabel' : input.get('ylabel', 'Velocidade'),
    };
    plt.figure(**{ 'figsize' : [ 10, 6 ] });
    plt_function = getattr(sns, proper['theme']);
    array = list(proper['data'][:2]);
    plt_function (
        **{ 'data' : proper['data'] },
        **{ 'x' : array[0] } if has_key (proper['data'], array[0]) else {},
        **{ 'y' : array[1] } if has_key (proper['data'], array[1]) else {},
        **{ 's' : 100, } if proper['theme'] == 'scatterplot' else {},
        **{ 'alpha' : .6, 'bins' : 8, 'color' : 'skyblue', 'element' : 'step', 'kde' : True, 'stat' : 'density' } if proper['theme'] == 'histplot' else {},
        **{ 'annot' : True, 'cmap' : 'coolwarm', 'fmt' : '.2f', 'vmin' : - 1, 'vmax' : 1 } if proper['theme'] == 'heatmap' else {},
    );
    is_argument_text = { 'color' : 'darkblue', 'fontsize' : 14, 'fontstyle' : 'italic', 'fontweight' : 'bold' };
    plt.title(proper['title'].title(), **is_argument_text, **{ 'loc' : 'left', 'pad' : 0, 'y' : 1 });
    plt.xlabel(proper['xlabel'].title(), **is_argument_text);
    plt.ylabel(proper['ylabel'].title(), **is_argument_text);
    plt.grid(**{ 'alpha' : .5, 'axis' : 'both', 'color' : 'red', 'linestyle' : '-', 'linewidth' : .8, 'which' : 'major' });
    plt.show();

def set_chart_themes (input = []):
    for theme in [ 'histplot', 'scatterplot', 'regplot', 'boxplot' ]:
        set_chart ({ 'data' : input, 'theme' : theme });
    set_divider();

set_chart_themes (is_database);

is_database = pd.DataFrame({
    'x' : set_array_number (),
    'y' : set_array_number (),
});

set_chart_themes (is_database);

is_x_median = get_attrib_obj (is_database['x'])['median'];
is_y_median = get_attrib_obj (is_database['y'])['median'];
is_x_std = get_attrib_obj (is_database['x'])['std'];
is_y_std = get_attrib_obj (is_database['y'])['std'];
is_x_value = is_y_value = 0;
is_x_value += 1 if is_x_std < is_y_std else 0;
is_x_value += 1 if is_x_median > is_y_median else 0;
is_y_value += 1 if is_y_std < is_y_std else 0;
is_y_value += 1 if is_y_median > is_y_median else 0;

if (is_x_value > is_y_value): print((f"a melhor transportadora é a \"X\".").title());
elif (is_x_value < is_y_value): print((f"a melhor transportadora é a \"Y\".").title());

set_divider();