import pygame

pygame.init()

win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hangman_Game.py")
fail = 0
letters = []

#load images
images = []
for i in range(8) :
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#setup game loop
FPS = 60
clock = pygame.time.Clock()
running = True

while running :
    clock.tick(FPS)
    
    win.fill((255,255,255))
    win.blit(images[fail], (25,25))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            print(pos)



pygame.quit()