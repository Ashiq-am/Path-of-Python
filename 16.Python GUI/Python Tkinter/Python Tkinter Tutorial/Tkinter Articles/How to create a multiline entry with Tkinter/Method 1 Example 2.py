import tkinter as tk


window = tk.Tk()
window.title("Text Widget with Scrollbar")

text = tk.Text(window, height=8, width=40)
scroll = tk.Scrollbar(window)
text.configure(yscrollcommand=scroll.set)
text.pack(side=tk.LEFT)

scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

insert_text = """GEEKSFORGEEKS : 
A Computer Science portal for geeks. 
It contains well written, well thought 
and well explained computer science and 
programming articles, quizzes and 
many more. 
GeeksforGeeks realises the importance of programming practice in the field of 
Computer Science. 
That is why, it also provides an option of practicing problems. 
This huge database of problems is created by programming experts. 
The active team of GeeksforGeeks makes the learning process 
interesting and fun. 
"""

text.insert(tk.END, insert_text)
tk.mainloop()
