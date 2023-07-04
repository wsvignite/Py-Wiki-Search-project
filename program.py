from tkinter import *
import wikipedia

def get_data():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "ERROR! Try other inputs & Check the internet connection")

win = Tk()
win.title("Small Wiki - By WSV Ignite")
win.configure(bg="#F5F5F5")

frame = Frame(win, bg="#F5F5F5", padx=20, pady=20)
frame.pack()

label = Label(frame, text="Search on Small Wiki", font=("Arial", 16, "bold"), fg="#2C2C2C", bg="#F5F5F5")
label.pack(pady=10)

entry = Entry(frame, font=("Arial", 12), bg="#E0E0E0")
entry.pack()

button = Button(frame, text="SEARCH", command=get_data, font=("Arial", 14, "bold"), fg="white", bg="#007AFF", bd=0, relief=FLAT, padx=20)
button.pack(pady=10)

result_frame = Frame(win, bg="#F5F5F5")
result_frame.pack(padx=20, pady=20)

scroll = Scrollbar(result_frame)
scroll.pack(side=RIGHT, fill=Y)

answer = Text(result_frame, width=60, height=15, yscrollcommand=scroll.set, wrap=WORD, font=("Arial", 12), bg="white", bd=0)
answer.pack()

scroll.config(command=answer.yview)

win.mainloop()
