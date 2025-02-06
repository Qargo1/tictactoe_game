from random import randint

def define_player():
    player_1 = input('Игрок 1, введи своё имя: ').strip().capitalize()
    player_2 = input('Игрок 2, введи своё имя: ').strip().capitalize()
    print(f'Имя игрока 1: {player_1}, Имя игрока 2: {player_2}')
    return player_1, player_2

def define_mark(player_1, player_2):
    while True:
        player_1_mark = input(f'{player_1}, выбери свой символ (X или O): ').upper()
        if player_1_mark in ('X', 'O'):
            player_2_mark = 'O' if player_1_mark == 'X' else 'X'
            game_settings = {player_1: player_1_mark, player_2: player_2_mark}
            print(f'{player_1} играет за {player_1_mark}, {player_2} играет за {player_2_mark}.')
            return game_settings
        else:
            print('Неверный символ. Пожалуйста, выбери X или O.')

def define_first_player(game_settings):
    print('Определяем, кто ходит первым...')
    players = list(game_settings.keys())
    first_player = players[randint(0, 1)]
    print(f'Первым ходит {first_player}!')
    return first_player

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def get_valid_move(board, player):
    while True:
        try:
            row = int(input(f'{player}, выбери строку (0, 1, 2): '))
            col = int(input(f'{player}, выбери столбец (0, 1, 2): '))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print('Недопустимый ход. Попробуй снова.')
        except ValueError:
            print('Неверный ввод. Введи число.')

def check_winner(board, mark):
    # Проверка строк
    for row in board:
        if row.count(mark) == 3:
            return True

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tictactoe():
    print('Добро пожаловать в игру Крестики-Нолики!')
    
    # Определение игроков и их символов
    player_1, player_2 = define_player()
    game_settings = define_mark(player_1, player_2)
    
    # Определение первого игрока
    first_player = define_first_player(game_settings)
    current_player = first_player
    
    # Создание игрового поля
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Основной игровой цикл
    while True:
        print_board(board)
        mark = game_settings[current_player]
        print(f'Ход игрока {current_player} ({mark})')
        
        # Получение допустимого хода
        row, col = get_valid_move(board, current_player)
        board[row][col] = mark
        
        # Проверка на победу
        if check_winner(board, mark):
            print_board(board)
            print(f'Победил игрок {current_player}!')
            break
        
        # Проверка на ничью
        if is_board_full(board):
            print_board(board)
            print('Ничья!')
            break
        
        # Переключение на другого игрока
        current_player = player_2 if current_player == player_1 else player_1

# Запуск игры
tictactoe()