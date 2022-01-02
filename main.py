import sys, pygame
import random

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

players = ['X', 'O']
current_player = random.randint (0, len(players)-1)
gameover = False

pygame.init ()

screen_width = 400
screen_height = 496
square_size = 133

bg_color = (18, 18, 18)
title_color = (228, 230, 235)
line_color = (58, 59, 60)
players_color = [
    (210, 4, 45),
    (135, 206, 235)
]
over_line_color = (179, 179, 179)


screen = pygame.display.set_mode ((screen_width, screen_height))
screen.fill (bg_color)


def render_text(font_type, font_size, font_color, font_text, text_rect_center):

    font = pygame.font.Font(font_type, font_size)
    text = font.render(font_text, True, font_color)
    text_rect = text.get_rect ()
    text_rect.center = text_rect_center
    screen.blit (text, text_rect)


font = 'freesansbold.ttf'
title = "TIC-TAC-TOE"


def set_prototype_screen():

    render_text(font, 28, title_color, title, (screen_width//2, (screen_height-screen_width)/2 - 15))
    pygame.draw.rect (screen, line_color, pygame.Rect(0, (screen_height-screen_width)//2 + 15, screen_width, screen_width), 3)
    for i in range (2):
    	pygame.draw.line (screen, line_color, (square_size*(i+1),  (screen_height-screen_width)//2 + 15), (square_size*(i+1), (screen_height-screen_width)//2 +  15 + screen_width), 2)
    for i in range (2):
    	pygame.draw.line (screen, line_color, (0, (screen_height-screen_width)//2 + 15+ square_size*(i+1)), (screen_width, (screen_height-screen_width)//2 + 15 + square_size*(i+1)), 2)


def available_square (row, col):
    return board[row][col] == ' '


def clicked_square (mousex, mousey):
    return (int (mousex//square_size), int ((mousey-((screen_height-screen_width)/2 + 15))//square_size))


def mark_square (i, j):
    board[i][j] = players[current_player]
    render_text (font, 28, players_color[current_player], board[i][j], ((square_size//2)+square_size*i, (square_size//2)+(screen_height-screen_width)/2 + 15 + square_size*j))



def game_over ():

    for i in range (0, 3):
        if (board[i][0] == board[i][1] == board[i][2] == players[current_player]):
            draw_line(i, 0, i, 2)
            win_screen (players[current_player] + " WINS!")
            # print ()
            return True

    for i in range (0, 3):
        if (board[0][i] == board[1][i] == board[2][i] == players[current_player]):
            draw_line(0, i, 2, i)
            win_screen (players[current_player] + " WINS!")
            # print (players[current_player] + " WINS!")
            return True

    if (board[0][0] == board[1][1] == board[2][2] == players[current_player]):
        draw_line(0, 0, 2, 2)
        win_screen (players[current_player] + " WINS!")
        # print (players[current_player] + " WINS!")
        return True

    if (board[0][2] == board[1][1] == board[2][0] == players[current_player]):
        draw_line(0, 2, 2, 0)
        win_screen (players[current_player] + " WINS!")
        # print (players[current_player] + " WINS!")
        return True
    
    return False


def draw_line (startx, starty, endx, endy):
     pygame.draw.line (screen, over_line_color, 
     ((startx*square_size)+(square_size//2), (starty*square_size)+(square_size//2)+(screen_height-screen_width)/2 + 15), 
     ((endx*square_size)+(square_size//2), (endy*square_size)+(square_size//2)+(screen_height-screen_width)/2 + 15), 2)


def win_screen (text):
    screen.fill (bg_color, (0, 0, screen_width, (screen_height-screen_width)/2 + 15))
    render_text(font, 28, players_color[current_player], text, (screen_width//2, (screen_height-screen_width)/2 - 15))


def restart ():
    screen.fill (bg_color)
    set_prototype_screen()
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '


set_prototype_screen()

while True:

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()
        
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            
            clicked_row, clicked_col = clicked_square (event.pos[0], event.pos[1])
            if (available_square (clicked_row, clicked_col)):
                mark_square (clicked_row, clicked_col)
                if game_over():
                    gameover = True
                current_player = (current_player+1) % len (players)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameover = False
                current_player = random.randint (0, len(players)-1)
                restart()

    pygame.display.update()