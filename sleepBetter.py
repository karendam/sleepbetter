from tkinter import *
import tkinter.scrolledtext as tkst
import tkinter.filedialog
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter as tk
import pygame
from tkinter import messagebox
import webbrowser

root = Tk()
root.configure(background="#A8BBD9")
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=11)
root.title("Sleep Better")

top = Toplevel()
top.attributes('-topmost', 'true')
top.title("Timer")


def save():
    min = open("test.txt", "w")
    min.write(input.get())
    min.close()
    top.destroy()


def timer():
    milli= open("test.txt","r")
    long=milli.read()
    milliseconds=int(long)*60*1000
    return milliseconds


label= Label(top, text= "How many minutes of white noise do you want?")
label.pack()
input = Entry(top)
input.pack(padx=5)
top.configure(background="#A8BBD9")
label.configure(background="#A8BBD9")

b = Button(top, text="Save", command=save)
b.pack(pady=5)
b.configure(background="#A8BBD9")


def rainStart():


    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    sounda= pygame.mixer.Sound("rain-03.wav")
    milliseconds=timer()
    sounda.play(-1,milliseconds)
    print("timer done")


def paperStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundb= pygame.mixer.Sound("paper-rustle-5.wav")
    milliseconds=timer()
    soundb.play(-1,milliseconds)
    print("timer done")

def planeStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundc= pygame.mixer.Sound("airplane-interior-1.wav")
    milliseconds=timer()
    soundc.play(-1,milliseconds)
    print("timer done")

def fanStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundd= pygame.mixer.Sound("18-Fan-10min.wav")
    milliseconds=timer()
    soundd.play(-1,milliseconds)
    print("Timer Initiated")

def clockStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    sounde= pygame.mixer.Sound("clock-ticking-2.wav")
    milliseconds=timer()
    sounde.play(-1,milliseconds)
    print("Timer Initiated")

def trainStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundf= pygame.mixer.Sound("train-pass-by-02.wav")
    milliseconds=timer()
    soundf.play(-1,milliseconds)
    print("Timer Initiated")

def carStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundg= pygame.mixer.Sound("car-passing-1.wav")
    milliseconds=timer()
    soundg.play(-1,milliseconds)
    print("Timer Initiated")

def dropStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundh= pygame.mixer.Sound("water-dripping-1.wav")
    milliseconds=timer()
    soundh.play(-1,milliseconds)
    print("Timer Initiated")

def oceanStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundi= pygame.mixer.Sound("ocean-wave-2.wav")
    milliseconds=timer()
    soundi.play(-1,milliseconds)
    print("Timer Initiated")

def windStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundj= pygame.mixer.Sound("wind-1.wav")
    milliseconds=timer()
    soundj.play(-1,milliseconds)
    print("Timer Initiated")

def riverStart():
    milliseconds = 0
    pygame.init()
    pygame.mixer.init()
    soundk= pygame.mixer.Sound("river.wav")
    milliseconds=timer()
    soundk.play(-1,milliseconds)
    print("Timer Initiated")

fillFrame = Frame(root, width = 50, height = 50, bd= 1)
fillFrame.grid(row=0,column=1)
fillFrame.configure(background="#A8BBD9")

header = Label(root,text = "Sleep Better")
header.grid(row = 0, column = 5)


nb = ttk.Notebook(root, width = 500, height = 500)
nb.grid(row = 2, column  = 7)

f1 = tkst.ScrolledText(master = root, wrap = WORD, bg = "#F1F4FB")

nb.add(f1, text='page ')

# journalframe = Frame(root, width =300, height = 75, bd = 1)
# journalframe.grid(row = 1, column = 7)

# tabsframe = Frame(root, width =300, height = 75, bd = 1)
# tabsframe.grid(row = 1, column = 6)

delframe = Frame(root, width =300, height = 75, bd = 1)
delframe.grid(row = 1, column = 7)

JournalText= Label(delframe, text = "Journal")
JournalText.pack()

def createTabs(event):
    tabz = tkst.ScrolledText(master = root, wrap = WORD, bg = "azure")
    nb.add(tabz, text = 'page')

