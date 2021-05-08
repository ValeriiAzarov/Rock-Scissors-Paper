from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint


# about
def about():
    messagebox.showinfo('About', 'Student of group 535A\nAzarov Valerii')


# reset points
def reset():
    computer_score["text"] = 0
    player_score["text"] = 0


# center a window on the screen
def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


# main window
root = Tk()
root.title("Rock Scissor Paper")
root.iconbitmap('images/ico/icon.ico')
root.configure(background="#2A2C2B")
center_window(855, 500)
root.resizable(0, 0)


# main menu
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label='About', command=about)
main_menu.add_command(label='Reset', command=reset)


# picture
rock_img_user = ImageTk.PhotoImage(Image.open("images/rock-user.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("images/paper-user.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("images/scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("images/rock-computer.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("images/paper-computer.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("images/scissors-computer.png"))

# insert picture
user_label = Label(root, image=scissor_img_user, bg="#2A2C2B")
comp_label = Label(root, image=scissor_img_comp, bg="#2A2C2B")
comp_label.grid(padx=0, pady=50, row=1, column=0)
user_label.grid(padx=0, pady=50, row=1, column=4)

# scores
player_score = Label(root, text=0, font=("Arial", 48), bg="#2A2C2B", fg="white")
computer_score = Label(root, text=0, font=("Arial", 48), bg="#2A2C2B", fg="white")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

# indicators
user_indicator = Label(root, padx=0, pady=25, font=50, text="USER", bg="#2A2C2B", fg="white")
comp_indicator = Label(root, padx=0, pady=25, font=50, text="COMPUTER", bg="#2A2C2B", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
message = Label(root, font=50, bg="#2A2C2B", fg="white")
message.grid(row=1, column=2)


# update message
def updateMessage(x):
    message['text'] = x


# update user score
def updateUserScore():
    score = int(player_score["text"])
    score += 1
    player_score["text"] = str(score)


# update computer score
def updateCompScore():
    score = int(computer_score["text"])
    score += 1
    computer_score["text"] = str(score)


# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass


# update choices
choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    # for user
    if x == "rock":
        user_label.configure(image=rock_img_user)
    elif x == "paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissor_img_user)
    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white",
              command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white",
               command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white",
                 command=lambda: updateChoice("scissor")).grid(row=2, column=3)


if __name__ == '__main__':
    root.mainloop()
