from tkinter import *
import random
from tkinter.tix import Y_REGION
import random  

my_list = []  
win_list = []


def generate_win_lottery_list():
    global win_list
    for i in range(6):
        num = random.randint(1, 45)
        win_list.append(num)


def check_lottery_win():
    global my_list, win_list, points
    idx = 0
    for i in my_list:
        if (i in win_list):
            idx += 1
    print(idx)
    if idx >= 5:
        lottery_hit_label["text"] = "1등이다 1등!!"
        points *= 10
    lottery_hit_label["text"] = str(idx) + '''개 맞았다
    이번 생은 글렀나보다
    또 사보자'''



def print_game_over():
    game_over_label["text"] = '''
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼'''


def generate_random_number():
    global my_list  # 전역 변수를 사용하기 위해 선언

    while True:
        number = random.randint(1, 45)  # 1부터 45 사이의 번호 랜덤 선택

        if number not in my_list:
            my_list.append(number)  # 리스트에 번호 추가
            break  # 번호가 중복되지 않으면 루프 종료
    lottery_numbers["text"] = my_list


def check_list():
    global pause_flag
    global my_list  # 전역 변수를 사용하기 위해 선언

    if len(my_list) == 6 and pause_flag == 0:  # 리스트에 6개의 번호가 들어있는지 확인
        check_lottery_win()
        # print("리스트가 다 찼습니다.")
        Prev_lottery_label["text"] += str(my_list) + str('\n')
        pause_flag = 1
    if len(my_list) == 6 and pause_flag == 1:
        my_list = []  # 리스트 초기화
        # print("리스트가 초기화되었습니다.")
        generate_random_number()
        pause_flag = 0

    # 함수 1 호출하여 새로운 번호 뽑기


F_WIDTH = 10
F_HEIGHT = 20
P_SIZE = 30
COLORS = ['gray', 'lightgreen', 'pink', 'orange', 'blue', 'purple', 'red', 'yellow', 'cyan', 'black', 'white']

AllCoor = [
    [[-1, 0, 0, 0, 1, 0, 2, 0], [0, -1, 0, 0, 0, 1, 0, 2], [-1, 0, 0, 0, 1, 0, 2, 0], [0, -1, 0, 0, 0, 1, 0, 2]],
    [[-1, -1, 0, -1, 0, 0, 0, 1], [-1, 0, 0, 0, 1, 0, 1, -1], [0, -1, 0, 0, 0, 1, 1, 1], [-1, 0, -1, 1, 0, 0, 1, 0]],
    [[0, -1, 0, 0, 0, 1, -1, 1], [-1, -1, -1, 0, 0, 0, 1, 0], [1, -1, 0, -1, 0, 0, 0, 1], [-1, 0, 0, 0, 1, 0, 1, 1]],
    [[-1, 0, 0, 0, 0, 1, 1, 1], [0, -1, 0, 0, -1, 0, -1, 1], [-1, 0, 0, 0, 0, 1, 1, 1], [0, -1, 0, 0, -1, 0, -1, 1]],
    [[0, 0, 0, 1, -1, 1, 1, 0], [-1, -1, -1, 0, 0, 0, 0, 1], [0, 0, 0, 1, -1, 1, 1, 0], [-1, -1, -1, 0, 0, 0, 0, 1]],
    [[0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1]],
    [[0, -1, 0, 0, -1, 0, 0, 1], [0, 0, -1, 0, 0, 1, 1, 0], [0, -1, 0, 0, 0, 1, 1, 0], [0, -1, 0, 0, -1, 0, 1, 0]]
]

graphic = [[0 for c in range(F_WIDTH)] for r in range(F_HEIGHT)]


def Show_Graphic():
    global canvas
    for i in range(F_HEIGHT):
        for j in range(F_WIDTH):
            canvas.itemconfig(rectangles[i][j], fill=COLORS[graphic[i][j]])


def Add_Block():
    for i in range(4):
        x = block_coor[2 * i] + location[0]
        y = block_coor[2 * i + 1] + location[1]
        graphic[x][y] = blocktype + 1


def Del_Block():
    for i in range(4):
        x = block_coor[2 * i] + location[0]
        y = block_coor[2 * i + 1] + location[1]
        graphic[x][y] = 0


def Check_Boundary():
    global boundary_overflow
    for i in range(4):
        x = block_coor[2 * i] + location[0]
        y = block_coor[2 * i + 1] + location[1]

        if (y < 0 or y > 9):
            boundary_overflow = 1
            return False
        if (x > 19 or x < 0):
            boundary_overflow = 1
            return False
        if graphic[x][y] != 0:
            boundary_overflow = 0
            return False

    return True


root = Tk()
root.title("life is tetris")

canvas = Canvas(root, width=300, height=600, bg='green')
canvas.grid(row=0, column=0)
label_canvas = Canvas(root, width=500, height=600)
label_canvas.grid(row=0, column=1)
label_canvas.pack_propagate(0)

fever_label = Label(label_canvas, font=('맑은 고딕', 14), fg='red', wraplength=400)
fever_label.pack()
score_label = Label(label_canvas, text="Score : 0")
score_label.pack()
lottery_label1 = Label(label_canvas, text="로또로 인생 한 번 펴 보자")
lottery_label1.pack()
Prev_lottery_label = Label(label_canvas, text="")
Prev_lottery_label.pack()
lottery_hit_label = Label(label_canvas)
lottery_hit_label.pack()
lottery_label2 = Label(label_canvas, text="이번 로또 번호는...")
lottery_label2.pack()
lottery_numbers = Label(label_canvas)
lottery_numbers.pack()
game_over_label = Label(label_canvas, text="", font=('Courier', 12))
game_over_label.place(x=25, y=50)
#game_over_label.pack()


