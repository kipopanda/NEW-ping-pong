import pygame
import random

# initializing pygame
pygame.init()

# creating the window
window = pygame.display.set_mode((800, 600))

# Background Music
pygame.mixer.music.load("pingiu/bg.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Creating logo
logo = pygame.transform.scale(pygame.image.load("pingiu/ping pong logo.png"), (64, 64))
pygame.display.set_icon(logo)

# Placing Caption
pygame.display.set_caption("Ping Pong")

# Background image
background = pygame.image.load("pingiu/background.jpg")
background = pygame.transform.scale(background, (800, 600))

# Player A
player_a_img = pygame.transform.scale(pygame.image.load("pingiu/bar.png"), (32, 128))
player_a_x_cor = 0
player_a_y_cor = 234
player_a_y_cor_change = 0
player_a_score = 0

# Player B
player_b_img = pygame.transform.scale(pygame.image.load("pingiu/bar.png"), (32, 128))
player_b_x_cor = 768
player_b_y_cor = 234
player_b_y_cor_change = 0
player_b_score = 0

# Ball
ball_img = pygame.transform.scale(pygame.image.load("pingiu/Ball.png"), (50, 50))
ball_x_cor = 350
ball_y_cor = 250
ball_x_cor_change = random.choice((1.5, -1.5, 1.4, -1.4))
ball_y_cor_change = random.choice((1.5, -1.5, 1.4, -1.4))


# Function to Show the score
def show_score():
    global player_a_score, player_b_score
    window.blit(pygame.font.Font("freesansbold.ttf", 40).render(f"Игрок A : {player_a_score}", True, (255, 166, 255)),
                (10, 10))
    window.blit(pygame.font.Font("freesansbold.ttf", 40).render(f"Игрок B: {player_b_score}", True, (255, 166, 255)),
                (580, 10))
    if player_a_score>=5 or player_b_score>=5:
        finish==True

# Game Main Loop
running = True
finish=False
while running:
    # Backgrounds
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))

    # Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_b_y_cor_change += -0.5
            if event.key == pygame.K_DOWN:
                player_b_y_cor_change += 0.5
            if event.key == pygame.K_w:
                player_a_y_cor_change += -0.5
            if event.key == pygame.K_s:
                player_a_y_cor_change += 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_b_y_cor_change += 0.5
            if event.key == pygame.K_DOWN:
                player_b_y_cor_change += -0.5
            if event.key == pygame.K_w:
                player_a_y_cor_change += 0.5
            if event.key == pygame.K_s:
                player_a_y_cor_change += -0.5
    if finish!=True:
        # Displaying Player A
        window.blit(player_a_img, (player_a_x_cor, player_a_y_cor))

        # Adding movement to player A
        player_a_y_cor += player_a_y_cor_change

        # Applying border for player A
        if player_a_y_cor <= 0:
            player_a_y_cor = 0
        elif player_a_y_cor + 128 >= 600:
            player_a_y_cor = 600 - 128

        # Displaying player B
        window.blit(player_b_img, (player_b_x_cor, player_b_y_cor))

        # Adding movement to player B
        player_b_y_cor += player_b_y_cor_change

        # Applying border for player B
        if player_b_y_cor <= 0:
            player_b_y_cor = 0
        elif player_b_y_cor + 128 >= 600:
            player_b_y_cor = 600 - 128

        # Displaying Ball
        window.blit(ball_img, (ball_x_cor, ball_y_cor))

        # Adding movement to Ball
        ball_x_cor += ball_x_cor_change
        ball_y_cor += ball_y_cor_change

        # Applying border to ball
        if ball_y_cor <= -5:
            ball_y_cor = -5
            ball_y_cor_change *= -1
        

        elif ball_y_cor >= 555:
            ball_y_cor = 555
            ball_y_cor_change *= -1
        

        # Ball hits Player
        if (0 <= ball_x_cor <= 32) and (ball_y_cor + 45 >= player_a_y_cor and ball_y_cor - 5 <= player_a_y_cor + 128):
            ball_x_cor = 33
            ball_x_cor_change *= -1
            

        elif (768 <= ball_x_cor + 50 <= 800) and (ball_y_cor + 45 >= player_b_y_cor and ball_y_cor - 5 <= player_b_y_cor + 128):
            ball_x_cor = 717
            ball_x_cor_change *= -1


        # Ball hits wall to over game
        # When player missed Ball
        if ball_x_cor < 0:
            player_b_score += 1
            ball_x_cor = 350
            ball_y_cor = 250
            ball_x_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
            ball_y_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
        

        elif ball_x_cor > 750:
            player_a_score += 1
            ball_x_cor = 350
            ball_y_cor = 250
            ball_x_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
            ball_y_cor_change = random.choice((0.3, -0.3, 0.4, -0.4))
            

        # Displaying Score
        show_score()
        
        # To update always
        pygame.display.update()

    elif finish==True:
        ball_x_cor_change=0
        ball_y_cor_change=0
        player_a_y_cor_change=0
        player_b_y_cor_change=0
        if player_a_score>player_b_score:
             window.blit(pygame.font.Font("freesansbold.ttf", 70).render(f"Игрок А победил", True, (255, 166, 255)),
                (0, 0))
        elif player_b_score>player_a_score:
             window.blit(pygame.font.Font("freesansbold.ttf", 70).render(f"Игрок B победил", True, (255, 166, 255)),
                (0, 0))