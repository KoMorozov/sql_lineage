import os
import re
import networkx as nx
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/scripts"
script_files_list = []
list_of_insert = []
list_of_tables = []
schemas = ['db', 'db2']

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        script_files_list.append(path)


def get_queries(file):
    file = file.lower()
    split_queries = file.split(';')
    for i in split_queries:
        if re.search('insert|create', i):
            list_of_insert.append(i)


for script in script_files_list:
    with open(os.path.dirname(os.path.realpath(__file__)) + "/scripts" + f"/{script}") as f:
        contents = f.read()
        get_queries(contents)

for i in list_of_insert:
    list_of_tables.append(re.findall(r'db.\w+|db2.\w+', i))

tuples_of_connections = []
for script in list_of_tables:
        for i in script:
            if i != script[0]:
                tuples_of_connections.append(tuple([i,script[0]]))


first_tables = []

for tables in list_of_tables:
    first_tables.append(tables[0])

#first_tables = list(dict.fromkeys(first_tables))

G = nx.DiGraph()  # создаём объект графа

nodes = first_tables
edges = tuples_of_connections


# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()