import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen.fill(WHITE)

color = BLACK
radius = 5
drawing = False
mode = "paint"
fill = False

start_pos = None
last_pos = None

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK

            elif event.key == pygame.K_e:
                mode = "erase"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "paint"
            elif event.key == pygame.K_q:
                mode = "rect"

            elif event.key == pygame.K_f:
                fill = not fill

            elif event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                radius += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                radius -= 1

            elif event.key == pygame.K_x:
                screen.fill(WHITE)

            radius = max(1, radius)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
            canvas_copy = screen.copy()

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                x1, y1 = start_pos
                x2, y2 = event.pos

                rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                   abs(x2-x1), abs(y2-y1))

                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                x1, y1 = start_pos
                x2, y2 = event.pos

                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)

        elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos

            if mode == "paint":
                pygame.draw.line(screen, color, last_pos, (x, y), radius)
                last_pos = (x, y)

            elif mode == "erase":
                pygame.draw.circle(screen, WHITE, (x, y), radius)

            elif mode == "rect":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos

                rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                   abs(x2-x1), abs(y2-y1))

                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos

                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()