from tkinter import *
import random
from tkinter.tix import Y_REGION

F_WIDTH = 10
F_HEIGHT = 20
P_SIZE = 30
COLORS = ['gray', 'lightgreen', 'pink', 'orange','blue','purple','red', 'yellow', 'cyan', 'black', 'white']

AllCoor = [
    [[-1,0,0,0,1,0,2,0],[0,-1,0,0,0,1,0,2],[-1,0,0,0,1,0,2,0],[0,-1,0,0,0,1,0,2]],
    [[-1,-1,0,-1,0,0,0,1],[-1,0,0,0,1,0,1,-1],[0,-1,0,0,0,1,1,1],[-1,0,-1,1,0,0,1,0]],
    [[0,-1,0,0,0,1,-1,1],[-1,-1,-1,0,0,0,1,0],[1,-1,0,-1,0,0,0,1],[-1,0,0,0,1,0,1,1]],
    [[-1,0,0,0,0,1,1,1],[0,-1,0,0,-1,0,-1,1],[-1,0,0,0,0,1,1,1],[0,-1,0,0,-1,0,-1,1]],
    [[0,0,0,1,-1,1,1,0],[-1,-1,-1,0,0,0,0,1],[0,0,0,1,-1,1,1,0],[-1,-1,-1,0,0,0,0,1]],
    [[0,0,0,1,1,0,1,1],[0,0,0,1,1,0,1,1],[0,0,0,1,1,0,1,1],[0,0,0,1,1,0,1,1]],
    [[0,-1,0,0,-1,0,0,1],[0,0,-1,0,0,1,1,0],[0,-1,0,0,0,1,1,0],[0,-1,0,0,-1,0,1,0]]
]


graphic = [[ 0 for c in range(F_WIDTH)] for r in range(F_HEIGHT)]

def Show_Graphic():
    global canvas
    for i in range(F_HEIGHT):
        for j in range(F_WIDTH):
            canvas.itemconfig(rectangles[i][j], fill = COLORS[graphic[i][j]])   
def Add_Block():
    for i in range(4):
        x = block_coor[2*i] + location[0]
        y = block_coor[2*i+1] + location[1]
        graphic[x][y] = blocktype+1
def Del_Block():
    for i in range(4):
        x = block_coor[2*i] + location[0]
        y = block_coor[2*i+1] + location[1]
        graphic[x][y] = 0     
def Check_Boundary():
    for i in range(4):
        x = block_coor[2*i] + location[0] 
        y = block_coor[2*i+1] + location[1]
        
        if ( y < 0  or y >9 ):
            return False
        if x > 19:
            return False
        if graphic[x][y] != 0 :
            return False
        
    return True
            
root = Tk()

canvas = Canvas(root, width = 300, height = 600, bg = 'green')
canvas.pack()

lbl = Label(root,text="Score : 0")
lbl.pack()

rectangles = [[ canvas.create_rectangle(c*P_SIZE,r*P_SIZE,(c+1)*P_SIZE,(r+1)*P_SIZE) for c in range (F_WIDTH)] 
                for r in range(F_HEIGHT)]

IsRunning = True 

location = [ 1, 5]

blocktype = random.randint(0,6)
spinvalue = random.randint(0,3)

points = 0
newpoints = 0

lbl['text'] = "Score : ", points

block_coor = AllCoor[blocktype][spinvalue]
Add_Block()
Show_Graphic() 

def Move(x,y):
    Del_Block()
    location[0] = location[0] + x
    location[1] = location[1] + y
    if Check_Boundary() == True:
        Add_Block()
        Show_Graphic()
    else:
        location[0] = location[0] - x
        location[1] = location[1] - y
        Add_Block()
        Show_Graphic()
        return False
    return True
def Spin_Block() :
    global spinvalue
    global block_coor
    Del_Block()
    spinvalue = (spinvalue + 1) % 4
    block_coor = AllCoor[blocktype][spinvalue]
    
    if Check_Boundary() == True :
        Add_Block()
        Show_Graphic()
    else :
        spinvalue = (spinvalue + 3) % 4
        Add_Block()
        Show_Graphic()
def New_Block() :
    global blocktype, spinvalue, block_coor, location, points
    
    blocktype = random.randint(0,6)
    spinvalue = random.randint(0,3)
    location = [ 1, 5]
    block_coor = AllCoor[blocktype][spinvalue]
def Check_line():
    global points, newpoints
    i = F_HEIGHT - 1
    while 0 < i < F_HEIGHT:
        count = 0
        for j in range(F_WIDTH):
            if graphic[i][j] == 0:
                count += 1
        if count == 0:
            for j in range(F_WIDTH):
                graphic[i][j] = 0
            for k in reversed(range(i+1)):
                for j in range(F_WIDTH):
                    graphic[k][j] = graphic[k-1][j]
            for j in range(F_WIDTH):
                graphic[0][j] = 0
            newpoints += 1000
            i += 1
        i -= 1
    if newpoints != points:
        points = newpoints
    lbl['text'] = "Score : ", points
def Fall_Block():
    Del_Block()
    if Move(1,0) == False:
        Check_line()
        New_Block()
        if Check_Boundary() == False:
            print("\n game over")
            print(" final score : ", points)
            return
    root.after(500, Fall_Block)
def Drop_Block():
    while Move(1,0) == True:
        pass 

Fall_Block()

canvas.focus_set()    
canvas.bind("<Left>",lambda _: Move(0,-1))
canvas.bind("<Right>",lambda _: Move(0,1))
canvas.bind("<Up>", lambda _: Spin_Block()) 
canvas.bind("<Down>",lambda _: Move(1,0))
canvas.bind("<space>", lambda _: Drop_Block())
root.mainloop()
IsRunning = False 
