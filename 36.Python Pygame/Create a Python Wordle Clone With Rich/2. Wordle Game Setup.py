# List of words and corresponding hints
word_list = [
    {"word": "python", "hint": "A programming language"},
    {"word": "flask", "hint": "A web framework for Python"},
    {"word": "banana", "hint": "A yellow fruit"},
    {"word": "mountain", "hint": "A land of green hills"},
    {"word": "sunflower", "hint": "A yellow color flower"}
    # Add more words and hints as needed
]

word_to_guess = random.choice(word_list)
correct_guesses = set()
remaining_chances = 5
