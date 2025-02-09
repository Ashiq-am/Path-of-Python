class NumberInWords:
    def last_digit_in_words(self, number):
        last_digit = number % 10
        words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return words[last_digit]

# Example usage:
niw = NumberInWords()
print(niw.last_digit_in_words(123))
