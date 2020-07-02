'''
Домашнее задание
Для следующих простых задач нужно привести 2-3 способа решения на python, сравнить между собой эти способы по затрачиваемым времени и памяти и объяснить с чем это может быть связано.
1. Чтение/запись в словарь. При попытке чтения несуществующего ключа возвращается None.
2. К каждому элементу списка применить какуе-либо преобразование (например, для числового списка - возвести в кавдрат, для строкового - привести к верхнему регистру, отфильтровать определенные символы, и т.д.).
3. Отсортировать список.
4. Распаковать вложенный список.
'''

import timeit

def create_dict_1(n):
    x = dict()
    for i in range(n):
        x[i] = i * 100 + i
    return x


def create_dict_2(n):
    x = list()
    for i in range(n):
        t = (i, i * 100 + i)
        x.append(t)
    return dict(x)

def read_dict_1(x: dict):
    for i in x.keys():
        a = x[i]


def read_dict_2(x: dict):
    for i in x.keys():
        a = x.get(i)


#create_dict_1(1000)
#create_dict_2(1000)

def create_dict_time():
    '''Compute create_dict_1'''
    SETUP_CODE = 'from __main__ import create_dict_1'

    TEST_CODE = 'create_dict_1(1000)'

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    print('Creating simple dict  time: {}'.format(min(times)))

def create_dict_from_tuple_time():
    '''Compute create_dict_2'''
    SETUP_CODE = 'from __main__ import create_dict_2'

    TEST_CODE = 'create_dict_2(1000)'

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    print('Creating  dict  from tuple time: {}'.format(min(times)))



def read_dict_time():
    '''Compute reading from dict'''
    SETUP_CODE = ''' 
from __main__ import create_dict_1, read_dict_1 
'''

    TEST_CODE = ''' 
mydict = create_dict_1(1000)
read_dict_1(mydict)
'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('read dict time: {}'.format(min(times)))


def read_dict_with_get_time():
    '''Compute readinf dict'''
    SETUP_CODE = ''' 
from __main__ import create_dict_1, read_dict_2 
'''

    TEST_CODE = ''' 
mydict = create_dict_1(1000)
read_dict_2(mydict) 
	'''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # priniting minimum exec. time
    print('Read dict with get  time: {}'.format(min(times)))


if __name__ == "__main__":
    create_dict_time()
    create_dict_from_tuple_time()

    read_dict_time()
    read_dict_with_get_time()


