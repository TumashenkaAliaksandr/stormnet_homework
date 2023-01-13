
class DataBase:
    """Объявите класс с именем DataBase, который бы хранил в себе следующую информацию
    Имена переменных (атрибутов класса) используйте pk, title, author, views и comments"""
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12

# class DataBase:
#     def __init__(self, pk, title, author, views, comments):
#         self.pk = 1
#         self.title = "Классы и объекты"
#         self.author = "Сергей Балакирев"
#         self.views = 14356
#         self.comments = 12

#------------------------------------

class Goods:
    """Объявите класс с именем Goods и пропишите в нем следующие атрибуты (переменные)
    title, weight, tp, price
    Затем, после объявления класса, измените его атрибут price на значение 2048 и добавьте еще один атрибут"""

    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100

# ------------------------------------
class Car:
    """Объявите пустой класс с именем Car. С помощью функции setattr()
    добавьте в этот класс атрибуты:
    model, color, number
    Выведите на экран значение атрибута color, используя словарь __dict__ класса Car."""
    pass


setattr(Car, "model" , "Тойота")
setattr(Car, "color", "Розовый")
setattr(Car, "number", "П111УУ77")
print(Car.__dict__['color'])

# ------------------------------------
class Notes:

    """Объявите класс с именем Notes и определите в нем следующие атрибуты:
    uid, title, author, pages
    Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author.
    """

    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, 'author'))

# class Notes:
#     pass
#
# dct = {'uid': 1005435,
#        'title': "Шутка",
#        'author': "И.С. Бах",
#        'pages': 2}
#
# [setattr(Notes, k, v) for k, v in dct.items()]
# print(getattr(Notes, 'author'))

# ----------------------------------------

class Dictionary:
    """Объявите класс с именем Dictionary и определите в нем следующие атрибуты:
    rus, eng
    Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута rus_word.
    Если такого атрибута в классе нет, то функция getattr() должна возвращать булево значение False."""

    pass

dct = {'rus': "Питон",
       'eng': "Python"}

[setattr(Notes, s, l) for s, l in dct.items()]
print(getattr(Dictionary, 'rus_word', False))


# class Dictionary:
#     rus = "Питон"
#     eng = "Python"
#
#
# print(getattr(Dictionary, 'rus_word', False))


# -----------------------------------------------
class TravelBlog:

    """Объявите класс с именем TravelBlog и объявите в нем атрибут:
    total_blogs: 0
    Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:
    name: 'Франция', days: 6
    Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
    Создайте еще один экземпляр класса TravelBlog с именем tb2,
    сформируйте в нем два локальных свойства:
    name: 'Италия', days: 5
    Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.
    """
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = 'Франция'
tb1.days = 6
TravelBlog.total_blogs += 1


tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
TravelBlog.total_blogs += 1

# -----------------------------------------

class Figure:

    """Объявите класс с именем Figure и двумя атрибутами:
    type_fig: 'ellipse'
    color: 'red'
    Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:
    start_pt: (10, 5)
    end_pt: (100, 20)
    color: 'blue'
    Удалите из экземпляра класса свойство color и выведите на экран список всех локальных свойств (без значений)
    объекта fig1 в одну строчку через пробел в порядке, указанном в задании."""

    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
delattr(fig1, 'color')
print(fig1.__dict__)

# -------------------------------------

# параметр - self -

class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')

media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")
media1.play()
media2.play()

# -------------------------------------------

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print(" ".join(map(str, filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1], self.data))))

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

# -------------------------------------------

import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False

        for i, key in enumerate(fields):
            setattr(self, key, lst_values[i])

        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()


# -------------------------------------
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')


    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))

    def select(self, a, b):
        return self.lst_data[a: b+1]

data = DataBase()
data.insert(lst_in)
print(data.lst_data)

# ---------------------------------------------

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        return self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "автомобиль")
tr.add("car", "машина")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")
print(*tr.translate("go"))