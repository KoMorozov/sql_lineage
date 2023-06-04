import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/scripts"
script_files_list = []

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        script_files_list.append(path)


def get_tables(file, file_name):
    split_queries = file.split(';')
    for i in split_queries:
        if "create" in i:
            print(1)
        else:
            print(2)



for script in script_files_list:
    with open(os.path.dirname(os.path.realpath(__file__)) + "/scripts" + f"/{script}") as f:
        contents = f.read()
        get_tables(contents, script)




