import pygame
pygame.init()

def drawEnemy(dict):
    win.blit(dict["img"], (dict["x"], dict["y"]))

def makeEnemy():
    enemy_img = pygame.Surface([16, 16]).convert()
    enemy_img.blit(img, (0, 0), (16, 48, 16, 16))
    e = {
        "x": 400,
        "y": 300,
        "img": pygame.transform.scale(enemy_img, (64, 64))
    }
    return e


# Create the clock object
clock = pygame.time.Clock()

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/hero/Old hero.png')
smol_img = pygame.Surface([16, 16]).convert()
smol_img.blit(img, (0, 0), (16, 0, 16, 16))
smol_img = pygame.transform.scale(smol_img, (64, 64))

# render text



x = 200
y = 200 

enemy = makeEnemy()
enemy2 = makeEnemy()


run = True
while run:
    # Limit the framerate to ~120 fps
    clock.tick(120)

    # Player stuff
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    if keys[pygame.K_RIGHT]:
        x += 3

    # Enemy stuff

    if x < enemy["x"]:
        enemy["x"] -= 1

    if x > enemy["x"]:
        enemy["x"] += 1












    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(smol_img, (x, y))

    drawEnemy(enemy)
    drawEnemy(enemy2)


    pygame.display.update()

pygame.quit()