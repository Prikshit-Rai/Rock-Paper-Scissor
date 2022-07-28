from tkinter import *
from PIL import Image,ImageTk
from random import randint

root =Tk() #main window
root.title("Rock Paper Scissor")
root.configure(background="#E77A40")

#images
rock_img=ImageTk.PhotoImage(Image.open("rock.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor.png"))

#images in window
user_label=Label(root,image=rock_img,bg="#E77A40")
user_label.grid(row=1, column=0)
com_label=Label(root,image=rock_img,bg="#E77A40")
com_label.grid(row=1, column=9)

#points
playersPoint=Label(root,text=0,font=100,bg="#E77A40",fg="white")
playersPoint.grid(row=1,column=1)
compPoint=Label(root,text=0,font=100,bg="#E77A40",fg="white")
compPoint.grid(row=1,column=8)
user_indicator = Label(root,font=50,text="User",bg="#E77A40",fg="white")
user_indicator.grid(row=0,column=1)
comp_indicator = Label(root,font=50,text="Computer",bg="#E77A40",fg="white")
comp_indicator.grid(row=0,column=8)

#result

result=Label(root,font=50, bg="#E77A40",fg="white")
result.grid(row=3,column=5)

def updateResult(x):
    result['text'] = x

def updateUserPoints():
    points = int(playersPoint["text"])
    points +=1
    playersPoint["text"] = str(points)

def updateCompPoints():
    points = int(compPoint["text"])
    points +=1
    compPoint["text"] = str(points)

#check winner
def checkWinner(player, comp):
    if player == comp:
        updateResult("It's a tie..")
    elif player == "rock":
        if comp == "paper":
            updateResult("Computer Win..")
            updateCompPoints()
        else:
            updateResult("You Win..")
            updateUserPoints()
            
    elif player == "paper":
        if comp == "scissor":
            updateResult("Computer Win..")
            updateCompPoints()
        else:
            updateResult("You Win..")
            updateUserPoints()

    elif player == "scissor":
        if comp == "rock":
            updateResult("Computer Win..")
            updateCompPoints()
        else:
            updateResult("You Win..")
            updateUserPoints()
    else:
        pass

#choices
choices =["rock","paper","scissor"]

def updatechoice(x):
    
    #for computer choices
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        com_label.configure(image=rock_img)
    elif compChoice == "paper":
        com_label.configure(image=paper_img)
    elif compChoice == "scissor":
        com_label.configure(image=scissor_img)

    #for user choices
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    elif x == "scissor":
        user_label.configure(image=scissor_img)
    
    checkWinner(x,compChoice)

#options
rock=Button(root,width=20,height=2,text="Rock",bg="#59558D",fg="white", command=lambda:updatechoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="Paper",bg="#D0D004",fg="white", command=lambda:updatechoice("paper")).grid(row=2,column=5)
scissor=Button(root,width=20,height=2,text="Scissor",bg="#D004BA",fg="white", command=lambda:updatechoice("scissor")).grid(row=2,column=8)

root.mainloop()