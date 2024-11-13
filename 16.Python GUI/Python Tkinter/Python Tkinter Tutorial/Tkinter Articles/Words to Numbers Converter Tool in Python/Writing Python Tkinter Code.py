import tkinter as tk
from word2number import w2n

def convert_to_number():
    input_text = entry.get()
    try:
        result = w2n.word_to_num(input_text)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(
            text="Invalid input, please enter a valid numeric word.")

# Create the main window
app = tk.Tk()
app.title("Words to Numbers Converter")

# Create and place widgets
label = tk.Label(app, text="Enter a numeric word:")
label.pack(pady=10)

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

convert_button = tk.Button(app, text="Convert", command=convert_to_number)
convert_button.pack(pady=10)

result_label = tk.Label(app, text="Result: ")
result_label.pack(pady=10)

# Run the application
app.mainloop()
