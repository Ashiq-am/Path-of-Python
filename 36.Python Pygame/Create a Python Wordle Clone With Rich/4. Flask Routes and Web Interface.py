@app.route("/", methods=["GET", "POST"])
def index():
    global word_to_guess, correct_guesses, remaining_chances

    message = None
    message_class = None

    if request.method == "POST":
        guess = request.form["guess"]
        if guess:
            guess = guess.lower()
            if evaluate_guess(word_to_guess["word"], guess, correct_guesses):
                status = game_status(word_to_guess["word"], correct_guesses)
                if status == "win":
                    message = "Congratulations! You guessed the word: {}".format(word_to_guess["word"])
                    message_class = "congratulations"
                return render_template("index.html", message=message, message_class=message_class)
            else:
                remaining_chances -= 1
                if remaining_chances == 0:
                    message = "Game Over! The correct word was: {}".format(word_to_guess["word"])
                    message_class = "game-over"
                    return render_template("index.html", message=message, message_class=message_class)

    status = game_status(word_to_guess["word"], correct_guesses)
    displayed_word = display_word(word_to_guess["word"], correct_guesses)
    table = Table(title="[bold]Wordle[/bold]", show_lines=True)
    table.add_row(displayed_word)
    console.print(table)
    incorrect_boxes = ["green" if i < remaining_chances else "red" for i in range(5)]

    if status == "ongoing":
        return render_template("index.html", word=displayed_word, hint=word_to_guess["hint"],
                               remaining_chances=remaining_chances, status=status, incorrect_boxes=incorrect_boxes, message=message, message_class=message_class)
    else:
        return render_template("index.html", message=message, message_class=message_class)


@app.route("/reset")
def reset():
    global word_to_guess, correct_guesses, remaining_chances
    word_to_guess = random.choice(word_list)
    correct_guesses = set()
    remaining_chances = 5
    return redirect(url_for("index"))
