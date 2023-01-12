import pygame as pg
import sys
import time
from pygame.locals import *

# очередность хода
XO = 'x'

# проверка на победителя
winner = None

# проверка на ничью
draw = None

# ширина окна
width = 400

# высота окна
height = 400

# белый цвет фона
white = (255, 255, 255)

# черный цвет линий
line_color = (0, 0, 0)

# создаем доску
board = [[None] * 3, [None] * 3, [None] * 3]

# инициализация игрового окна
pg.init()

# вручную устанавливаем кол-во кадров
fps = 30

# часы для таймингов
CLOCK = pg.time.Clock()

# устанавливаем параметры окна
screen = pg.display.set_mode((width, height + 100), 0, 32)

# заголовок для игрового окна
pg.display.set_caption("Крестики Нолики")

# загружаем картинки как питоновские обьекты
initiating_window = pg.image.load("modified_cover.png")
x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("o_modified.png")

# подгоняем размеры
initiating_window = pg.transform.scale(initiating_window,
                                       (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))


def game_initiating_window():

    screen.blit(initiating_window, (0, 0))

    # обновление экрана
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    # рисуем линии
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0),
                 (width / 3 * 2, height), 7)

    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2),
                 (width, height / 3 * 2), 7)
    draw_status()


def draw_status():
    global winner, draw
    #Тексты сообщений
    if draw == True:
        message = "Ничья !"
    elif winner == None:
        message = "ход игрока " + XO.upper()
    else:
        message = "игрок " + winner + " победил!"
    

    font = pg.font.Font(None, 30)

    # текст и его цвет
    text = font.render(message, True, (255, 255, 255))

    #надпись внизу экрана с комментарием
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()


def check_win():
    global board, winner, draw

    # проверка на победу
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2])
                and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * height / 3 - height / 6),
                         (width, (row + 1) * height / 3 - height / 6), 4)
            break

    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board[2][col])
                and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0),
                         ((col + 1) * width / 3 - width / 6, 0),
                         ((col + 1) * width / 3 - width / 6, height), 4)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0]
                                                        is not None):
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2]
                                                        is not None):
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if (all([all(row) for row in board]) and winner == None):
      draw = True
    draw_status()


def drawXO(row, col):
    global board, XO

    posx = ""
    posy = ""

    if row == 1:
        posx = 30

    if row == 2:
        posx = width / 3 + 30

    if row == 3:
        posx = width / 3 * 2 + 30

    if col == 1:
        posy = 30

    if col == 2:
        posy = height / 3 + 30

    if col == 3:
        posy = height / 3 * 2 + 30

    board[row-1][col-1] = XO  

    if (XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'

    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()


def user_click():
    #получаем координаты клика мышки
    x, y = pg.mouse.get_pos()

    #определяем колонку клика
    if (x < width / 3):
        col = 1

    elif (x < width / 3 * 2):
        col = 2

    elif (x < width):
        col = 3

    else:
        col = None

    #определяем ряд клика
    if (y < height / 3):
        row = 1

    elif (y < height / 3 * 2):
        row = 2

    elif (y < height):
        row = 3

    else:
        row = None

    #после того как получили ряд и колонку, нужно нарисовать картинка в соответсвующих местах
    if (row and col and board[row - 1][col - 1] is None):
        global XO
        drawXO(row, col)
        check_win()


def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = None
    game_initiating_window()
    winner = None
    board = [[None] * 3, [None] * 3, [None] * 3]


game_initiating_window()

while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if (winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
