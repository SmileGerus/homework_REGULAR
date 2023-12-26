from collections import OrderedDict
from pprint import pprint
import re, csv


# 1. Выполните пункты 1-3 задания.
def current_name() -> str:
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    for cou, contact in enumerate(contacts_list):
        name = " ".join(contact[:3])
        name = name.split(" ")
        contacts_list[cou][0], contacts_list[cou][1], contacts_list[cou][2] = name[0], name[1], name[2]

    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


def current_phone():
    with open('phonebook.csv', encoding='utf-8') as file:
        r_file = file.read()
    pattern = re.compile(
        r'(\+7|8)?[\(\s]*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d+)[\s\(]*(доб.|доб.)*\s*(\d+)*\)*')
    result = pattern.sub(r'+7(\2)\3-\4-\5 \6\7', r_file)
    with open('phonebook.csv', 'w', encoding='utf-8') as file:
        file.write(result)
    return 'Done'


def unite_list():
    new_contact_list = {}
    with open("phonebook.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    for c in contacts_list:
        name = ' '.join(c[:3])
        new_contact_list[name] = c[3:]


def remove_duplicates():
    with open("phonebook.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    k = 0
    while k < len(contacts_list) - 1:
        for list1, list2 in zip(contacts_list[k], contacts_list[k + 1]):
            if list1 == list2:
                new_list = list(OrderedDict.fromkeys(contacts_list[k] + contacts_list[k + 1]))
                contacts_list.remove(contacts_list[k + 1])
                contacts_list.remove(contacts_list[k])
                contacts_list.append(new_list)
            break
        k += 1

    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

current_name()
current_phone()
remove_duplicates()







