print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import tkinter as tk
import random
from tkinter import Tk, Label, Entry, W, N, E, S
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 120
def startGame(event):
    """Bắt đầu trò chơi khi nhấn phím Enter (hoặc khi gọi trực tiếp)."""
    global timeleft
    if timeleft == 120:
        countdown()
    nextColour()
def nextColour():
    """Kiểm tra câu trả lời, cập nhật điểm, và hiển thị màu mới."""
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text = str(colours[0]))
        scorelabel.config(text = "Score: " + str(score))
def countdown():
    """Đếm ngược thời gian và cập nhật Label hiển thị thời gian."""
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text = "Time left: " + str(timeleft))
        timelabel.after(1000, countdown)
    elif timeleft == 0:
        scorelabel.config(text=f"Game Over! Final Score: {score}")
root = tk.Tk()
root.title("COLOURGAME")
root.geometry("375x300")
instructions = tk.Label(
    root, 
    text = "Type in the colour of the words, and not the word text!",
    font = ('Helvetica', 12)
)
instructions.pack()
scorelabel = tk.Label(
    root, 
    text = "Press enter to start", 
    font = ('Helvetica', 12)
)
scorelabel.pack()
timelabel = tk.Label(
    root, 
    text = "Time left: " + str(timeleft), 
    font = ('Helvetica', 12)
)
timelabel.pack()
label = tk.Label(
    root, 
    font = ('Helvetica', 60)
)
label.pack()
e = tk.Entry(root)
root.bind('<Return>', startGame) 
e.pack()
e.focus_set()
root.mainloop()
