import pygame

# Initialize Pygame
pygame.init()

# Set up window
WIDTH, HEIGHT = 720, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman_Game.py")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont('comicsans', 25)

# Draw the game interface
def draw_interface(images, fail, guessed, word, letters, add, add_word, display_lb, scores, choice, name, name_ok, choose_difficulty):
    """Draws the game interface based on the current state."""
    win.fill(WHITE)

    if add:  # Add word mode
        text = font.render(f"Enter a new word: {add_word}", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    elif display_lb:  # Leaderboard mode
        title = font.render("Leaderboard", 1, BLACK)
        win.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        y = 100
        for i, (player_name, score) in enumerate(scores[:10]):  # Display top 10 scores
            text = font.render(f"{i + 1}. {player_name}: {score}", 1, BLACK)
            win.blit(text, (260, y))
            y += 30

        back_text = font.render("Press ESC to return to the menu.", 1, BLACK)
        win.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 50))

    elif choice:  # Menu
        text = font.render("Press Enter to start a game", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25)))
        text = font.render("Press A to add a word to the game", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        text = font.render("Press S to see the leaderboard", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25)))

    elif not name_ok:  # Enter name screen
        text = font.render(f"Choose a name: {name}", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    elif choose_difficulty:  # Difficulty selection
        text = font.render("Choose a difficulty:", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 37.5)))
        text = font.render("1. Easy", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 12.5)))
        text = font.render("2. Normal", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 12.5)))
        text = font.render("3. Hard", 1, BLACK)
        win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 37.5)))

    else:  # Main game
        win.blit(images[fail], (WIDTH // 2 - images[fail].get_width() // 2, 100))

        if fail < 7:
            # If not failed completely, draw word and buttons
            display_word = " ".join([letter if letter in guessed else "_" for letter in word])
            text = font.render(display_word, 1, BLACK)
            win.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 35)))

            for x, y, letter, visible in letters:
                if visible:
                    text = font.render(letter, 1, BLACK)
                    pygame.draw.circle(win, BLACK, (x, y), 20, 3)
                    win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

        else:  # Losing screen
            loser_text = font.render("YOU LOST! Press Enter to restart.", 1, BLACK)
            win.blit(loser_text, loser_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.update()