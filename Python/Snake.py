import pygame
import pygame.freetype
import random
import time

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
gray = (68, 68, 68)
red = (255, 0, 0)
green = (0, 255, 0)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
font_style = pygame.freetype.Font(None, 44)


def food_x():
    while True:
        result = round(random.randrange(20, dis_width - 20) / 10.0) * 10.0
        if result not in [200, 300, 600]:
            return result


def our_snake(moves, li):
    for x in li:
        pygame.draw.rect(dis, white, [x[0], x[1], moves, moves])


def message(text, color, px, py):
    text_surface, rect = font_style.render(text, color)
    dis.blit(text_surface, (px, py))
    pygame.display.flip()


def game():
    game_time = 15
    game_over = False
    game_close = False
    move = 10
    snake_speed = 10
    x1 = 300
    y1 = 300
    x1_change = 0
    y1_change = 0
    count_snake = []
    length_snake = 1
    fx = food_x()
    fy = round(random.randrange(20, dis_height - 20) / 10.0) * 10.0

    while not game_over:
        if game_time > 170:
            if snake_speed < 15:
                snake_speed *= 2
        while game_close:
            dis.fill(black)
            message('You lose, try again? Y/N!', red, 150, 200)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -move
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = move
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -move
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = move
                    x1_change = 0

        if x1 > 10 and x1_change < 0:
            x1 += x1_change
        elif x1 < 780 and x1_change > 0:
            x1 += x1_change
        if x1 == 10 and x1_change < 0 or x1 == 780 and x1_change > 0:
            game_close = True
        elif x1 == 210 and y1 in [i for i in range(10, 301)] and x1_change < 0:
            game_close = True
        elif x1 == 200 and y1 in [i for i in range(10, 311)] and y1_change < 0:
            game_close = True
        elif x1 == 190 and y1 in [i for i in range(10, 301)] and x1_change > 0:
            game_close = True
        elif x1 == 590 and y1 in [i for i in range(300, 581)] and x1_change > 0:
            game_close = True
        elif x1 == 600 and y1 in [i for i in range(290, 581)] and y1_change > 0:
            game_close = True
        elif x1 == 610 and y1 in [i for i in range(300, 581)] and x1_change < 0:
            game_close = True

        if y1 > 10 and y1_change < 0:
            y1 += y1_change
        elif y1 < 580 and y1_change > 0:
            y1 += y1_change
        if y1 == 10 and y1_change < 0 or y1 == 580 and y1_change > 0:
            game_close = True

        dis.fill(black)
        pygame.draw.rect(dis, green, [fx, fy, move, move])
        snake_head = [x1, y1]
        count_snake.append(snake_head)
        if len(count_snake) > length_snake:
            del count_snake[0]
        for x in count_snake[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(move, count_snake)
        for i in range(1, dis_width + 1):
            pygame.draw.rect(dis, gray, [i, 0, move, move])
            pygame.draw.rect(dis, gray, [i, 590, move, move])
        for i in range(1, dis_height + 1):
            pygame.draw.rect(dis, gray, [0, i, move, move])
            pygame.draw.rect(dis, gray, [790, i, move, move])
        for i in range(1, 301):
            pygame.draw.rect(dis, gray, [200, i, move, move])
        for i in range(1, 801):
            if i > 299:
                pygame.draw.rect(dis, gray, [600, i, move, move])
        pygame.display.update()
        if x1 == fx and y1 == fy:
            fx = food_x()
            fy = round(random.randrange(20, dis_height - 20) / 10.0) * 10.0
            length_snake += 1
        if game_time != 180:
            game_time += 1
        clock.tick(snake_speed)
    message("Game over!", red, 250, 200)
    time.sleep(2)
    pygame.quit()
    quit()


game()
