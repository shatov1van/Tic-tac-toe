from inspect import getsource, isfunction, ismethod

from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Отрисовать поле в терминале.
    game.display()
    # Разместить на поле символ по указанным координатам - сделать ход.
    game.make_move(1, 1, 'X')
    game.make_move(1, 2, 'O')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()
    print(game) # Выводит строковое представление объекта game.

    print('----------New Board------------')
    game2 = Board()

    while True:
        try:
            row = int(input('Введите номер строки: '))
            if row < 0 or row > game.field_size:
                raise FieldIndexError # raise FieldIndexError('Свой новый текст')
            
            col = int(input('Введите номер столбца: '))
            if col < 0 or col > game.field_size:
                raise FieldIndexError
            
        except FieldIndexError:
            print(f'Значение должно быть неотрицательным и больше {game.field_size}')
            print('Введите корретные координаты')
            continue

        except ValueError:
            print('Буквы вводить нельзя. Только числа.')
            print('Пожалуйста, введите значения для строки и столбца заново.')
            continue

        else:
            break

    game2.make_move(row, col, 'X')
    game2.display()

if __name__ == "__main__":
    main()

# Интроспекция — способность программы исследовать свои собственные структуры и объекты во время выполнения.
# Основные функции и атрибуты для получения информации об объектах:
# type() — возвращает тип объекта.
# isinstance() — проверяет, принадлежит ли объект определённому классу.
# dir() — показывает все атрибуты и методы объекта, включая унаследованные.
# __class__ и __dict__ — дают информацию о классе объекта и его атрибутах и методах.
# Использование модуля inspect:
# getsource() позволяет вывести код объекта (например, функции или метода).
# isfunction() и ismethod() помогают отличать функции от методов.


# Интроспекция в программировании — способность программы во время выполнения 
# исследовать типы и свойства объектов, которые содержатся в программе. 
# Это особенно полезно в языках с динамической типизацией, таких как Python, 
# где о типах объектов ничего не известно до момента выполнения программы.

# # Как узнать тип объекта
# game = Board()
# print(type(game))
# print(type(game) is Board)
# print(type(game) == Board)
# print(type(game) == int)

# # Определить, принадлежит ли экземпляр к определённому классу, можно и через функцию isinstance()
# print(isinstance(game, Board)) # Применение isinstance() считается лучшей практикой.
# print(game.__class__)

# # Функция dir()
# print(dir(game)) # Выводит список всех атрибутов и методов объекта game.

# # Этим списком можно воспользоваться для того, чтобы узнать, 
# # есть ли у объекта нужный атрибут или метод. 
# # Для этого обычно используется оператор in, также есть hasattr.
# print('__str__' in dir(game))
# print(hasattr(game, '__str__'))

# # Словарь __dict__
# print(game.__class__.__dict__) # Выводит словарь атрибутов и методов класса Board.
# print(game.__dict__) # Содержит словарь всех атрибутов экземпляра, что позволяет просматривать и изменять их.

# # Функция inspect.getsource(object)
# print(getsource(Board)) # Выводит исходный код(именно все строки кода функции, класса и т.п.) класса Board.

# # Функции inspect.isfunction(object) и inspect.ismethod(object)
# print(isfunction(game.display)) # Проверяет, является ли объект обычной функцией.
# print(ismethod(game.display)) # Проверяет, является ли объект методом.

