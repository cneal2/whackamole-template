import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_x_pos = 0
        mole_y_pos = 0
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mole_x_pos //= 32
                    mole_y_pos //= 32
                    radical = list(event.pos)
                    x = radical[0] // 32
                    y = radical[1] // 32

                    if (x == mole_x_pos) and (y == mole_y_pos):
                       # print(mole_x_pos,mole_y_pos)
                        mole_x_pos = random.randrange(0,21) * 32
                        mole_y_pos = random.randrange(0,17) * 32
                        #print(mole_x_pos, mole_y_pos)
                    else:
                        mole_x_pos *= 32
                        mole_y_pos *= 32

            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32, 512))
            for i in range(16):
                pygame.draw.line(screen, (0, 0, 0), (0, i * 32),(640, i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x_pos, mole_y_pos)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
