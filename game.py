from inspect import getsource, isfunction, ismethod

from gameparts import Board
from gameparts.exceptions import FieldIndexError
from gameparts.exceptions import CellOccupiedError

def save_result(text: str):
    # Контекстный менеджер — это конструкция(with/as), которая во время работы программы создаёт 
    # определённым образом настроенную среду («контекст»), где будет выполняться заданный код.
    # Контекстный менеджер полезен в тех случаях, когда перед выполнением 
    # некоторых операций нужно подготовиться, а после — «прибраться».
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')

def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    current_player = 'X'
    running = True
    # Отрисовать поле в терминале.
    game.display()
    
    # Тут запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError

                if game.board[row][column] != ' ':
                    raise CellOccupiedError
                
            except FieldIndexError:
                print('Значение должно быть неотрицательным и меньше 'f'{game.field_size}.')
                print('Введите значения для строки и столбца заново.')
                continue

            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue

            
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        # Теперь для установки значения на поле само значение берётся
        # из переменной current_player.
        game.make_move(row, column, current_player)
        game.display()

        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            print(result)
            save_result(result)
            running = False

        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False
        
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'

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

