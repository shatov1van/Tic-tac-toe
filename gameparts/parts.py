# Объявить класс.
class Board:
    """Класс, который описывает игровое поле.""" # Это докстринг - строка документации, вызывающаяся при помощи __doc__ для любого объекта: функции, класса, пакета
    field_size = 3
    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        if 0 <= row < 3 and 0 <= col < 3:
            self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    # Метод для проверки заполненности поля
    def is_board_full(self):
        for i in range(self.field_size):
            # А потом по всем столбцам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True

    # Этот метод определяет победу
    def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or
                all([self.board[j][i] == player for j in range(self.field_size)])):
                return True

        return all([self.board[i][i] == player for i in range(self.field_size)]) or all([self.board[i][self.field_size - 1 - i] == player for i in range(self.field_size)])

    # Метод для печати объекта класса Board
    def __str__(self):
        return ('Объект игрового поля размером '
        f'{self.field_size}x{self.field_size}')

if __name__ == "__main__": # Без этого блока код будет выполняться при импорте модуля, везде.
    print(Board.__doc__) # Вызов докстринга
    print('Игра "Крестики-нолики"') # А с этим условным опер будет выполняться только при запуске модуля напрямую.

    