tabsbutton = Button(delframe, text = "Tabs +")
tabsbutton.bind("<Button-1 >", createTabs) #"<Button 1 >" = rightclick
tabsbutton.pack(side = LEFT)
 #"<Button 1 >" = rightclick
def deletetab(event):
     nb.forget(nb.select())

deltab = Button(delframe,text="Delete Current Tab")
deltab.bind("<Button-1>",deletetab)
deltab.pack(side = RIGHT)




RecFrame = Frame(root, width = 600, height = 350, bd= 1) #filler frame
RecFrame.grid(row=7,column=7, columnspan = 4)
RecText= Label(root, text = "Recommend Me Something!")
RecText.grid(row=7,column=7)
RecFrame.configure(background="#A8BBD9")

def create_window():
    main = tk.Toplevel()
    main.title("Recommended")
    main.geometry('275x300+0+0')
    main.configure(background="#A8BBD9")

    RecFrame = Frame(main, width = 100, height = 350, bd= 8, padx = 20)
    RecFrame.grid(row = 3, column = 1, padx = 50)
    head = Label(main,text = "Recommend Me Something!")
    head.grid(row = 2, column = 1)
    RecFrame.configure(background="#D1DFEC")

    def one(event):
        webbrowser.open_new(r"http://jingyi.me/starcollector/")
    def two(event):
        webbrowser.open_new(r"http://stressreliefpig.com/games/relaxing/fishing-girl.html")

    def three(event):
        webbrowser.open_new(r"https://www.silvergames.com/en/dokotonaku")

    def four(event):
        webbrowser.open_new(r"http://pusheen.com/")

    def five(event):
        webbrowser.open_new(r"https://www.instagram.com/mahoukarp/?hl=en")

    title = Label(RecFrame, text = "Cute Game")
    title.pack()

    link = Label(RecFrame, text = "(´ ∀ ` *)	", fg = "blue", cursor = "hand2")
    link.pack()
    link.bind("<Button-1>", one)

    titlea = Label(RecFrame, text = "Calming Game")
    titlea.pack()

    linkTwo = Label(RecFrame, text = "(°)#))<<", fg = "blue", cursor = "hand2")
    linkTwo.pack()
    linkTwo.bind("<Button-1>", two)

    titles = Label(RecFrame, text = "Weird Game")
    titles.pack()

    linkThree = Label(RecFrame, text = "＼(º □ º l|l)/", fg = "blue", cursor = "hand2")
    linkThree.pack()
    linkThree.bind("<Button-1>", three)

    titled = Label(RecFrame, text = "Cute Pictures")
    titled.pack()

    linkFour = Label(RecFrame, text = "(=^･ω･^=)", fg = "blue", cursor = "hand2")
    linkFour.pack()
    linkFour.bind("<Button-1>", four)

    titlef = Label(RecFrame, text = "Even more cute pictures")
    titlef.pack()

    linkFive = Label(RecFrame, text = "( ・∀・)・・・-------- ◎", fg = "blue", cursor = "hand2")
    linkFive.pack()
    linkFive.bind("<Button-1>", five)


bu = tk.Button(root, text="Recommend Me Something!", command=create_window)
bu.grid(row = 3, column = 7)

WidgetsFrame = Frame(root, width = 500, height = 650, bg = "#D1DFEC")
WidgetsFrame.grid(row = 2, column = 1)
WidgetsText = Label(WidgetsFrame, text = "White Noises: ")
WidgetsText.grid(row = 2, sticky = W, padx = 20)


##########

whiteNoise = Label(WidgetsFrame, text = "Rain") # not showing up
whiteNoise.grid(row = 1, sticky = W, padx = 12)
White_Noise_button = Button(WidgetsFrame, command = rainStart)

filedname = PhotoImage(file = "raindrop.ppm")
White_Noise_button.config(image = filedname)
White_Noise_button.grid(row = 2, sticky = N+W, padx = 12)


#
PaperNoise = Label(WidgetsFrame, text = "Paper")
PaperNoise.grid(row = 3, sticky = W, padx = 12)
Paper_Noise_button = Button(WidgetsFrame,command=paperStart)

