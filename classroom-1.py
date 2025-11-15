import math;
import random;
import statistics as statistic;

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import seaborn as sns;

from typing import List;

is_male_name = [
    # Nomes Populares
    "Miguel", "Arthur", "Gael", "Heitor", "Theo", "Davi", "Gabriel", "Bernardo", "Noah", "Samuel", "Lucas", "João", "Enzo", "Matheus", "Pedro", "Rafael", "Daniel", "Antônio", "Luís", "Carlos", "Felipe", "Francisco", "Eduardo", "Ricardo", "Bruno", "Leonardo", "Gustavo", "Henrique", "Vitor", "Thiago", "Vinicius", "Cauã", "Ravi", "Liam",
    # Nomes Compostos Populares
    "João Miguel", "Pedro Henrique", "Enzo Gabriel", "João Lucas", "Luiz Otávio", "Luiz Felipe", "João Guilherme", "Marcos Vinicius", "Davi Lucca", "Paulo César", "José Carlos",
    # Nomes Tradicionais
    "Joaquim", "Sebastião", "Benedito", "Cícero", "Valdir", "Osvaldo", "Raimundo", "Rubens", "Geraldo", "Nelson", "Augusto", "Celso",
    # Nomes Estrangeiros
    "Ben", "Bryan", "Ryan", "Kauan", "Yuri", "Yan", "Zion", "Kevin", "Eric", "Henry", "Oliver", "Lorenzo", "Martin", "Thales", "Nicolas",
    # Nomes Incomuns
    "Belarmino", "Caim", "Donatello", "Eros", "Gaetano", "Talisson", "Oziel", "Tristan", "Ives", "Anibal", "Amenadiel", "Zacarias", "Faustino", "Cornélio", "Hildebrando", "Eleutério", "Belarmino"
];

is_female_name = [
    # Nomes Populares
    "Helena", "Alice", "Laura", "Maria Alice", "Sophia", "Manuela", "Maitê", "Cecília", "Isabella", "Luísa", "Eloá", "Heloísa", "Júlia", "Ayla", "Ísis", "Elisa", "Antonella", "Valentina", "Maya", "Aurora", "Lara", "Giovanna", "Maria Clara", "Beatriz", "Clara", "Yasmin",
    # Nomes Tradicionais
    "Maria", "Ana", "Francisca", "Antônia", "Márcia", "Fernanda", "Aline", "Camila", "Amanda", "Bruna", "Letícia", "Vanessa", "Mariana", "Rita", "Marlene", "Terezinha", "Raimunda", "Adriana", "Cristina", "Patrícia", "Sandra", "Regina", "Sônia", "Vera",
    # Nomes Compostos Populares
    "Maria Cecília", "Maria Júlia", "Maria Eduarda", "Maria Luíza", "Ana Clara", "Ana Luíza", "Ana Júlia", "Laura Beatriz", "Isabela Cristina",
    # Nomes Curto
    "Liz", "Mel", "Nina", "Chloe", "Eva", "Jade", "Gaia", "Zara", "Luna", "Bella", "Stella", "Zoe", "Lívia", "Mila", "Pérola", "Flora",
    # Nomes de Origem Estrangeira
    "Sophie", "Tiffany", "Kéfera", "Greta", "Chloe", "Dominique", "Ayanna", "Farah", "Alina", "Filipa", "Zoé", "Aisha", "Celine", "Penélope", "Lavínia", "Olivia",
    # Nomes Raros
    "Dandara", "Uyara", "Ipanema", "Ayra", "Inaiá", "Filomena", "Esperanza", "Kalliope", "Mirela", "Harumi"
];

is_first_name = is_male_name + is_female_name;

is_last_name = [
    # Os 10 Sobrenomes Mais Comuns
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes",
    # Sobrenomes Portugueses
    "Carvalho", "Ribeiro", "Costa", "Martins", "Cardoso", "Barbosa", "Freitas", "Dias", "Nunes", "Pinto",
    # Sobrenomes de Imigração Comuns (Italianos, Espanhóis, Alemães)
    "Rossi", "Ferrari", "Conti", "Galli", "Benetti", "Zanetti", "Ricci", "Colombo",
    # Espanhóis
    "Hernandes", "Gutiérrez", "Ramirez", "Sánchez",
    # Alemães
    "Schmidt", "Schulz", "Becker", "Weber", "Klein",
    # Japoneses
    "Yamamoto", "Tanaka", "Suzuki", "Sato",
    # Árabes
    "Haddad", "Maluf", "Nasser", "Salloum",
    # Sobrenomes Diversos
    "Müller",
];

def set_divider(input = '='):
    is_divider = 150;
    if (input == '='): is_text = "\n" + input * is_divider + "\n";
    elif (input != '='): is_text = input * is_divider;
    print(is_text);

def set_join(input = [], between = ', '): return (between.join(np.array(input).astype(str)));

def set_choice(input = []): return random.choice(input);

