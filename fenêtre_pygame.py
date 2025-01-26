import pygame
import random

pygame.init()

#set window
width, height = 720, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman_Game.py")


#colors
white = (255, 255, 255)
black = (0, 0, 0)

#display alphabet
radius = 20
gap = 15
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 360
A = 65
letters = []
for i in range(26) :
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(A + i), True])


#fonts
font = pygame.font.SysFont('comicsans', 25)

#game variables
words = []
pseudo_ok = False
pseudo = ""
choice = True
add = ""
leaderboard = False
choose_difficulty = False
difficulty_level = None
add_word = ""
def restart(difficulty_level) :
    """reset variables"""
    fail = 0
    guess = ""
    guessed = []
    letters = []
    for i in range(26) :
        x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
        y = starty + ((i // 13) * (gap-15 + radius * 2))
        letters.append([x, y, chr(A + i), True])
    words = []
    with open("words.txt", "r") as fl :
        for l in fl :
            words.append(l.rstrip('\n'))
    words1 = [word for word in words if 1 <= len(word) <= 5]
    words2 = [word for word in words if 1 <= len(word) <= 7]
    words3 = [word for word in words if 6 <= len(word)]
    word = "start"
    if difficulty_level == 1 :
        word = random.choice(words1).upper()
    elif difficulty_level == 2 :
        word = random.choice(words2).upper()
    elif difficulty_level == 3 :
        word = random.choice(words3).upper()
    print(word)
    return word, fail, guessed, letters, guess
word, fail, guessed, letters, guess = restart(difficulty_level)
    
#load images
images = []
for i in range(8) :
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw() :
    #draw background
    win.fill(white)
    if add == True :
        text = font.render(f"Enter a new word : {add_word}", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2)))
    elif leaderboard == True :
        #attention
        None
    elif choice == True :
        #draw selection 
        text = font.render("Press enter to start a game", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2-25)))
        text = font.render("Press A to add a word in the game", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2)))
        text = font.render("Press S to see the leaderboard", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2+25)))
    elif pseudo_ok == False :
        #draw pseudo selection
        text = font.render(f"Choose a pseudo : {pseudo}", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2)))
    elif choose_difficulty == True :
        text = font.render("Choose a difficulty :", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2-37.5)))
        text = font.render("1. Easy", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2-12.5)))
        text = font.render("2. Normal", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2+12.5)))
        text = font.render("3. Hard", 1, black)
        win.blit(text, text.get_rect(center=(width//2, height//2+37.5)))
    
    else :
        #draw hangman
        win.blit(images[fail], image.get_rect(center=(width//2+20, 125)))
        if fail < 7 :
            #winning screen
            if guess == word :
                text = font.render("WINNER! PRESS ENTER TO RESTART.", 1, black)
                if fail > 0 :
                    win.blit(text, text.get_rect(center=(width//2, height//2+100)))
                else :
                    win.blit(text, text.get_rect(center=(width//2, height//2)))
            else :
                #draw word
                display_word = ""
                for letter in word :
                    if letter in guessed :
                        display_word += letter + " "
                    else :
                        display_word += "_ "
                text = font.render(display_word, 1, black)
                win.blit(text, text.get_rect(center=(width//2, height//2+35)))
                #draw buttons
                for letter in letters :
                    x, y, ltr, visible = letter
                    if visible :
                        text = font.render(ltr, 1, black)
                        win.blit(text, (x - text.get_width() / 2-3, y - text.get_height() / 2+50))
        else:
            #loosing screen
            loser = font.render("LOOSER! PRESS ENTER TO RESTART.", 1, black)
            win.blit(loser, loser.get_rect(center=(width//2, height//2)))
    pygame.display.update()



while run :
    clock.tick(FPS)

    


    draw()
    #verify input
    guess = ""
    for letter in word :
        if letter in guessed :
            guess += letter 

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                #ajouter score ici
                words = []
                pseudo_ok = False
                pseudo = ""
                choice = True
                add = ""
                leaderboard = False
                choose_difficulty = False
                difficulty_level = None
                add_word = ""
                word, fail, guessed, letters, guess = restart(difficulty_level)
            elif guess == word :
                if event.key ==13 :
                    word, fail, guessed, letters, guess = restart(difficulty_level)
            elif fail == 7 :
                if event.key == 13 :
                    words = []
                    pseudo_ok = False
                    pseudo = ""
                    choice = True
                    add = ""
                    leaderboard = False
                    choose_difficulty = False
                    difficulty_level = None
                    add_word = ""
                    word, fail, guessed, letters, guess = restart(difficulty_level)
            elif add == True :
                if event.key == pygame.K_BACKSPACE :
                    add_word = add_word[:-1]
                elif event.key == 13 :
                    add = False
                    if add_word != "" and " " not in add_word :
                        with open("words.txt", "a") as fl :
                            fl.write(f"\n{add_word}")
                        add_word = ""
                else :
                    add_word += event.unicode.lower()
            elif leaderboard == True :
                #attention afficher score ici
                None
            elif choice == True :
                if event.key == 13 :
                    choice = False
                elif event.key == 97 :
                    add = True
                elif event.key == 115 :
                    leaderboard = True
            elif pseudo_ok == False :
                if event.key == pygame.K_BACKSPACE :
                    pseudo = pseudo[:-1]
                elif event.key == 13 :
                    pseudo_ok = True
                    choose_difficulty = True
                else :
                    pseudo += event.unicode.upper()
            elif choose_difficulty == True :
                if event.key == 49 or event.key == 1073741913 :
                    difficulty_level = 1
                    choose_difficulty = False
                    word, fail, guessed, letters, guess = restart(difficulty_level)
                elif event.key == 50 or event.key == 1073741914 :
                    difficulty_level = 2
                    choose_difficulty = False
                    word, fail, guessed, letters, guess = restart(difficulty_level)
                elif event.key == 51 or event.key == 1073741915 :
                    difficulty_level = 3
                    choose_difficulty = False
                    word, fail, guessed, letters, guess = restart(difficulty_level)
            else :
                if 97 <= event.key <= 122 :
                    pressed = chr(event.key).upper()
                    for letter in letters :
                        x, y, ltr, visible = letter
                        if visible :
                            if ltr == pressed :
                                letter[3] = False
                                guessed.append(ltr)
                                if ltr not in word :
                                    fail +=1

pygame.quit()