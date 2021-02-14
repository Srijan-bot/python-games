import tkinter
from tkinter import *
import random
import tkinter.messagebox as msg

root = tkinter.Tk()

root.title("ROCK PAPER SCISSOR")
root.iconbitmap("icon.ico")


    # player_choice.update()


def _credit_():
    credit__ = msg.showinfo("CREDIT", "This app is made by Srijan Kumar")


# Geomatery
root.geometry("632x340")
# root.resizable(0, 0)

menu = Menu(root)
menu.add_command(label="QUIT", command=quit)
root.config(menu=menu)

# Frames
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_1.pack()
frame_2.pack()

l1 = Label(frame_1, text="CHOOSE ANY OPTION/FIGURE TO  START AND RESTART THE GAME",
           pady=20, font="lucida 12 bold").pack(side=LEFT, anchor=E)
# l2=Label(frame_1,text="COMPUTER CHOICE").pack(side=RIGHT,anchor=W)


rhand = PhotoImage(file=r"rock.png")
shand = PhotoImage(file=r"scissor.png")
phand = PhotoImage(file=r"paper.png")

crock = PhotoImage(file=r"crock.png")
cpaper = PhotoImage(file=r"cpaper.png")
cscissor = PhotoImage(file=r"cscissor.png")
winner = PhotoImage(file=r"win.png")
looser = PhotoImage(file=r"loose.png")
tie = PhotoImage(file=r"tie.png")


rbtn = ''
pbtn = ''
sbtn = ''


click = True


def plays():
    global rbtn, pbtn, sbtn

    rbtn = Button(frame_2,text="rock", image=rhand, command=lambda: youPick("rock"))
    rbtn.config(bg="blue", text="rock", activebackground="yellow")
    rbtn.grid(row=0, column=0)
    # rbtn.bind("<Button-1>",choice_label)

    pbtn = Button(frame_2,text="paper",image=phand, command=lambda: youPick("paper"))
    pbtn.config(bg="gray", text="rock", activebackground="red")
    pbtn.grid(row=0, column=1)
    # pbtn.bind("<Button-1>",choice_label)

    sbtn = Button(frame_2,text="scissor",image=shand, command=lambda: youPick("scissor"))
    sbtn.config(bg="yellow", text="rock", activebackground="blue")
    sbtn.grid(row=0, column=2)
    # sbtn.bind("<Button-1>",choice_label)


def compchoice():
    comp = random.choice(["rock", "paper", "scissor"])
    return comp



def youPick(yourchoice):
    global click,player_choice
    # yourchoice=youpick
    i=0
    computerpick = compchoice()
    for i in range(5):
        i=i+1
        if click == True:
                if yourchoice == "rock":
                    rbtn.config(image=crock)
                    if computerpick == "rock":
                        sbtn.config(image=crock)
                        pbtn.config(image=tie)
                        click = False
                    elif computerpick == "paper":
                        sbtn.config(image=cpaper)
                        pbtn.config(image=looser)
                        click = False
                    elif computerpick == "scissor":
                        sbtn.config(image=cscissor)
                        pbtn.config(image=winner)
                        click=False
                        # ______________________
                if yourchoice == "paper":
                    rbtn.config(image=cpaper)
                    if computerpick == "rock":
                        sbtn.config(image=crock)
                        pbtn.config(image=winner)
                        click = False
                    elif computerpick == "paper":
                        sbtn.config(image=cpaper)
                        pbtn.config(image=tie)
                        click = False
                    elif computerpick == "scissor":
                        sbtn.config(image=cscissor)
                        pbtn.config(image=looser)
                        click=False
                        # ____________________
                if yourchoice == "scissor":
                    rbtn.config(image=cscissor)
                    if computerpick == "rock":
                        sbtn.config(image=crock)
                        pbtn.config(image=looser)
                        click = False
                    elif computerpick == "paper":
                        sbtn.config(image=cpaper)
                        pbtn.config(image=winner)
                        click = False
                    elif computerpick == "scissor":
                        sbtn.config(image=cscissor)
                        pbtn.config(image=tie)
                        click=False
        else:
            if yourchoice=="rock" or yourchoice=="paper" or yourchoice=="scissor" :
                
                rbtn.config(image=rhand)
                pbtn.config(image=phand)
                sbtn.config(image=shand)
                click=True
        player_choice.config(textvariable=yourchoice)
        i+=1
    else:
        pass

        


plays()

# player_choice=Label(root,textvariable=choose).pack()

credit = Button(root, text="CREDITS", pady=10,bg="red",fg="white",activebackground="white",activeforeground="red",command=_credit_).pack(side=BOTTOM,fill="x")
player_choice=Label(root,text="hi").pack()


# choice_label.config(text=youPick)



root.mainloop()
