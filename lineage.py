import os
import re
import networkx as nx
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\scripts"

schemas = ['db', 'db2']

script_files_list = []

for path, subdirs, files in os.walk(dir_path):
    for name in files:
        if ".txt" in name:
            script_files_list.append(os.path.join(path, name))

list_of_insert = []


def get_queries(file):
    file = file.lower()
    split_queries = file.split(';')
    for i in split_queries:
        if re.search('insert|create', i):
            list_of_insert.append(i)


for script in script_files_list:
    with open(script) as f:
        contents = f.read()
        get_queries(contents)

list_of_tables = []

for i in list_of_insert:
    list_of_tables.append(re.findall(r'db.\w+|db2.\w+|dm.\w+', i))

tuples_of_connections = []
for script in list_of_tables:
    for i in script:
        if i != script[0]:
            tuples_of_connections.append(tuple([i, script[0]]))

first_tables = []

for tables in list_of_tables:
    first_tables.append(tables[0])

G = nx.DiGraph()  # создаём объект графа

nodes = first_tables
edges = tuples_of_connections

# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
