import math;
import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import random;
import seaborn as sns;
import statistics as statistic;

def has_key (input = {}, key = ''): return key in input;

def set_array_number(input = {}):
    proper = {
        'length' : input.get('length', 15),
        'min' : input.get('min', 1),
        'max' : input.get('max', 15),
    };
    result = [];
    for _ in range(proper['length']):
        result.append(random.randint(proper['min'], proper['max']));
    result = sorted(result);
    return result;

def set_join(input = [], between = ', '): return (between.join(np.array(input).astype(str)));

divider_length = 150;

marketing_database = pd.DataFrame({
    'investment' : set_array_number ({ 'min' : 10, 'max' : 100 }),
    'visitor' : set_array_number ({ 'min' : 300, 'max' : 3000 }),
});

logistic_database = pd.DataFrame({
    'x' : set_array_number (),
    'y' : set_array_number (),
});

def get_attrib_obj (input = []):
    return {
        'ampleness' : round(input.max() - input.min(), 2),
        'max' : round(max(input), 2),
        'mean' : round(statistic.mean(input), 2),
        'median' : round(input.median(), 2),
        'min' : round(input.min(), 2),
        'std' : round(input.std(), 2),
        'sum' : round(input.sum(), 2),
        'var' : round(input.var(), 2),
    };

def get_attrib (input = []):
    length = 2;
    bullet = "";
    if (length > 1): bullet = "-" * length + " ";
    for key, value in get_attrib_obj(input).items():
        print((f"{bullet}{key} : {value:.2f}.").title());
    print("\n" + "=" * divider_length + "\n");

print(marketing_database);
print("-" * divider_length);
print((f"investment: {set_join (marketing_database['investment'])}.").title());
print((f"visitor: {set_join (marketing_database['visitor'])}.").title());
print("-" * divider_length);
get_attrib(marketing_database['investment']);
print("-" * divider_length);
get_attrib(marketing_database['visitor']);

print("\n" + "=" * divider_length + "\n");

def set_chart (input = []):
    global divider_length;
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
    argument_text = { 'color' : 'darkblue', 'fontsize' : 14, 'fontstyle' : 'italic', 'fontweight' : 'bold' };
    plt.title(proper['title'].title(), **argument_text, **{ 'loc' : 'left', 'pad' : 0, 'y' : 1 });
    plt.xlabel(proper['xlabel'].title(), **argument_text);
    plt.ylabel(proper['ylabel'].title(), **argument_text);
    plt.grid(**{ 'alpha' : .5, 'axis' : 'both', 'color' : 'red', 'linestyle' : '-', 'linewidth' : .8, 'which' : 'major' });
    plt.show();

library = [ 'histplot', 'scatterplot', 'regplot', 'boxplot' ];

for theme in library: set_chart ({ 'data' : logistic_database, 'theme' : theme });
print("\n" + "=" * divider_length + "\n");

logistic_x_median = get_attrib_obj (logistic_database['x'])['median'];
logistic_y_median = get_attrib_obj (logistic_database['y'])['median'];

logistic_x_std = get_attrib_obj (logistic_database['x'])['std'];
logistic_y_std = get_attrib_obj (logistic_database['y'])['std'];

logistic_x_value = logistic_y_value = 0;

logistic_x_value += 1 if logistic_x_std < logistic_y_std else 0;
logistic_x_value += 1 if logistic_x_median > logistic_y_median else 0;

logistic_y_value += 1 if logistic_y_std < logistic_y_std else 0;
logistic_y_value += 1 if logistic_y_median > logistic_y_median else 0;

if (logistic_x_value > logistic_y_value):
    print("a transportadora melhor é \"X\".");
elif (logistic_x_value < logistic_y_value):
    print("a transportadora melhor é \"Y\".");

print("\n" + "=" * divider_length + "\n");

for theme in library: set_chart ({ 'data' : marketing_database, 'theme' : theme });
print("\n" + "=" * divider_length + "\n");