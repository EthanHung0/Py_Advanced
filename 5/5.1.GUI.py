from guizero import *
import Classes

stuff = [
    Classes.Book("B001","AIUEO","SomeJPGuy",150),
    Classes.DVD("D002","SieuNhanGao","holysh",7200),
    Classes.Magazine("M003","ThangSau","nxbongod",12),
    Classes.Book("B002","Lập trình Python","Nguyễn Văn A",320),
    Classes.DVD("D101","Học Python qua phim","Lê Thị B",5400),
    Classes.Magazine("M301","Công nghệ hôm nay","Trần C",45)
]

StorageApp = App("The Storage",1000,700)
Text(StorageApp,"Welcome!",size=20)
Text(StorageApp,text="This is your storage!")

Display = Box(StorageApp,"grid")

def Display_Sort(item_type):
    DList.clear()
    if item_type == "A":
        for x in stuff:
            DList.append(x.get_info())
        return
    CorrectType = [y.get_info() for y in stuff if y.id[0] == item_type]
    if CorrectType:
        for z in CorrectType:
            DList.append(z)
    else:
        info("Notice","Category is Empty.")

def Remove():
    selected_Item = DList.value
    if selected_Item == None:
        info("Notice","No item selected.")
        return
    for i in stuff[:]:
        if i.get_info() == selected_Item:
            stuff.remove(i)
            Display_Sort("A")
            break

def Add():
    NewItem = Window(StorageApp,title="New Item",width=200,height=300)
    Text(NewItem,text="Add A New Item",size=15)
    Text(NewItem,text="Input new item info",size=8)

    InputBox = Box(NewItem,align="left",layout="grid")
    Text(InputBox,text="Type: ",align="left",grid=[0,0])
    New_type = Combo(InputBox,options=["Book","DVD","Magazine"],width=8,height=1,align="left",grid=[1,0])

    Text(InputBox,text="ID: ",align="left",grid=[0,1])
    New_id = TextBox(InputBox,width=5,height=1,align="left",grid=[1,1])

    Text(InputBox,text="Title",align="left",grid=[0,2])
    New_title = TextBox(InputBox,width=5,height=1,align="left",grid=[1,2])

    Text(InputBox,text="Author",align="left",grid=[0,3])
    New_author = TextBox(InputBox,width=5,height=1,align="left",grid=[1,3])

    # Text(InputBox,text="",align="left",grid=[0,4])
    # New_ = TextBox(InputBox,width=5,height=1,align="left",grid=[1,4])


Buttons = Box(Display,layout="grid",align="top",grid=[0,0])
DList = ListBox(Display,width=700,height=400,grid=[1,0,1,2])
Display_Sort("A")
All = PushButton(Buttons,text="All",width=8,height=1,command=Display_Sort,args=["A"],grid=[0,0])
BookSort = PushButton(Buttons,text="Books",width=8,height=1,command=Display_Sort,args=["B"],grid=[0,1])
DVDSort = PushButton(Buttons,text="DVDs",width=8,height=1,command=Display_Sort,args=["D"],grid=[0,2])
MagSort = PushButton(Buttons,text="Magazines",width=8,height=1,command=Display_Sort,args=["M"],grid=[0,3])

Inputs = Box(Display,layout="grid",align="bottom",grid=[0,1])
ADDButton = PushButton(Inputs,text="ADD",width=8,height=1,command=Add,grid=[0,0])
REMOVEButton = PushButton(Inputs,text="REMOVE",width=8,height=1,command=Remove,grid=[0,1])

StorageApp.display()
