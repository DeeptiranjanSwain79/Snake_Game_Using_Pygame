import pygame
import random

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

def Snake(screen, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])

def Text(text, color, x, y):
    scrn_text = font.render(text, True, color)
    screen.blit(scrn_text, [x, y])

def Gameloop():
    exit = False
    over = False
    snake_x = 100
    snake_y = 100
    frog_x = random.randint(15, screen_width/2)
    frog_y = random.randint(15, screen_height/2)
    velocity_x = velocity_y = 0
    velocity = 7
    score = 0
    snake_list = []
    snake_length = 1
    snake_size = frog_size = 20
    fps = 40

    while not exit:
        if over:
            screen.fill(black)
            Text("Score: " + str(score), red, 5, 5)
            Text("YOU LOST,PRESS ENTER TO CONTINUE...", red, 100, 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Gameloop()
        else:
            screen.fill((255, 255, 230))
            pygame.draw.rect(screen, green, [frog_x, frog_y, frog_size, frog_size])
            Text("Score: "+str(score), red, 5, 5)
            Snake(screen, black, snake_list, snake_size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = +velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = +velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - frog_x)<snake_size and abs(snake_y - frog_y)<snake_size:
                score += 10
                frog_x = random.randint(15, screen_width/2)
                frog_y = random.randint(15, screen_height/2)
                snake_length += 5

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                over = True
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

Gameloop()