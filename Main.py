import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("10 Lab")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

bird = pygame.image.load("bird1.png").convert_alpha()

jumpbirdright = [pygame.image.load('bird1.png').convert_alpha(), pygame.image.load('bird2.png').convert_alpha(), pygame.image.load('bird3.png').convert_alpha(), pygame.image.load('bird4.png').convert_alpha(), pygame.image.load('bird5.png').convert_alpha(), pygame.image.load('bird6.png').convert_alpha(),]

jumpbirdleft = [pygame.image.load('bird7.png').convert_alpha(), pygame.image.load('bird8.png').convert_alpha(), pygame.image.load('bird9.png').convert_alpha(), pygame.image.load('bird10.png').convert_alpha(), pygame.image.load('bird11.png').convert_alpha(), pygame.image.load('bird12.png').convert_alpha(),]

background = pygame.image.load('Star.png').convert_alpha()

gravity = 1

change = 3

xbird = 100

ybird = 200

jump = 0

wcount = 1

r = 1

l = 0

scorecount = 0

def pipe():
    pygame.draw.rect(screen,GREEN,[420,y - 1200,80,1000])
    pygame.draw.rect(screen,GREEN,[420,y + 0,80,1000])

font = pygame.font.SysFont('Calibri', 25, True, False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if l == 1:
                    jump = 1

                if r == 1:
                    jump = 2

                for i in range(600):
                    ybird = ybird - 0.1
                gravity = 1

    # --- Game logic should go here

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    pygame.mouse.set_visible(False)

    if ybird > 715:
        done = True

    if ybird <= 0:
        ybird = 5

    if xbird >= 950:
        change = -3
        bird = pygame.transform.flip(bird,True,False)
        r = 0
        l = 1
        scorecount = scorecount + 1

    if xbird <= 0:
        change = 3
        bird = pygame.transform.flip(bird,True,False)
        l = 0
        r = 1
        scorecount = scorecount + 1

    if xbird >= 330 and xbird <= 500 and ybird >= (y-1200) and ybird <= (y-1200+1000):
        done = True

    if xbird >= 330 and xbird <= 500 and ybird >= y and ybird <= (y+1000):
        done = True

    # --- Drawing code should go here

    screen.blit(background,[0,0])

    pipe()

    screen.blit(bird,[xbird, ybird])

    gravity = gravity + 0.1

    ybird = ybird + gravity

    xbird = xbird + change

    text = font.render("Score: " + str(scorecount),True,BLACK)

    screen.blit(text,[20, 20])

    if jump == 1:

        screen.blit(jumpbirdleft[wcount],[xbird,ybird])

        wcount = wcount + 1

        if wcount > 5 :
            wcount = 1
            jump = 0

    if jump == 2:

        screen.blit(jumpbirdright [wcount],[xbird,ybird])

        wcount = wcount + 1

        if wcount > 5 :
            wcount = 1
            jump = 0

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(90)

# Close the window and quit.
pygame.quit()
