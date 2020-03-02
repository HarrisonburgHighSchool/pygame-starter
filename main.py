import pygame
pygame.init()


# Create the clock object
clock = pygame.time.Clock()

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/gfx/Inner.png')
smol_img = pygame.Surface([16, 16]).convert()
smol_img.blit(img, (0, 0), (0, 0, 16, 16))
smol_img = pygame.transform.scale(smol_img, (64, 64))



run = True
while run:
    # Limit the framerate to ~120 fps
    clock.tick(120)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(smol_img, (0, 0))
    win.blit(smol_img, (40, 0))


    pygame.display.update()

pygame.quit()