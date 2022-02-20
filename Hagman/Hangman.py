import random
import pygame
import math
import sys
from pygame.locals import *

# basic setup
pygame.init()
clock = pygame.time.Clock()

from words import words
print(words)

#window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(("Hangman"))

# Colors
WHITE = (249, 224, 217) #pinkish red
PURP = (93, 73, 84) #darkpurple
BLACK = (0,0,0)

#Images
IMAGES = []

for i in range(7):
    image = pygame.image.load(f'images/hangman{i}.png')
    IMAGES.append(image) #i load each image, and then i add to the []

# variables
hangman_status = 0
guessed = []

def get_valid_word(words):
    word = random.choice(words) #randoomly chooses word
    while '-' in word or ' ' in word:
        word = random.choice(words)
    print(word)
    return word

word = get_valid_word(words)

# Buttons. using for loop to draw button. 26 total, 2 rows 13 in each. 
# wdith - ((gap + 2*radius)*13)/2
RADIUS = 20
GAP = 15
letters = [] #< want to give us x, y, letter
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2)) #integer division excludes the answer? 14//13 = 1. 
    letters.append([x, y, chr(A + i), True]) #we add it to our array. we get character rep of #65 + i

# fonts
LETTER_FONT = pygame.font.SysFont('montserrat', 30)
WORD_FONT = pygame.font.SysFont('montserrat', 60)
TITLE_FONT = pygame.font.SysFont('montserrat', 70)



def draw():
    screen.fill(WHITE) #fills screen background color 
    # draw title
    text = TITLE_FONT.render("hangman :)" , 1, PURP)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    # draw word
    display_word = ""
    for letter in word: #loop thru letter
        if letter.upper() in guessed:
            display_word += letter.upper() + " " 
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, PURP)
    screen.blit(text, (400, 200))



    # draw buttons
    for letter in letters:
        x, y, let, visible = letter #splitting up variables -- [x, y, letter]
        if visible:
            pygame.draw.circle(screen, PURP, (x,y), RADIUS, 2) #drawing circle center at x,y
            text = LETTER_FONT.render(let, 1, BLACK) #render the font
            screen.blit(text, (x - text.get_width()/2 , y - text.get_height()/2 + 3))


    screen.blit(IMAGES[hangman_status],(150,100)) #draw image, given x y position
    pygame.display.update()


def display_message(message):
        pygame.time.delay(3000)
        screen.fill(WHITE)
        text = WORD_FONT.render(message , 1, PURP)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)


# background stuff?
while True:
    clock.tick(50) #frame rate

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, let, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2) #ditsance b/w mouse and center of button
                    if dis < RADIUS:
                        letter[3] = False #change it to invisible when clicked
                        guessed.append(let) #add letter to guess
                        print(guessed)
                        if let.lower() not in word:
                           hangman_status += 1
    draw()

    won = True
    for letter in word:
        if letter.upper() not in guessed:
            won = False
            break
    
    if won:
        display_message("good job! you won :)")
        break 

    if hangman_status == 6:
        display_message("i'm sorry, you lost :(")
        final_word = "the word was: "+ word
        display_message(final_word)
        break


    
