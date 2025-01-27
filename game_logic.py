import random

# Restart game logic
def restart(difficulty_level, word_list):
    """Reset game variables and select a new word."""
    fail = 0
    guessed = []
    letters = []
    radius, gap, startx, starty = 20, 15, 50, 360  # Letter button positions

    # Initialize letters
    for i in range(26):
        x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
        y = starty + ((i // 13) * (gap + radius * 2))
        letters.append([x, y, chr(65 + i), True])  # A-Z buttons

    # Filter words by difficulty
    if difficulty_level == 1:  # Easy
        word_pool = [word for word in word_list if len(word) <= 5]
    elif difficulty_level == 2:  # Normal
        word_pool = [word for word in word_list if 6 <= len(word) <= 7]
    else:  # Hard
        word_pool = [word for word in word_list if len(word) > 7]

    # Select a random word
    word = random.choice(word_pool).upper()
    return word, fail, guessed, letters

# Check user guess
def check_guess(word, guessed, letter):
    """Verify if the guessed letter is in the word."""
    if letter in word and letter not in guessed:
        guessed.append(letter)
        return True
    else:
        return False