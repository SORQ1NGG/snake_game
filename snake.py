import pygame
import time
import random

pygame.init()


def flip():
    pygame.display.flip()


width = 800
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

font = pygame.font.SysFont("None", 35)

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

rect_size = 15
snake_speed = 10

head_x = width // 2 // rect_size * rect_size
head_y = height // 2 // rect_size * rect_size


def get_random_point():
    x = random.randint(0, width - rect_size) // rect_size * rect_size
    y = random.randint(0, height - rect_size) // rect_size * rect_size
    return x, y


def show_snake(snake):
    for x in snake:
        pygame.draw.rect(display, black, [x[0], x[1], rect_size, rect_size])


def show_score(score):
    value = font.render("Очки: " + str(score), True, black)
    display.blit(value, [0, 0])


food_x, food_y = get_random_point()

snake = []
snake_length = 1

velocity_x = 0
velocity_y = 0

clock = pygame.time.Clock()

while True:

    if head_x < 0 or head_x > width - rect_size or head_y < 0 or head_y > height - rect_size:
        red = (213, 50, 80)
        message = font.render("Вы проиграли", True, red)
        display.blit(message, [width // 2, height // 2])
        flip()

        time.sleep(2)

        pygame.quit()
        quit()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocity_y = rect_size
                velocity_x = 0
            elif event.key == pygame.K_UP:
                velocity_y -= rect_size
                velocity_x = 0
            elif event.key == pygame.K_LEFT:
                velocity_y = 0
                velocity_x -= rect_size
            elif event.key == pygame.K_RIGHT:
                velocity_y = 0
                velocity_x = rect_size

    head_x += velocity_x
    head_y += velocity_y

    display.fill(white)

    pygame.draw.rect(display, red, [food_x, food_y, rect_size, rect_size])

    pygame.draw.rect(display, black, [head_x, head_y, rect_size, rect_size])

    snake.append((head_x, head_y))
    if len(snake) > snake_length:
        del snake[0]

    show_snake(snake)
    show_score(snake_length - 1)

    if head_x == food_x and head_y == food_y:
        food_x, food_y = get_random_point()
        snake_length += 1

    flip()
    clock.tick(snake_speed)
