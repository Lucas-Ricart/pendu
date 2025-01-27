import os

# Add score to file
def add_score(name, score):
    """Add a player's score to the leaderboard."""
    with open("scores.txt", "a") as file:
        file.write(f"{name}:{score}\n")

# Read scores from file
def read_scores():
    """Read scores from the leaderboard file and return a sorted list."""
    scores = []
    if not os.path.exists("scores.txt"):
        return scores

    with open("scores.txt", "r") as file:
        for line in file:
            try:
                name, score = line.strip().split(":")
                scores.append((name, int(score)))
            except ValueError:
                continue
    return sorted(scores, key=lambda x: x[1], reverse=True)