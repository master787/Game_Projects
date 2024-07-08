board_size = 3

board = [1,2,3,4,5,6,7,8,9] #Поле

def draw_board(): #Вывод поля
    print("_" * 4 * board_size)
    for i in range(board_size):
        print((" " * 3 + "|")*3)
        print(board[i*3], " |", board[1 + i*3], "|", board[2 + i*3], "|")
        print(("_" * 3 + "|") * 3)
def game_step(index, current_player): #Выполнение хода
    if board[index-1] in ("X", "O"):
        return False
    board[index-1] = current_player
    return True

def Check_the_victory(): #Проверка на победителя
    win = False
    win_combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_combination:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            win = board[i[0]]

    return win
def Start_the_game(): #Начало игры
    current_player = "X"
    step = 1 #количество шагов
    draw_board()

    while step <= 9 and Check_the_victory() == False: #Запрос хода
        i = 0
        while i == 0:
            index = int(input(f"Игрок {current_player} делает ход." + " Введите номер поля (0 - выйти из игры):"))
            if index == 0: #Выход т
                break
            if 9 >= index > 0 and type(index) == int: #Проверка
                i += 1
            else:
                print("Вы ввели некорректное значение.")
        if index == 0: #Выход
            break

        if game_step(index, current_player):
            print(f"Игрок {current_player} сделал ход на поле: №{index}")
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


            draw_board()
            step += 1
        else:
            print(f"Поле №{index} уже занято!")
    if Check_the_victory() == False:
        print("Ничья!")
    else:
        print(f"Игрок {Check_the_victory()} выграл!")


print("Запуск игры ...")
print("""Добро пожаловать в игру!\nЧтобы выполнить ход введите номер поля от 1 до 9!""")
Start_the_game()
