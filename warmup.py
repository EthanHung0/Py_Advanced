from guizero import *
import random

"""app = App(title="warm up1", width=500, height=500)

Text(app,text="Nhập điểm của bạn",size=20,color="blue")
Text(app,text="điểm toán:")
math = TextBox(app)
Text(app,text="điểm văn:")
lit = TextBox(app)
Text(app,text="điểm anh:")
eng = TextBox(app)

def classification():
    try:
        if 0<=int(math.value)<=10 and 0<=int(lit.value)<=10 and 0<=int(eng.value)<=10:
            tbc = (int(math.value) + int(lit.value) + int(eng.value))/3
            if 0<=tbc<=4.5:
                ranking = "Yếu"
            elif tbc<=6.5:
                ranking = "TB"
            elif tbc<=8:
                ranking = "Khá"
            elif tbc<=10:
                ranking = "Giỏi"
            Final.value = f"Điểm trung bình: {tbc:.2f} - Học lực {ranking}"
        else:
            warn(title="ERROR",text="Vui lòng nhập đúng điểm")
    except ValueError:
        warn(title="ERROR",text="Vui lòng nhập đủ điểm")

PushButton(app,text="Tính TBC",command=classification)
Final = Text(app,"Điểm trung bình: ")

app.display()"""

#=========================================================================================

"""guessnumber = App(title="Guess The Number!",width=500,height=500)
Text(guessnumber,text="Guess a number between 1 to 100",size=20,color="blue")
guess = TextBox(guessnumber)

game = random.randint(1, 100)
def takeguess():
    tguess = int(guess.value)
    Results.value = "Too high!" if tguess > game else "Too low!" if tguess < game else "You guessed the correct number!"

thebutton = PushButton(guessnumber,text="Take A Guess",command=takeguess)
Results = Text(guessnumber)

guessnumber.display()"""

#=========================================================================================

from guizero import *
app2 = App(title="Schedule",width=500,height=500,bg="#D3D3D3")

Text(app2,text="Make Your Schedule!",size=20,color="blue",bg="white")
dad = Box(app2,layout="grid")
Text(dad,"Tasks: ",grid=[0,0])
task = TextBox(dad,grid=[1,0])
task.bg = "white"

def save():
    with open("tasks.txt",mode="w",encoding="utf-8") as a:
        for i in Tlist.items:
            a.write(f"{i.strip()}\n")
def add_schedule():
    if not task.value:
        warn("ERROR!","Empty input!")
    else:
        Tlist.append(task.value)
        task.value = ""
        save()
def remove_schedule():
    if not Tlist.value:
        warn("ERROR!","Schedule is empty!")
    else:
        Tlist.remove(Tlist.value)
        save()

add = PushButton(dad,grid=[2,0],command=add_schedule,text="ADD")
add.bg = "white"
remov = PushButton(dad,command=remove_schedule,grid=[2,1],text="REMOVE")
remov.bg = "white"
Tlist = ListBox(app2,width=1000,height=1000)
Tlist.bg = "white"

app2.display()