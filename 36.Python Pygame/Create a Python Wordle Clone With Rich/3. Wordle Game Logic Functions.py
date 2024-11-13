def display_word(word, correct_guesses):
    displayed_word = ""
    for letter in word:
        if letter in correct_guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def evaluate_guess(word, guess, correct_guesses):
    if guess.lower() == word.lower():
        correct_guesses.update(word)
        return True
    return False

def game_status(word, correct_guesses):
    if set(word.lower()) == correct_guesses:
        return "win"
    return "ongoing"
