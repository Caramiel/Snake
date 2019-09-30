import pygame
from random import *

def main():
    width, height = 500, 500
    surface = pygame.display.set_mode((width, height))

    fps = 7
    clock = pygame.time.Clock()

    gw, gh = 25, 25
    body = []

    hx = gw // 2
    hy = gh // 2.5
    body.append((hx, hy))

    while True:
        ax = randint(1, gw)
        ay = randint(1, gh)
        if not ((ax,ay) in body):
            break

    dx = width // gw
    dy = height // gh

    # L, R, U, D
    direction = "R"

    running = True
    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != "R":
                        direction = "L"
                elif event.key == pygame.K_RIGHT:
                    if direction != "L":
                        direction = "R"
                elif event.key == pygame.K_UP:
                    if direction != "D":
                        direction = "U"
                elif event.key == pygame.K_DOWN:
                    if direction != "U":
                        direction = "D"

        surface.fill((0, 0, 0))
        
        head = body[0]
        if direction == "L":
            head = (head[0] - 1, head[1])
        elif direction == "R":
            head = (head[0] + 1, head[1])
        elif direction == "U":
            head = (head[0], head[1] - 1)
        elif direction == "D":
            head = (head[0], head[1] + 1)

        if head[0] < 1 or head[0] > gw or head[1] < 1 or head[1] > gh:
            print("Game over!!")
            running = False

        if head in body:
            print("Game over!!")
            running = False

        if direction != "":
            body.insert(0, head)
            if ax == head[0] and ay == head[1]:
                 while True:
                    ax = randint(1, gw)
                    ay = randint(1, gh)
                    if not ((ax,ay) in body):
                        break
            else:
                body.pop()

        # Grid
        for x in range(0, width, dx):
            pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, height))

        for y in range(0, height, dy):
            pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))

        # Body
        for (x, y) in body:
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect((x - 1) * dx, (y - 1) * dy, dx, dy))

        # Apple
        pygame.draw.rect(surface, (0, 255, 0), pygame.Rect((ax - 1) * dx, (ay - 1) * dy, dx, dy))

        pygame.display.flip()

main()
