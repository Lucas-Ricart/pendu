import pygame
import random
import os

pygame.init()

#set window
WIDTH, HEIGHT = 720, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman_Game.py")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#display alphabet
radius = 20
gap = 15
startx = round((WIDTH - (radius * 2 + gap) * 13) / 2)
starty = 360
A = 65
letters = []
for i in range(26) :
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(A + i), True])

#fonts
font = pygame.font.SysFont('comicsans', 25)

#load images
images = []
for i in range(8) :
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

#game variables
def reset_all() :
    add = False
    add_word = ""
    display_lb = False
    score = 0
    choice = True
    name_ok = False
    name = ""
    choose_difficulty = False
    difficulty_level = None
    return name_ok, name, choice, add, display_lb, score, choose_difficulty, difficulty_level, add_word
name_ok, name, choice, add, display_lb, score, choose_difficulty, difficulty_level, add_word = reset_all()
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

if not os.path.exists("scores.txt"):
    with open("scores.txt", "w") as f:
        pass

def add_score(name, score):
    """add a score."""
    with open("scores.txt", "a") as f:
        f.write(f"{name}:{score}\n")

def read_scores():
    """Read scores from the file and return a sorted list."""
    scores = []
    with open("scores.txt", "r") as f:
        for line in f:
            try:
                name, score = line.strip().split(":")
                scores.append((name, int(score)))
            except ValueError:
                continue
    return sorted(scores, key=lambda x: x[1], reverse=True)

def draw(name) :
    #draw background
    win.fill(WHITE)
    if add == True :
        text = font.render(f"Enter a new word : {add_word}", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
    elif display_lb == True :
        title = font.render("Leaderboard", 1, BLACK)
        win.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        scores = read_scores()
        y = 100
        for i, (name, score) in enumerate(scores[:10]):  # Top 10 scores
            text = font.render(f"{i + 1}. {name}: {score}", 1, BLACK)
            win.blit(text, (260, y))
            y += 30
        back_text = font.render("Press ESC to return to the menu.", 1, BLACK)
        win.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 50))
    elif choice == True :
        #draw selection 
        text = font.render("Press enter to start a game", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2-25)))
        text = font.render("Press A to add a word in the game", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        text = font.render("Press S to see the leaderboard", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2+25)))
    elif name_ok == False :
        #draw name selection
        text = font.render(f"Choose a name : {name}", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
    elif choose_difficulty == True :
        text = font.render("Choose a difficulty :", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2-37.5)))
        text = font.render("1. Easy", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2-12.5)))
        text = font.render("2. Normal", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2+12.5)))
        text = font.render("3. Hard", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2+37.5)))
    
    else :
        #draw hangman
        win.blit(images[fail], image.get_rect(center=(WIDTH//2+20, 125)))
        if fail < 7 :
            #winning screen
            if guess == word :
                text = font.render("WINNER! PRESS ENTER TO RESTART.", 1, BLACK)
                if fail > 0 :
                    win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2+100)))
                else :
                    win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
            else :
                #draw word
                display_word = ""
                for letter in word :
                    if letter in guessed :
                        display_word += letter + " "
                    else :
                        display_word += "_ "
                text = font.render(display_word, 1, BLACK)
                win.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2+35)))
                #draw buttons
                for letter in letters :
                    x, y, ltr, visible = letter
                    if visible :
                        text = font.render(ltr, 1, BLACK)
                        win.blit(text, (x - text.get_width() / 2-3, y - text.get_height() / 2+50))
        else:
            #loosing screen
            loser = font.render("LOOSER! PRESS ENTER TO RESTART.", 1, BLACK)
            win.blit(loser, loser.get_rect(center=(WIDTH//2, HEIGHT//2)))
    pygame.display.update()



while run :
    clock.tick(FPS)
    draw(name)
    #verify input
    guess = ""
    for letter in word :
        if letter in guessed :
            guess += letter
    #check input
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                add_score(name, score)
                #ajouter score ici
                name_ok, name, choice, add, display_lb, score, choose_difficulty, difficulty_level, add_word = reset_all()
                word, fail, guessed, letters, guess = restart(difficulty_level)
            elif guess == word :
                #increase score
                if guess == word :
                    score += len(word)*5
                    guess = ""
                if event.key ==13 or event.key == 1073741912 :
                    word, fail, guessed, letters, guess = restart(difficulty_level)
            elif fail == 7 :
                if event.key == 13 or event.key == 1073741912 :
                    score = add_score(name, score)
                    name_ok, name, choice, add, display_lb, score, choose_difficulty, difficulty_level, add_word = reset_all()
                    word, fail, guessed, letters, guess = restart(difficulty_level)
            elif add == True :
                if event.key == pygame.K_BACKSPACE :
                    add_word = add_word[:-1]
                elif event.key == 13 or event.key == 1073741912 :
                    add = False
                    if add_word != "" and " " not in add_word :
                        with open("words.txt", "a") as fl :
                            fl.write(f"\n{add_word}")
                        add_word = ""
                else :
                    add_word += event.unicode.lower()
            elif choice == True :
                if event.key == 13 or event.key == 1073741912 :
                    choice = False
                elif event.key == 97 :
                    add = True
                elif event.key == 115 :
                    display_lb = True
            elif name_ok == False :
                if event.key == pygame.K_BACKSPACE :
                    name = name[:-1]
                elif event.key == 13 or event.key == 1073741912 :
                    name_ok = True
                    choose_difficulty = True
                    if name == "" :
                        name = "AAA"
                else :
                    name += event.unicode.upper()
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