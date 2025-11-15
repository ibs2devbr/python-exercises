import math;
import random;
import statistics as statistic;

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

from typing import List;

def set_divider(input = '='):
    is_divider = 150;
    if (input == '='): is_text = "\n" + input * is_divider + "\n";
    elif (input != '='): is_text = input * is_divider;
    print(is_text);

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

set_divider();

is_database = pd.DataFrame({});
is_database['experience'] = np.array(set_array_number ({
    'min' : 1,
    'max' : 30,
}));
is_salary = 1518;
is_database['salary'] = np.array(set_array_number ({
    'min' : is_salary,
    'max' : is_salary * 10,
}));
plt.figure(figsize=(10, 6));
sns.histplot(
    is_database['salary'],
    alpha=0.6,
    bins=8,
    color='skyblue',
    element='step',
    kde=True,
    stat='density',
);
is_argument = {
    'color': 'darkblue',
    'fontsize': 14,
    'fontstyle': 'italic',
    'fontweight': 'semibold',
};
plt.title(
    'Distribuição Salarial Anual',
    **is_argument,
    loc='left',
    pad=0,
    y=1,
);
is_argument = {
    **is_argument,
    'labelpad': 10,
};
plt.xlabel('Salarial Anual', **is_argument);
plt.ylabel('Frequência', **is_argument);
plt.grid(alpha=0.5, axis='both', color='red', linestyle='-', which='major');
plt.show();

set_divider();

sns_obj = {
    'data' : is_database,
    's' : 100,
    'x' : 'experience',
    'y' : 'salary',
};
plt.figure(figsize=(10, 6));
sns.scatterplot(**sns_obj);
is_argument = {
    'color': 'darkblue',
    'fontsize': 14,
    'fontstyle': 'italic',
    'fontweight': 'semibold',
};
plt.title('Experiência e Salário', **is_argument);
plt.xlabel('Experiência', **is_argument);
plt.ylabel('Salário', **is_argument);
plt.grid(alpha=0.5, axis='both', color='red', linestyle='-', which='major');
plt.show();

set_divider();

sns_obj = {
    'data' : is_database,
    'x' : 'experience',
    'y' : 'salary',
};
plt.figure(figsize=(10, 6));
sns.regplot(**sns_obj);
plt.title('Linha de Regressão: Experiência vs. Salário');
plt.xlabel('Anos de Experiência');
plt.ylabel('Salário Anual.');
plt.grid(True);
plt.show();

set_divider();

is_correlation = is_database.corr();
print(is_correlation);

set_divider();

plt.figure(figsize=(10, 6));
sns.heatmap(
    is_correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    vmin=-1,
    vmax=1,
);
plt.title('Matriz de Correlação', fontsize=14);
plt.show();

set_divider();