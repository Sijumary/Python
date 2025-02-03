import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
FPS = 60

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
BACKGROUND_COLOR = (50, 50, 50)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Set up the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5  #paddles can move, with a value of 5 units per frame or update cycle. 
PADDLE_COLOR = WHITE
#creating two paddle objects using the pygame.Rect() constructor and position them at the center of each side of the game window
paddle1 = pygame.Rect(0, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(
    WIDTH - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT
)
# Set up the ball
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
BALL_COLOR = WHITE
#creating a ball object using pygame.Rect() constructor and positioning it at the center of the game window
ball = pygame.Rect(
    WIDTH / 2 - BALL_WIDTH / 2, HEIGHT / 2 - BALL_HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT
)

#setting the initial speed of the ball in both x and y directions randomly
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
# Set up the game variables
score1 = 0
score2 = 0
game_font = pygame.font.SysFont(None, 48)
SCORE_COLOR = WHITE
POWERUP_WIDTH = 15
POWERUP_HEIGHT = 15
POWERUP_COLOR = ORANGE
powerup = pygame.Rect(WIDTH / 2 - POWERUP_WIDTH / 2, HEIGHT / 2 - POWERUP_HEIGHT / 2, POWERUP_WIDTH, POWERUP_HEIGHT)

powerup_speed_x = 2 * random.choice((1, -1))
powerup_speed_y = 2 * random.choice((1, -1))
powerup_active = False  # Initially, the power-up is not active
# Set up the game loop
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1.y > 0:
            paddle1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1.y < HEIGHT - PADDLE_HEIGHT:
            paddle1.y += PADDLE_SPEED
        if keys[pygame.K_UP] and paddle2.y > 0:
            paddle2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2.y < HEIGHT - PADDLE_HEIGHT:
            paddle2.y += PADDLE_SPEED
        # Move the ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        # Ball collision with paddles
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x *= -1

        # Ball collision with walls
        if ball.y > HEIGHT - BALL_HEIGHT or ball.y < 0:
            ball_speed_y *= -1 
        # Increase the score and reset the ball
        if ball.x < 0:
            score2 += 1
            ball.center = (WIDTH / 2, HEIGHT / 2)
            ball_speed_x *= random.choice((1, -1))
            ball_speed_y *= random.choice((1, -1))
        if ball.x > WIDTH:
            score1 += 1
            ball.center = (WIDTH / 2, HEIGHT / 2)
            ball_speed_x *= random.choice((1, -1))
            ball_speed_y *= random.choice((1, -1))
        # Power-up collision with paddles
        if powerup.colliderect(paddle1) or powerup.colliderect(paddle2):
            powerup_active = True
            powerup.x = WIDTH / 2 - POWERUP_WIDTH / 2
            powerup.y = HEIGHT / 2 - POWERUP_HEIGHT / 2

        # Power-up movement
        if powerup_active:
            powerup.x += powerup_speed_x
            powerup.y += powerup_speed_y

            if powerup.x > WIDTH - POWERUP_WIDTH or powerup.x < 0:
                powerup_speed_x *= -1
            if powerup.y > HEIGHT - POWERUP_HEIGHT or powerup.y < 0:
                powerup_speed_y *= -1
        # Draw the game elements
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, PADDLE_COLOR, paddle1)
        pygame.draw.rect(screen, PADDLE_COLOR, paddle2)
        pygame.draw.ellipse(screen, BALL_COLOR, ball)
        pygame.draw.rect(screen, POWERUP_COLOR, powerup)
        # Draw the score
        score_text = game_font.render(f"{score1} : {score2}", True, SCORE_COLOR)
        screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, 10))
        # Update the display
        pygame.display.flip()
        # Set the FPS
        clock.tick(FPS)
    # Quit the game
pygame.quit()
sys.exit()