rectangles = [
    [canvas.create_rectangle(c * P_SIZE, r * P_SIZE, (c + 1) * P_SIZE, (r + 1) * P_SIZE) for c in range(F_WIDTH)]
    for r in range(F_HEIGHT)]

IsRunning = True

location = [16, 5]

blocktype = random.randint(0, 6)
spinvalue = random.randint(0, 3)

points = 0
newpoints = 0

boundary_overflow = 0
interval = 500
pause_flag = 0
mode0_count = 0
mode1_count = 0
mode2_count = 0

score_label['text'] = "Score : " + str(points)

block_coor = AllCoor[blocktype][spinvalue]
Add_Block()
Show_Graphic()
generate_win_lottery_list()


def Move(x, y):
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


def Spin_Block():
    global spinvalue
    global block_coor
    Del_Block()
    spinvalue = (spinvalue + 1) % 4
    block_coor = AllCoor[blocktype][spinvalue]

    if Check_Boundary() == True:
        Add_Block()
        Show_Graphic()
    else:
        for dy in [-1, 1]:
            location[1] += dy
            if Check_Boundary() and boundary_overflow == 1:
                Add_Block()
                Show_Graphic()
                return
            location[1] -= dy
        spinvalue = (spinvalue + 3) % 4
        block_coor = AllCoor[blocktype][spinvalue]
        Add_Block()
        Show_Graphic()


def randomInterval(mode):
    global interval, mode0_count, mode1_count, mode2_count
    if mode == 0:
        fever_label["text"] = "세상은 때론 너의 속도보다 빠르게 다가올 때도 있지~"
        interval = 100
        mode0_count += 1
    elif mode == 1:
        fever_label["text"] = "너무 빠르게 가려고 하는 것보다 주변을 둘러보는 게 좋을 수도 있어"
        interval = 800
        canvas.bind("<space>", lambda _: None)
        canvas.bind("<Up>", lambda _: None)

        mode1_count += 1



def setInterval():
    global interval
    if points >= 5000:
        interval = 400
    elif points >= 10000:
        interval = 300
    elif points >= 15000:
        interval = 200
    elif points >= 20000:
        interval = 150
    elif points >= 25000:
        interval = 100


def normalizeInterval():
    global interval, mode0_count, mode1_count, mode2_count
    if mode0_count > 3:
        fever_label["text"] = ""
        setInterval()
        mode0_count = 0
    if mode1_count > 1:
        fever_label["text"] = ""
        canvas.bind("<space>", lambda _: Drop_Block())
        canvas.bind("<Up>", lambda _: Move(-1, 0))
        mode1_count = 0
        setInterval()



def New_Block():
    global blocktype, spinvalue, block_coor, location, points, interval, mode0_count, mode1_count, mode2_count

    blocktype = random.randint(0, 6)
    spinvalue = random.randint(0, 3)
    location = [16, 5]
    block_coor = AllCoor[blocktype][spinvalue]

    setInterval()

    mode_count = mode0_count + mode1_count + mode2_count
    if mode_count == 0 and points >= 2000:
        mode = random.randint(0, 7)
        if mode <= 1:
            randomInterval(mode)
    elif mode_count > 0 and points >= 2000:
        if 0 < mode0_count <= 3:
            randomInterval(0)
            normalizeInterval()
        elif 0 < mode1_count <= 1:
            randomInterval(1)
            normalizeInterval()





def Check_line():
    global points, newpoints
    i = 0
    while 0 <= i < F_HEIGHT:
        count = 0
        for j in range(F_WIDTH):
            if graphic[i][j] == 0:
                count += 1
        if count == 0:
            for j in range(F_WIDTH):
                graphic[i][j] = 0
            for k in (range(i + 1, F_HEIGHT - 1)):
                for j in (range(F_WIDTH)):
                    graphic[k - 1][j] = graphic[k][j]
            for j in range(F_WIDTH):
                graphic[F_HEIGHT-1][j] = 0
            newpoints += 1000
            i -= 1
            generate_random_number()
            check_list()
        i += 1
    if newpoints != points:
        points = newpoints
    score_label['text'] = "Score : " + str(points)

    if (points // 10000) % 2:
        canvas.bind("<Left>", lambda _: Move(0, 1))
        canvas.bind("<Right>", lambda _: Move(0, -1))
    else:
        canvas.bind("<Left>", lambda _: Move(0, -1))
        canvas.bind("<Right>", lambda _: Move(0, 1))


def Fall_Block():
    global interval
    Del_Block()
    if Move(-1, 0) == False:
        Check_line()
        New_Block()
        if Check_Boundary() == False:

            print_game_over()

            return
    root.after(interval, Fall_Block)


def Drop_Block():
    while Move(-1, 0) == True:
        pass


Fall_Block()

canvas.focus_set()
canvas.bind("<Left>", lambda _: Move(0, -1))
canvas.bind("<Right>", lambda _: Move(0, 1))
canvas.bind("<Up>", lambda _: Move(-1, 0))
canvas.bind("<Down>", lambda _: Spin_Block())
canvas.bind("<space>", lambda _: Drop_Block())
root.mainloop()
IsRunning = False
