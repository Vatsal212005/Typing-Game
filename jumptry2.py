import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Vatsal- Typing Game')
font = pygame.font.Font('C:\\Users\\ironm\\Desktop\\C\\jump-game\\assets\\comic.ttf', 40)

# Define the path to the font file
font_name = 'C:\\Users\\ironm\\Desktop\\C\\jump-game\\assets\\comic.ttf'

3
# Initialize variables
word_speed = 0.1
score = 0
x_cor = WIDTH // 2
y_cor = 0
displayword = ""
yourword = ""

# Load high score from file
def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Save high score to file
def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

# Load initial high score
high_score = load_high_score()

# Function to generate a new word
def new_word():
    global displayword, x_cor, y_cor, yourword
    x_cor = random.randint(300, 700)
    y_cor = 200
    yourword = ''
    with open("C:\\Users\\ironm\\Desktop\\C\\jump-game\\assets\\words.txt") as f:
        words = f.read().split(', ')
        displayword = random.choice(words)

# Function to get the difficulty speed
def get_difficulty_speed():
    if word_speed == 0.13:
        return 0.13
    elif word_speed == 0.15:
        return 0.15
    elif word_speed == 0.19:
        return 0.19

# Function to draw text on screen
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)

# Function to display game front screen
def game_front_screen(message):
    global score
    game_over_text = message
    restart_text = "Press any key to restart"
    gameDisplay.blit(background, (0, 0))
    draw_text(gameDisplay, game_over_text, 50, WIDTH / 2, HEIGHT / 3 - 20)
    draw_text(gameDisplay, "High Score:", 30, WIDTH / 2, HEIGHT / 2)
    draw_text(gameDisplay, str(high_score), 30, WIDTH / 2, HEIGHT / 2 + 30)
    draw_text(gameDisplay, restart_text, 30, WIDTH / 2, HEIGHT / 2 + 80)
    draw_text(gameDisplay, 'Score: ' + str(score), 30, WIDTH / 2, HEIGHT / 2 + 150)
    pygame.display.flip()
    wait_for_key()

# Function to wait for user input
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()
                else:
                    waiting = False

# Function to display difficulty menu
def difficulty_menu():
    global word_speed
    gameDisplay.fill((255, 255, 255))  
    draw_text(gameDisplay, "Select Difficulty:", 54, WIDTH / 2, HEIGHT / 4)
    draw_text(gameDisplay, "1. Easy", 40, WIDTH / 2, HEIGHT / 2)
    draw_text(gameDisplay, "2. Medium", 40, WIDTH / 2, HEIGHT / 2 + 50)
    draw_text(gameDisplay, "3. Hard", 40, WIDTH / 2, HEIGHT / 2 + 100)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    word_speed = 0.13
                    waiting = False
                elif event.key == pygame.K_2:
                    word_speed = 0.15
                    waiting = False
                elif event.key == pygame.K_3:
                    word_speed = 0.19
                    waiting = False

# Display difficulty menu
difficulty_menu()

# Load background image
background = pygame.image.load('C:\\Users\\ironm\\Desktop\\C\\jump-game\\assets\\background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Generate initial word
new_word()

# Main game loop
while True:
    # Check for game over condition
    if y_cor > HEIGHT - 5:
        if score > high_score:
            high_score = score
            save_high_score(high_score)
        game_front_screen("You Lost! Score: {}".format(score, high_score))
        score = 0
        word_speed = 0.1  # Reset word speed when the game restarts
        new_word()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Exit
                pygame.quit()
                sys.exit()
            elif displayword.startswith(yourword + pygame.key.name(event.key)):
                yourword += pygame.key.name(event.key)
                if displayword == yourword:
                    score += len(displayword)
                    new_word()
                    # Increase word speed, but cap at 0.7
                    word_speed = min(0.7, word_speed + 0.05)
            else:
                yourword = ''  # Reset yourword if the player types a wrong key

    # Update game state
    y_cor += word_speed

    # Draw elements on the screen
    gameDisplay.blit(background, (0, 0))

    draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
    draw_text(gameDisplay, 'Score:' + str(score), 40, WIDTH / 2, 5)
    draw_text(gameDisplay, 'High Score:' + str(high_score), 40, WIDTH / 2, 45)

    # Update display
    pygame.display.update()
