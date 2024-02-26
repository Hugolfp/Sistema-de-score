import pygame
import sys
import random

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Jogo com Desenho Personalizado")
cubo_img = pygame.image.load("image.xcf")  
CUBE_WIDTH, CUBE_HEIGHT = 50, 50
cube_x = (WIDTH - CUBE_WIDTH) // 2
cube_y = HEIGHT - CUBE_HEIGHT - 50  
cube_speed = 5
score = 0
balls = []
def create_ball():
    ball_radius = 10
    ball_x = random.randint(ball_radius, WIDTH - ball_radius)
    ball_y = 0
    ball_speed = 3
    balls.append((ball_x, ball_y, ball_radius, ball_speed))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cube_x -= cube_speed
    if keys[pygame.K_RIGHT]:
        cube_x += cube_speed

   
    if cube_x < 0:
        cube_x = 0
    elif cube_x > WIDTH - CUBE_WIDTH:
        cube_x = WIDTH - CUBE_WIDTH

   
    if random.random() < 0.02:
        create_ball()

   
    for i, ball in enumerate(balls):
        ball_x, ball_y, ball_radius, ball_speed = ball
        ball_y += ball_speed
        balls[i] = (ball_x, ball_y, ball_radius, ball_speed)

        
        if (cube_x < ball_x < cube_x + CUBE_WIDTH) and (cube_y < ball_y < cube_y + CUBE_HEIGHT):
            score -= 1
            del balls[i]

       
        elif (cube_x > ball_x + ball_radius or cube_x + CUBE_WIDTH < ball_x - ball_radius) and ball_y > cube_y + CUBE_HEIGHT:
           
            score += 1
           
            del balls[i]

        
        if ball_y > HEIGHT + ball_radius:
            del balls[i]

    screen.fill(BLACK)
    screen.blit(cubo_img, (cube_x, cube_y))

    
    for ball in balls:
        ball_x, ball_y, ball_radius, _ = ball
        pygame.draw.circle(screen, RED, (ball_x, int(ball_y)), ball_radius)

    
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    
    pygame.display.flip()

    
    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()
