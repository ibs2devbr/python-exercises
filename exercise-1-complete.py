import math;
import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import random;
import seaborn as sns;
import statistics as statistic;

male_name = [
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

female_name = [
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

first_name = male_name + female_name;

last_name = [
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

divider_length = 150;

def set_join(input = [], between = ', '): return (between.join(np.array(input).astype(str)));

def set_choice(input = []): return random.choice(input);

def has_key(input = {}, key = ''): return key in input;

def set_array_fullname(input = 5):
    global first_name, last_name;
    result = [];
    for _ in range(input):
        result.append((f"{set_choice(first_name)} {set_choice(last_name)} {set_choice(last_name)}").title());
    return result;

def set_array_number(input = {}):
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

def set_array_number_decimal(input = {}):
    proper = {
        'length' : input['length'] if has_key(input, 'length') else 10,
        'min' : input['min'] if has_key(input, 'min') else 40,
        'max' : input['max'] if has_key(input, 'max') else 50,
    };
    result = [];
    multiplier = 10 ** 1;
    whole = range(int(proper['min'] * multiplier), int(proper['max'] * multiplier) + 1, 1);
    final = [ valor / multiplier for valor in whole ];
    for _ in range(proper['length']):
        result.append(random.choice(final));
    result = sorted(result);
    return result;

print("\n" + "=" * divider_length + "\n");

array_number = np.array(set_array_number());
print((f"note: {set_join(array_number)}.").title());
def get_attribute (input = []):
    length = 2;
    bullet = "";
    if (length > 1): bullet = "-" * length + " ";
    print((f"{bullet}ampleness: {(max(input) - min(input)):.2f}.").title());
    print((f"{bullet}max: {max(input):.2f}.").title());
    print((f"{bullet}mean: {statistic.mean(input):.2f}.").title());
    print((f"{bullet}min: {min(input):.2f}.").title());
    # print((f"{bullet}mode: {input.mode()[0]:.2f}.").title());
    print((f"{bullet}std: {input.std():.2f}.").title());
    print((f"{bullet}sum: {sum(input):.2f}.").title());
    print((f"{bullet}var: {input.var():.2f}.").title());
get_attribute(array_number);
print("\n" + "=" * divider_length + "\n");

print((f"name: {set_choice(set_array_fullname())}.").title());
print((f"note: {set_choice(set_array_number()):.2f}.").title());
print("\n" + "=" * divider_length + "\n");

database = pd.DataFrame({
    'full-name' : set_array_fullname (),
});
database['note'] = set_array_number ({
    'length' : len(database['full-name']),
});
database['absence'] = set_array_number ({
    'length' : len(database['full-name']),
});
print(database);
print("-" * divider_length);
def get_information (input = {}):
    proper = {
        'key' : input['key'] if has_key (input, 'key') else 'note',
        'database' : input['database'] if has_key (input, 'database') else [],
    };
    print((f"{proper['key']}:").title());
    get_attribute (proper['database'][proper['key']]);
get_information ({
    'database' : database,
});
print("-" * divider_length);
get_information ({
    'database' : database,
    'key' : 'absence',
});
print("\n" + "=" * divider_length + "\n");

def get_analysis (input = {}):
    global divider_length;
    proper = {
        'title' : input['title'] if has_key(input, 'title') else '',
        'table' : input['table'] if has_key(input, 'table') else [],
        # (SE VERDADEIRO) IF (CONDIÇÃO) ELSE (SE FALSO)
    };
    if has_key(proper['table'], 'a') and has_key(proper['table'], 'b'):
        description = '';
        if (proper['title'] == 'machine'): description = 'screws';
        elif (proper['title'] == 'class'): description = 'notes';
        def set_description (input = {}):
            global divider_length;
            proper = {
                'title' : input['title'] if has_key(input, 'title') else '',
                'description' : input['description'] if has_key(input, 'description') else '',
                'table' : input['table'] if has_key(input, 'table') else [],
                'key' : input['key'] if has_key(input, 'key') else 'a',
            };
            key = proper['key'];
            key_value = proper['table'][key];
            print((f"{proper['title']} ({key}):").title());
            print((f"{proper['description']}: {set_join(key_value)}.").title());
            print((f"mean: {key_value.mean():.2f}.").title());
            print((f"inconsistency: {key_value.std():.2f}.").title());
            print("-" * divider_length);
        description = {
            'description' : description,
            'title' : proper['title'],
            'table' : proper['table'],
        };
        set_description({ **description, 'key' : 'a' });
        set_description({ **description, 'key' : 'b' });
        if proper['table']['a'].std() < proper['table']['b'].std():
            print((f"{proper['title']} (a) more consistent.").title());
            print((f"{proper['title']} (b) less consistent.").title());
        elif proper['table']['a'].std() > proper['table']['b'].std():
            print((f"{proper['title']} (a) less consistent.").title());
            print((f"{proper['title']} (b) more consistent.").title());
        else:
            print((f"both {proper['title']}s have the same consistency.").title());
        print("\n" + "=" * divider_length + "\n");
    else:
        print(("invalid object.").title());

def get_table (): return pd.DataFrame({
    'a' : np.array (set_array_number ()),
    'b' : np.array (set_array_number ()),
});

get_analysis ({ 'title' : 'class', 'table' : get_table () });

get_analysis ({ 'title' : 'machine', 'table' : get_table () });