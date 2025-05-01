from tkinter import *

window = Tk()
window.title('Sample Window')
window.geometry('400x400')
window.configure(bg='light blue')

greeting = Label(text='Hello! These is my first Tkinter', fg='black', bg='white')
button = Button(text='Click me', fg='black', bg='white')
entry = Entry(fg='yellow', bg='blue', width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief='ridge', borderwidth=5)
frame.pack()

label = Label(master=frame, text='This is a frame')
label.pack()

text = Text(master=frame, fg='yellow', bg='blue')
text.pack()

window.mainloop()
