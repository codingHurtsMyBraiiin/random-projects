import pygame, random   #install pygame btw 
                        #sudo apt-get install python3-pygame (for linux)
                        #pip install pygame (for windows)

pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]
size = [400, 500]

screen =  pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Snowfall")

snowfall = []
for i in range(50):
    x = random.randrange(400)
    y = random.randrange(500)
    snowfall.append([x, y])

closed = False
while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(black)
    for i in range(len(snowfall)):
        pygame.draw.circle(screen, white, snowfall[i], 2)

        snowfall[i][1] += 1
        if snowfall[i][1] > 500:
            y = random.randrange(-50, -10)
            snowfall[i][1] = y

            x = random.randrange(0, 400)
            snowfall[i][0] = x

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
