from requests import get
from itertools import zip_longest
import pickle
import sys


# Задание 1

response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(response)


with open('nginx_logs.txt') as f:
    task1_list = []
    for i in f:
        value = i.split()
        remote_addr = value[0]
        request_type = value[5]
        requested_resource = value[6]
        task1_list.append((remote_addr, request_type, requested_resource))
print(task1_list)

# Задание 3



task3_dict = {}
with open('users.csv', encoding='utf-8') as u:
    with open('hobby.csv', encoding='utf-8') as h:
        u_val = 0
        h_val = 0
        for i in u:
            u_val += 1
        for i in h:
            h_val += 1
        print(u_val)
        print(h_val)
        if u_val < h_val:
            print(1)
        else:
            u.seek(0)
            h.seek(0)
            for user, hobby in zip_longest(u, h):
                task3_dict[str(user).strip()] = str(hobby).strip()

print(task3_dict)

with open('users_hobby.pickle', 'wb') as f:
    pickle.dump(task3_dict, f)

# Проверка чтения словаря
# with open('users_hobby.pickle', 'rb') as f:
#     test = pickle.load(f)
# print(test)

# Задание 6

val = sys.argv[1:]

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(val) == 0:
        print(f.read())
    elif len(val) == 1:
        for i, line in enumerate(f):
            if i + 1 >= int(sys.argv[1]):
                print(line)
    elif len(val) == 2:
        for i, line in enumerate(f):
            if int(sys.argv[1]) <= i+1 <= int(sys.argv[2]):
                print(line)
