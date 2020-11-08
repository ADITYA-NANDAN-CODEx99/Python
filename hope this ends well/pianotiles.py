import pygame, random

pygame.init()

WW, WH = 400, 600
WINDOW = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Piano Tiles')
clock = pygame.time.Clock()


def new_tiles_1b(t_template):
    empty = random.choice([0, 1, 2, 3, 4])
    t_list = []
    for i, n in zip(range(0, WW+1, WW//5), range(5)):
        if n != empty:
            t = t_template.copy()
            t.x = i + 7.5
            t_list.append(t)
    return t_list

def new_tiles_4b(t_template):
    empty = random.choice([0, 1, 2, 3])
    t_list = []
    for i, n in zip(range(0, WW+1, WW//4), range(4)):
        if n == empty:
            t = t_template.copy()
            t.x = i + 7.5
            t_list.append(t)
    return t_list

def main():
    # some main vars
    tw, th = WW/6, 100
    vy = 5
    tile = pygame.Rect(0, -th, tw, th)
    
    tiles = new_tiles_4b(tile)

    running = True
    while running:
        clock.tick(60)

        WINDOW.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        for t in tiles:
            pygame.draw.rect(WINDOW, (255, 255, 255), t)

            t.y += vy

            if t.top > WH:
                tiles = new_tiles_4b(tile)
                if vy < 10:
                    vy += 1
                break

        pygame.display.update()

main() # -_-