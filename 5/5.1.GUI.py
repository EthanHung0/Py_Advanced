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

def selectNewtype():
    def typeConfirm():
        Win.destroy()
        Add()
    Win = Window(StorageApp,title="New Item",width=200,height=100)
    Text(Win,text="Select an Item Type.",size=15)
    global New_type
    b = Box(Win,layout="grid")
    New_type = Combo(b,options=["Book","DVD","Magazine"],width=8,height=1,grid=[0,0])
    PushButton(b,command=typeConfirm,width=5,height=1,text="Confirm",grid=[1,0])


def Add():
    NewItem = Window(StorageApp,title="New Item",width=200,height=300)
    Text(NewItem,text="Add A New Item",size=15)
    Text(NewItem,text="Input new item info",size=8)

    InputBox = Box(NewItem,layout="grid",width=180,height=200)

    Text(InputBox,text="ID: ",align="left",grid=[0,0])
    New_id = TextBox(InputBox,width=5,height=1,align="left",grid=[1,0])

    Text(InputBox,text="Title",align="left",grid=[0,1])
    New_title = TextBox(InputBox,width=15,height=1,align="left",grid=[1,1])

    Text(InputBox,text="Author",align="left",grid=[0,2])
    New_author = TextBox(InputBox,width=15,height=1,align="left",grid=[1,2])

    global New_pages, New_duration, New_issue
    New_pages = None
    New_duration = None
    New_issue = None

    if New_type.value == "Book":
        Text(InputBox,text="Pages: ",align="left",grid=[0,3])
        New_pages = TextBox(InputBox,width=5,height=1,align="left",grid=[1,3])
    elif New_type.value == "DVD":
        Text(InputBox,text="Duration (second):",align="left",grid=[0,3])
        New_duration = TextBox(InputBox,width=10,height=1,align="left",grid=[1,3])
    else:
        Text(InputBox,text="Issue: #",align="left",grid=[0,3])
        New_issue = TextBox(InputBox,width=5,height=1,align="left",grid=[1,3])

    def is_num(s):
        if all(i in "0123456789" for i in s):
            return True
        return False
    def Confirm():
        id_val = New_id.value.strip()
        title_val = New_title.value.strip()
        author_val = New_author.value.strip()

        def filled(b):
            return b is not None and b.value.strip() != ""

        if len(id_val) != 3:
            info("Invalid Input","Item ID must be exactly 3 digits.")
            return

        try:
            if New_type.value == "Book" and filled(New_pages) and is_num(New_pages.value):
                stuff.append(Classes.Book(f"B{id_val}",title_val,author_val,int(New_pages.value)))
            elif New_type.value == "DVD" and filled(New_duration) and is_num(New_duration.value):
                stuff.append(Classes.DVD(f"D{id_val}",title_val,author_val,int(New_duration.value)))
            elif New_type.value == "Magazine" and filled(New_issue) and is_num(New_issue.value):
                stuff.append(Classes.Magazine(f"M{id_val}",title_val,author_val,int(New_issue.value)))
            Display_Sort("A")
            NewItem.destroy()
        except Exception as e:
            info("Error",f"Unexpected Error: {e}")
            return

    PushButton(NewItem,command=Confirm)


Buttons = Box(Display,layout="grid",align="top",grid=[0,0])
DList = ListBox(Display,width=700,height=400,grid=[1,0,1,2])
Display_Sort("A")
All = PushButton(Buttons,text="All",width=8,height=1,command=Display_Sort,args=["A"],grid=[0,0])
BookSort = PushButton(Buttons,text="Books",width=8,height=1,command=Display_Sort,args=["B"],grid=[0,1])
DVDSort = PushButton(Buttons,text="DVDs",width=8,height=1,command=Display_Sort,args=["D"],grid=[0,2])
MagSort = PushButton(Buttons,text="Magazines",width=8,height=1,command=Display_Sort,args=["M"],grid=[0,3])

Inputs = Box(Display,layout="grid",align="bottom",grid=[0,1])
ADDButton = PushButton(Inputs,text="ADD",width=8,height=1,command=selectNewtype,grid=[0,0])
REMOVEButton = PushButton(Inputs,text="REMOVE",width=8,height=1,command=Remove,grid=[0,1])

StorageApp.display()
