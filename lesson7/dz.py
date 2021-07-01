import os
import shutil

# Задание 1

try:
    project_dict = {
        'name': 'my_project',
        'settings': 'settings',
        'main': 'mainapp',
        'admin': 'adminapp',
        'auth': 'authapp',
    }

    for i in project_dict:
        if i != 'name':
            os.makedirs(f'{project_dict["name"]}\\{project_dict[f"{i}"]}')

except FileExistsError:
    print('Невозможно создать каталог, так как он уже существует')


# Задание 3

task3_list = []
file_list = []
my_dir = 'lesson7'
folder = r'my_project'

for root, dir, files in os.walk(folder):
    for file in files:
        if '.html' in file:
            files.append(os.path.join(root, file))
for path in file_list:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
        save_path = os.path.join(folder, os.path.basename(path))
        shutil.copy(path, save_path)


# Задание 4
task4_list = []
task4_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}
for root, dir, folder in os.walk('my_project'):
    for file in folder:
        path = os.path.join(root, file)
        task4_list.append(os.stat(path).st_size)
for el in task4_list:
    if el > 100 and el < 1000:
        task4_dict[1000] += 1
    elif el > 1000 and el < 10000:
        task4_dict[10000] += 1
    elif el > 10000 and el < 100000:
        task4_dict[100000] += 1
print(task4_dict)
