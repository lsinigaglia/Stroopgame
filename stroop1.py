import pygame
import random
import time

pygame.init()

def display_feedback_rect(color):
    feedback_rect = pygame.Rect(word_text_rect.left, word_text_rect.bottom + 10, word_text_rect.width, 10)
    pygame.draw.rect(window, color, feedback_rect)
    pygame.display.flip()
    time.sleep(0.5)
    pygame.draw.rect(window, (0, 0, 0), feedback_rect)
    redraw_word_text()

# Set up the Pygame window
window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE | pygame.DOUBLEBUF, 32)

# Create a font object for displaying the text
font = pygame.font.Font("fonts/Audiowide-Regular.ttf", 120)
font1 = pygame.font.Font("fonts/Audiowide-Regular.ttf", 150)
# Create surfaces for True and False buttons
true_button = pygame.Surface((400, 150))
true_button.fill((220, 220, 220))
false_button = pygame.Surface((400, 150))
false_button.fill((220, 220, 220))

words = ["RED", "GREEN", "BLUE", "YELLOW", "BROWN", "VIOLET", "ORANGE"]
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (109, 39, 9), (148, 0, 211), (255, 165, 0)]

def random_word_and_color():
    word = random.choice(words)
    correct_color = colors[words.index(word)]

    if random.random() < 0.5:
        color = correct_color
    else:
        other_colors = [c for c in colors if c != correct_color]
        color = random.choice(other_colors)
    return word, color

word, color = random_word_and_color()
word_text = font.render(word, True, color)
word_text_rect = word_text.get_rect(center=(window_width / 2, window_height / 5))

def redraw_word_text():
    global word_text, word_text_rect, word, color

    pygame.draw.rect(window, (0, 0, 0), word_text_rect)
    word, color = random_word_and_color()
    word_text = font.render(word, True, color)
    word_text_rect = word_text.get_rect(center=(window_width / 2, window_height / 5))
    window.blit(word_text, word_text_rect)
    pygame.display.flip()
# Render the text
true_text = font.render("True", True, (0, 0, 0))
false_text = font.render("False", True, (0, 0, 0))
word_text = font1.render("BLUE", True, (0, 0, 255))

# Draw the text on the buttons
true_button.blit(true_text, (40, 0))
false_button.blit(false_text, (20, 0))

# Calculate button positions
word_text_rect = word_text.get_rect(center=(window_width / 2, window_height / 5))
true_rect = true_button.get_rect(center=(window_width/4, window_height - window_height/6))
false_rect = false_button.get_rect(center=(window_width - window_width/4, window_height - window_height/6))

# Display the buttons
window.blit(true_button, true_rect)
window.blit(false_button, false_rect)
window.blit(word_text, word_text_rect)

# Update the display
pygame.display.flip()

# Keep the window open until the user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            correct = color == colors[words.index(word)]
            if true_rect.collidepoint(event.pos):
                if correct:
                    print("Correct")
                    display_feedback_rect((0, 255, 0))
                else:
                    print("Incorrect")
                    display_feedback_rect((255, 0, 0))
            elif false_rect.collidepoint(event.pos):
                if not correct:
                    print("Correct")
                    display_feedback_rect((0, 255, 0))
                else:
                    print("Incorrect")
                    display_feedback_rect((255, 0, 0))
pygame.quit()
quit()