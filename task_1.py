"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
1. Программа должна выводить данные 
2. Программа должна сохранять данные в текстовом файле 
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
4. Использование функций. 
Ваша программа не должна быть линейной
"""
from csv import DictReader, DictWriter
from os.path import exists
file_name = 'phone.csv'
file_2 = 'copy_phone.csv'

def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер')
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)
    
def write_new_file(file_2, lst):
    res = read_file(file_name)
    res.append(obj)
    with open(file_2, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'имя': lst[0], 'фамилия': lst[1], 'телефон': lst[2]}
    res.append(obj)
    standart_write(file_name, res)

def standart_write(file_name, lst):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(lst)

def copy_row(file_name, file_2):
    res = read_file(file_name)
    flag = False
    while not flag:
        try:
            number_row = int(input('Введите номер строки: '))
            if number_row > len(res):
                print(f'Номер строки не должен превышать {len(res)}')
            else:
                flag = True
        except ValueError:
                print('Вы ввели не число')
    lst_row_copy = []
    for row in range(len(res)):
        if row == number_row - 1:
            lst_row_copy.append(res[row])
    standart_write(file_2, lst_row_copy)
        
        
def row_search(file_name):
    last_name = input('Введите фамилию: ')
    res = read_file(file_name)
    for elem in res:
        if elem['фамилия'] == last_name:
            print(elem)
            break
        else:
            print('Такой фамилии нет')
            

def main():
    while True:
        command = input("Введите комманду: ")
        if command == 'q':
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_2):
                create_file(file_2)
            copy_row(file_name, file_2)
        elif command == 'f':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            row_search(file_name)


main()



            


        


    


        