def has_key(input = {}, key = ''): return key in input;

def set_array_fullname(input = 5):
    global is_first_name, is_last_name;
    is_result = [];
    for _ in range(input):
        is_result.append((f"{set_choice(is_first_name)} {set_choice(is_last_name)} {set_choice(is_last_name)}").title());
    return is_result;

def set_array_number(input = {}):
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
def set_array_number_decimal(input = {}):
    proper = {
        'length' : input.get('length', 10),
        'min' : input.get('min', 40),
        'max' : input.get('max', 50),
    };
    is_result = [];
    is_multiplier = 10 ** 1;
    is_whole = range(int(proper['min'] * is_multiplier), int(proper['max'] * is_multiplier) + 1, 1);
    is_final = [ is_valor / is_multiplier for is_valor in is_whole ];
    for _ in range(proper['length']): is_result.append(random.choice(is_final));
    is_result = sorted(is_result);
    return is_result;

def set_range(start = 0, end = 0): return range(start, start + end);

set_divider();

is_array_number = np.array(set_array_number());
print((f"note: {set_join(is_array_number)}.").title());

set_divider('-');

def get_attrib (input = {}):
    proper = {
        'key' : input.get('key', ''),
        'database' : input.get('database', []),
    };
    is_bullet = '-' * 5 + ' ';
    if (proper['key'] != ''): print((f"{proper['key']}:").title());
    print((f"{is_bullet}ampleness: {(proper['database'].max() - proper['database'].min()):.2f}.").title());
    print((f"{is_bullet}max: {proper['database'].max():.2f}.").title());
    print((f"{is_bullet}mean: {statistic.mean(proper['database']):.2f}.").title());
    print((f"{is_bullet}min: {proper['database'].min():.2f}.").title());
    print((f"{is_bullet}std: {proper['database'].std():.2f}.").title());
    print((f"{is_bullet}sum: {proper['database'].sum():.2f}.").title());
    print((f"{is_bullet}var: {proper['database'].var():.2f}.").title());

get_attrib({
    'database' : is_array_number
});

set_divider();

is_database = pd.DataFrame({
    'full-name' : set_array_fullname(),
});
is_length = len(is_database['full-name']);
is_database['note'] = set_array_number ({
    'length' : is_length,
});
is_database['absence'] = set_array_number ({
    'length' : is_length,
});
print(is_database);

set_divider('-');

i = set_choice(set_range(0, is_length));

print((f"full name: {is_database['full-name'][i]}.").title());
print((f"note: {is_database['note'][i]:.2f}.").title());
print((f"absence: {is_database['absence'][i]:.2f}.").title());

set_divider();

def get_information (input = {}):
    proper = {
        'key' : input.get('key', 'note'),
        'database' : input.get('database', []),
    };
    get_attrib ({
        'key' : proper['key'],
        'database' : proper['database'][proper['key']],
    });

get_information ({ 'database' : is_database });

set_divider('-');

get_information ({ 'database' : is_database, 'key' : 'absence' });

set_divider();

def get_analysis (input = {}):
    proper = {
        'title' : input.get('title', ''),
        'table' : input.get('table', []),
    };
    if has_key(proper['table'], 'a') and has_key(proper['table'], 'b'):
        is_description = '';
        if (proper['title'] == 'machine'): is_description = 'screws';
        elif (proper['title'] == 'class'): is_description = 'notes';
        def set_description (input = {}):
            proper = {
                'title' : input.get('title', ''),
                'description' : input.get('description', ''),
                'table' : input.get('table', []),
                'key' : input.get('key', 'a'),
            };
            is_key = proper['key'];
            is_value = proper['table'][is_key];
            print((f"{proper['title']} ({is_key}):").title());
            print((f"{proper['description']}: {set_join(is_value)}.").title());
            print((f"mean: {is_value.mean():.2f}.").title());
            print((f"inconsistency: {is_value.std():.2f}.").title());
            set_divider('-');
        is_description = {
            'description' : is_description,
            'title' : proper['title'],
            'table' : proper['table'] 
        };
        set_description({ **is_description, 'key' : 'a' });
        set_description({ **is_description, 'key' : 'b' });
        if proper['table']['a'].std() < proper['table']['b'].std():
            print((f"{proper['title']} (a) more consistent.").title());
            print((f"{proper['title']} (b) less consistent.").title());
        elif proper['table']['a'].std() > proper['table']['b'].std():
            print((f"{proper['title']} (a) less consistent.").title());
            print((f"{proper['title']} (b) more consistent.").title());
        else:
            print((f"both {proper['title']}s have the same consistency.").title());
        set_divider();
    else:
        print(("invalid object.").title());

def get_table ():
    return pd.DataFrame({
        'a' : np.array (set_array_number ()),
        'b' : np.array (set_array_number ()),
    });

get_analysis ({
    'title' : 'class',
    'table' : get_table(),
});

get_analysis ({
    'title' : 'machine',
    'table' : get_table(),
});