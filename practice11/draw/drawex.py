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
            # Выбор цвета
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK

            # Выбор режима рисования
            elif event.key == pygame.K_e:
                mode = "erase"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "paint"
            elif event.key == pygame.K_q:
                mode = "rect"

            # Задание 1: квадрат
            elif event.key == pygame.K_s:
                mode = "square"

            # Задание 2: прямоугольный треугольник
            elif event.key == pygame.K_t:
                mode = "triangle_right"

            # Задание 3: равносторонний треугольник
            elif event.key == pygame.K_y:
                mode = "triangle_equil"

            # Задание 4: ромб
            elif event.key == pygame.K_d:
                mode = "rhombus"

            # Заливка вкл/выкл
            elif event.key == pygame.K_f:
                fill = not fill

            # Размер кисти
            elif event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                radius += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                radius -= 1

            # Очистить экран
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
                rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                x1, y1 = start_pos
                x2, y2 = event.pos
                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)

            # Задание 1: квадрат — все стороны равные
            elif mode == "square":
                x1, y1 = start_pos
                x2, y2 = event.pos
                side = min(abs(x2-x1), abs(y2-y1))
                rect = pygame.Rect(x1, y1, side, side)
                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            # Задание 2: прямоугольный треугольник — прямой угол в start_pos
            elif mode == "triangle_right":
                x1, y1 = start_pos
                x2, y2 = event.pos
                points = [(x1, y1), (x2, y1), (x1, y2)]
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

            # Задание 3: равносторонний треугольник
            elif mode == "triangle_equil":
                x1, y1 = start_pos
                x2, y2 = event.pos
                base = abs(x2 - x1)
                h = int(base * (3**0.5) / 2)  # высота = сторона * √3/2
                points = [(x1, y1 + h), (x2, y1 + h), ((x1+x2)//2, y1)]
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

            # Задание 4: ромб — 4 точки по центрам сторон прямоугольника
            elif mode == "rhombus":
                x1, y1 = start_pos
                x2, y2 = event.pos
                cx, cy = (x1+x2)//2, (y1+y2)//2
                points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

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
                rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)

            # Превью квадрата при перетаскивании
            elif mode == "square":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                side = min(abs(x2-x1), abs(y2-y1))
                rect = pygame.Rect(x1, y1, side, side)
                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            # Превью прямоугольного треугольника при перетаскивании
            elif mode == "triangle_right":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                points = [(x1, y1), (x2, y1), (x1, y2)]
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

            # Превью равностороннего треугольника при перетаскивании
            elif mode == "triangle_equil":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                base = abs(x2 - x1)
                h = int(base * (3**0.5) / 2)
                points = [(x1, y1 + h), (x2, y1 + h), ((x1+x2)//2, y1)]
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

            # Превью ромба при перетаскивании
            elif mode == "rhombus":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                cx, cy = (x1+x2)//2, (y1+y2)//2
                points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()