from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#Setting up main window
root = Tk()
root.title("Denomination counter")
root.configure(bg="light blue")
root.geometry("650x400")

#Adding Image and Labels in the main window
upload = Image.open("app_img.jpg")

#Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg="light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)

#Fuction to display a messagebox and proceed if Ok in Clicked
def msg():
    Msgbox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?"       
    )
    if Msgbox == "ok":
        topwin()

# Adding Buttons to the Main window
button1 = Button(
    master=root,
    text="Let's Start",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=300, y=360)

#Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x600")

    label = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg="light grey")

    l1 = Label(top, text="1000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="200", bg="light grey")
    l4 = Label(top, text="100", bg="light grey")
    l5 = Label(top, text="50", bg="light grey")
    l6 = Label(top, text="20", bg="light grey")
    l7 = Label(top, text="10", bg="light grey")
    l8 = Label(top, text="5", bg="light grey")
    l9 = Label(top, text="2", bg="light grey")
    l10 = Label(top, text="1", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)
    t8 = Entry(top)
    t9 = Entry(top)
    t10 = Entry(top)

# Calculation
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note200 = amount // 200
            amount %= 200
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50
            note20 = amount // 20
            amount %= 20
            note10 = amount // 10
            amount %= 10
            note5 = amount // 5
            amount %= 5
            note2 = amount // 2
            amount %= 2
            note1 = amount // 1
            amount %= 1

            t1.delete(0, END) 
            t2.delete(0, END) 
            t3.delete(0, END) 
            t4.delete(0, END) 
            t5.delete(0, END) 
            t6.delete(0, END) 
            t7.delete(0, END) 
            t8.delete(0, END) 
            t9.delete(0, END) 
            t10.delete(0, END)

            t1.insert(END, str(note1000)) 
            t2.insert(END, str(note500)) 
            t3.insert(END, str(note200)) 
            t4.insert(END, str(note100)) 
            t5.insert(END, str(note50)) 
            t6.insert(END, str(note20)) 
            t7.insert(END, str(note10)) 
            t8.insert(END, str(note5)) 
            t9.insert(END, str(note2)) 
            t10.insert(END, str(note1))
        except ValueError:
            messagebox.showerror("Error", "Please enter a vaild number")

    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")

    # Centering Widgets in the Top window
    label.place(x=270, y=50)
    entry.place(x=260, y=80)
    btn.place(x=180, y=150)

    l1.place(x=180, y=200) 
    l2.place(x=180, y=230) 
    l3.place(x=180, y=260) 
    l4.place(x=180, y=290) 
    l5.place(x=180, y=320) 
    l6.place(x=180, y=350) 
    l7.place(x=180, y=380) 
    l8.place(x=180, y=410) 
    l9.place(x=180, y=440) 
    l10.place(x=180, y=470)

    t1.place(x=270, y=200) 
    t2.place(x=270, y=230) 
    t3.place(x=270, y=260) 
    t4.place(x=270, y=290) 
    t5.place(x=270, y=320) 
    t6.place(x=270, y=350) 
    t7.place(x=270, y=380) 
    t8.place(x=270, y=410) 
    t9.place(x=270, y=440) 
    t10.place(x=270, y=470)

    top.mainloop()

root.mainloop()

