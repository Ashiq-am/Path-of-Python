# Import necessary modules
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create the main window
root = Tk()
root.geometry('1100x320')  # Set the window size
root.resizable(0, 0)  # Disable window resizing
root['bg'] = 'pink'  # Set background color
root.title('Real-time translator')  # Set window title

# Create a label for the title
Label(root, text="Language Translator", font="Arial 20 bold").pack()

# Create a label for the input text
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)

# Create an entry widget for user input
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

# Create a label for the output
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)

# Create a text widget for displaying the translation
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

# Get the list of supported languages
language = list(LANGUAGES.values())

# Create a Combobox for selecting the destination language
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('Choose Language')  # Set default value


# Function to perform translation
def Translate():
    try:
        # Create a Translator object
        translator = Translator()

        # Translate the input text to the selected destination language
        translation = translator.translate(Input_text.get(), dest=dest_lang.get())

        # Clear the output text and insert the translation
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation.text)
    except Exception as e:
        print(f"Translation error: {e}")


# Create a button for triggering translation
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='orange',
                   activebackground='green')
trans_btn.place(x=445, y=180)

# Start the Tkinter event loop
root.mainloop()
