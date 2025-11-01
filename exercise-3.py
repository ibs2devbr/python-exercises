import math;
import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import random;
import seaborn as sns;
import statistics as statistic;

divider_length = 125;

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

print("\n" + "=" * divider_length + "\n");

investment_data = pd.DataFrame({});

investment_data['experience'] = np.array(set_array_number ({
    'min' : 1,
    'max' : 30,
    'length' : 10,
}));

salary = 1518;

investment_data['salary'] = np.array(set_array_number ({
    'min' : salary,
    'max' : salary * 10,
    'length' : 10,
}));

plt.figure(figsize=(10, 6));


sns.histplot(
    investment_data['salary'],
    alpha=0.6,
    bins=8,
    color='skyblue',
    element='step',
    kde=True,
    stat='density',
);
arguments = {
    'color': 'darkblue',
    'fontsize': 14,
    'fontstyle': 'italic',
    'fontweight': 'semibold',
};
plt.title(
    'Distribuição Salarial Anual',
    **arguments,
    loc='left',
    pad=0,
    y=1,
);
arguments = {
    **arguments,
    'labelpad': 10,
};
plt.xlabel('Salarial Anual', **arguments);
plt.ylabel('Frequência', **arguments);
plt.grid(alpha=0.5, axis='both', color='red', linestyle='-', which='major');

plt.show();

print("\n" + "=" * divider_length + "\n");

sns_obj = {
    'data' : investment_data,
    's' : 100,
    'x' : 'experience',
    'y' : 'salary',
};

plt.figure(figsize=(10, 6));
sns.scatterplot(**sns_obj);
argument = {
    'color': 'darkblue',
    'fontsize': 14,
    'fontstyle': 'italic',
    'fontweight': 'semibold',
};
plt.title('Experiência e Salário', **argument);
plt.xlabel('Experiência', **argument);
plt.ylabel('Salário', **argument);
plt.grid(alpha=0.5, axis='both', color='red', linestyle='-', which='major');
plt.show();

print("\n" + "=" * divider_length + "\n");

sns_obj = {
    'data' : investment_data,
    'x' : 'experience',
    'y' : 'salary',
};
plt.figure(figsize=(10, 6))
sns.regplot(**sns_obj);
plt.title('Linha de Regressão: Experiência vs. Salário')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário Anual (em milhares de R$)')
plt.grid(True)
plt.show()

print("\n" + "=" * divider_length + "\n");





correlation = investment_data.corr();
print(correlation);

print("\n" + "=" * divider_length + "\n");





plt.figure(figsize=(10, 6));
sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    vmin=-1,
    vmax=1,
);
plt.title('Matriz de Correlação', fontsize=14);
plt.show();