filesname = PhotoImage(file = "paper resizing.ppm")
Paper_Noise_button.config(image = filesname)
Paper_Noise_button.grid(row = 4, sticky = W, padx = 12)
#
#
#
PlaneNoise = Label(WidgetsFrame, text = "Plane")
PlaneNoise.grid(row = 5, sticky = W, padx = 12)
Plane_Noise_button = Button(WidgetsFrame, command=planeStart)
#
aaa = PhotoImage(file = "plane resizing.ppm")
Plane_Noise_button.config(image = aaa)
Plane_Noise_button.grid(row = 6, sticky = W, padx = 12)
# #
# #
#
FanNoise = Label(WidgetsFrame, text = "Fan")
FanNoise.grid(row = 7, sticky = W, padx = 12)
Fan_Noise_button = Button(WidgetsFrame,command=fanStart)
#
a = PhotoImage(file = "fan resizing.ppm")
Fan_Noise_button.config(image = a)
Fan_Noise_button.grid(row = 8, sticky = W, padx = 12)
#
#
#
ClockNoise = Label(WidgetsFrame, text = "Clock")
ClockNoise.grid(row = 1, column = 1, sticky = W, padx = 12)
Clock_Noise_button = Button(WidgetsFrame,command=clockStart)

aa = PhotoImage(file = "clock resizing.ppm")
Clock_Noise_button.config(image = aa)
Clock_Noise_button.grid(row = 2, column = 1, sticky = W+N, padx = 12)
# #
# #
#
TrainNoise = Label(WidgetsFrame, text = "Train")
TrainNoise.grid(row = 3, column = 1, sticky = W, padx = 12)
Train_Noise_button = Button(WidgetsFrame,command=trainStart)

filename = PhotoImage(file = "railroad resizing.ppm")
Train_Noise_button.config(image = filename)
Train_Noise_button.grid(row = 4, column = 1, sticky = W+N, padx = 12)
#
#
#
CarNoise = Label(WidgetsFrame, text = "Car")
CarNoise.grid(row = 5, column = 1, sticky = W, padx = 12)
Car_Noise_button = Button(WidgetsFrame, command=carStart)

filenames = PhotoImage(file = "car resizing.ppm")
Car_Noise_button.config(image = filenames)
Car_Noise_button.grid(row = 6, column = 1, sticky = W, padx = 12 )
#
#
#
DropNoise = Label(WidgetsFrame, text = "Drop")
DropNoise.grid(row = 7, column = 1, sticky = W, padx = 12)
Drop_Noise_button = Button(WidgetsFrame, command=dropStart)

aaaaa = PhotoImage(file = "drop resizing.ppm")
Drop_Noise_button.config(image = aaaaa)
Drop_Noise_button.grid(row = 8, column = 1, sticky = W, padx = 12 )
#
#
#
OceanNoise = Label(WidgetsFrame, text = "Ocean")
OceanNoise.grid(row = 1, column = 2, sticky = W, padx = 12)
Ocean_Noise_button = Button(WidgetsFrame, command=oceanStart)

aaaaab = PhotoImage(file = "waves resizing.ppm")
Ocean_Noise_button.config(image = aaaaab)
Ocean_Noise_button.grid(row = 2, column = 2, sticky = W, padx = 12)
#
#
#
WindNoise = Label(WidgetsFrame, text = "Wind")
WindNoise.grid(row = 3, column = 2, sticky = W, padx = 12)
Wind_Noise_button = Button(WidgetsFrame, command=windStart)

aaaaaa = PhotoImage(file = "wind.ppm")
Wind_Noise_button.config(image = aaaaaa)
Wind_Noise_button.grid(row = 4, column = 2, sticky = W, padx = 12)
#
#
#
RiverNoise = Label(WidgetsFrame, text = "River")
RiverNoise.grid(row = 5, column = 2, sticky = W, padx = 12)
River_Noise_button = Button(WidgetsFrame, command=riverStart)

aaaaabb = PhotoImage(file = "river resizing.ppm")
River_Noise_button.config(image = aaaaabb)
River_Noise_button.grid(row = 6, column = 2, sticky = W, padx = 12)

root.mainloop()
