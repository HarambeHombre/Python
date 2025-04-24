import random
import pygame

pygame.init()
clock = pygame.time.Clock()

score = 0
lives = 3
game_over = False
won = False

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Block Breaker')

font = pygame.font.Font(None, 36)

BALL_COLOR = 'white'
BALL_SIZE = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 7 * random.choice((1, -1))
ball_dy = -7

BRICK_COLOR = 'white'
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICK_ROWS = 5
BRICK_COLS = WIDTH // BRICK_WIDTH
bricks = []

PADDLE_WIDTH = 200
PADDLE_HEIGHT = 20
PADDLE_COLOR = 'white'
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - 40

for row in range(5):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and (game_over or won):
            if event.key == pygame.K_SPACE:
                score = 0
                lives = 3
                game_over = False
                won = False
                bricks.clear()
                for row in range(BRICK_ROWS):
                    for col in range(BRICK_COLS):
                        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50,
                                          BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
                        bricks.append(brick)
                ball_x = WIDTH // 2
                ball_y = HEIGHT // 2
                ball_dx = 7 * random.choice((1, -1))
                ball_dy = -7

    if not game_over and not won:
        paddle_x = pygame.mouse.get_pos()[0] - PADDLE_WIDTH // 2
        paddle_x = max(0, min(paddle_x, WIDTH - PADDLE_WIDTH))

        ball_x += ball_dx
        ball_y += ball_dy

        if ball_x <= 0 or ball_x >= WIDTH - BALL_SIZE:
            ball_dx *= -1

        if ball_y <= 0:
            ball_dy *= -1

        if ball_y >= HEIGHT:
            lives -= 1
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_dx = 7 * random.choice((1, -1))
            ball_dy = -7
            if lives == 0:
                game_over = True

        paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        if paddle_rect.collidepoint(ball_x, ball_y) and ball_dy > 0:
            ball_dy *= -1

        for brick in bricks[:]:
            if brick.collidepoint(ball_x, ball_y):
                bricks.remove(brick)
                ball_dy *= -1
                score += 10
                break

        if len(bricks) <= 30:
            PADDLE_WIDTH = 100
            PADDLE_COLOR = 'orange'
            BRICK_COLOR = 'red'
            BALL_COLOR = 'orange'

        if len(bricks) <= 15:
            PADDLE_WIDTH = 75
            PADDLE_COLOR = random.choice(('blue', 'white', 'green', 'purple', 'orange', 'brown', 'gray'))
            BRICK_COLOR = random.choice(('blue', 'white', 'green', 'purple', 'orange', 'brown', 'gray'))
            BALL_COLOR = random.choice(('blue', 'white', 'green', 'purple', 'orange', 'brown', 'gray'))

    screen.fill('black')

    paddle = pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_SIZE)

    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (WIDTH // 2 - 385, HEIGHT // 2 - 285))

    lives_text = font.render(f'Lives: {lives}', True, 'white')
    screen.blit(lives_text, (WIDTH // 2 + 300, HEIGHT // 2 - 285))

    if not bricks:
        won = True

    if won:
        text = font.render('You won! Press space to start a new game', True, 'white')
        screen.blit(text, (WIDTH // 2 - 250, HEIGHT // 2 + 20))

    if game_over:
        text = font.render('Game Over! Press space to start a new game', True, 'white')
        screen.blit(text, (WIDTH // 2 - 250, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()