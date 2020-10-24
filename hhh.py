# Словари:

# dict_witch_pairs = {'Ключ1': 'Значение', 'Ключ2', 'Значение'}
# dict_ = {3: 1, 2, 3.4:2, 3.2}
# print(dict_)

# method fromkeys на основве списка создает новые словари
# names = {'name': 'John', 'namel': 'Tom'}
# print(names['namel'])
# print(names['name'])

# dictionary = dict.fromkeys(['key1', 'key2'])
# print(dictionary)
# dictionary2 = dict.fromkeys(['key', 'key2'], ['val', 'val2'])
# print(dictionary2)

# извлечение данных из словаря
# test = {"name": "John", 'lastname': 'Snov'}
# print(test['name'])
# print(test['lastname'])
# print(test['key'])

# [] - введите ключ {} - введите значение ключа
# some_dict = {1:5, 2:8, 3:4}
# some_dict[4] = 10 + 5
# print(some_dict)
# some_dict ['key'] ='value'
# print(some_dict)
# some_dict['key2'] = [1,2,3,4,5]
# some_dict ['key3'] = {1:1, 2:2}
# print(some_dict)
# some_dict['key3', 'key'] = {3:3, 4:4}
# print(some_dict)
# some_dict ['key3'] = 'значение'
# print(some_dict)



# method get значения ключа

# cars = {'mersedes' : '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.get('subaru'))
# print(cars['subaru'])



# method keys выводит все ключи
# cars = {'mersedes' : '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.keys())
# cars_list = cars.keys()
# print(cars_list)
# print(len(cars))
# mersedes = cars.get('mersedes')
# print(mersedes)


# method values выводит все значения
# cars = {'mersedes' : '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.values())
# print(type(cars.values()))


# method pop вырезает по ключу и возвращает значение обязательно указывать ключ
# dict_ = {'firs': 'lst', 'second': '2nd', 'third': '3rd'}
# print(dict_)
# firs = dict_.pop('firs')
# print(dict_)
# print(firs)


# method popitem вырезает последнее значение, не обязательно указывать ключ
# cars = {'mersedes' : '221', 'bmw': '750i', 'subaru': 'impreza'}
# deleted = cars.popitem()
# print(deleted)


# method update склеивает словари в один (нельзя через запятую!)
# laptops = {'lenovo': 'yoga', 'mackbook': 'pro', 'asus': 'zephyris'}
# laptops2 = {'dell': 'allienware'}
# print(laptops)
# laptops.update(laptops2)
# print(laptops)


# method setdefault сохраняет значение по ключу
# dict_= {'keyl1': 1, 'keyl2': 2, 'keyl3':3}
# new_dict = dict_.setdefault ('keyl2')
# print(new_dict)
# new = dict_['keyl2']
# print(new_dict)
# new2 = dict_.get('keyl2')
# print(new2)


# capitals = dict(Russia = 'Moskow', Kyrgyztan = 'Bischkek', USA = 'Waschington')
# print(capitals)
# capitals = dict([('Russia', 'Moskow'),('Kyrgyztan', 'Bishkek')])
# print(capitals)

# capitals = {'Russia' : 'Moskow', 'Kyrgyztan' : 'Bishkek'}
# print(capitals)



# Множество/set удаляет повторныезначения (хранит любые значения)
# set_ = [1, 2, 3, 4, 1, 2, 4, 5]
# set_ = set(set_)
# print(set_)

# set_ = {1, 2, 3, 5}
# print(set_)
# print(type(set_))
# set_.add(4)
# print(set_)
# set множества (ключи) dict - значения
# set сортирует
# add добавляет значения в множество

# method remove
# set_ = {1,2,3,1,2,3,5,5}
# print(set_)
# set_.remove(1)
# print(set_)

# method discard
# set_ = {1,2,3,1,2,3,5,5}
#  set_.discard(1)
# print(set_)

# method pop вырезает элемент
# set_ = {1,2,3,1,2,3,5,5}
# print(set_.pop())















































