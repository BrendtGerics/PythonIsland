from tkinter import *
from tkinter import messagebox


class Squadron(object):
    def __init__(self,type,full,inj,loc):
        self.type = type
        self.full = full
        self.inj = inj
        self.loc = loc

    def update_hp(self,n):
        self.inj += n
        self.full -= n

    def move(self,new_loc):
        self.loc = new_loc

class Person(object):
    def __init__(self, name, res,army,ap,structs, builds,test):
        self.name = name
        self.test = IntVar()
        temp_set_map = {
            "food": IntVar(),
            "wood": IntVar(),
            "stone": IntVar(),
            "metal": IntVar(),
            "gold": IntVar()
        }
        temp_set_map["food"].set(10)
        temp_set_map["wood"].set(5)
        temp_set_map["stone"].set(5)
        temp_set_map["metal"].set(5)
        temp_set_map["gold"].set(5)

        self.res = temp_set_map
        self.army = army = {}
        self.ap = ap
        temp_struct = {
            "mine": IntVar(),
            "quarry": IntVar(),
            "mill": IntVar(),
            "farm": IntVar()
        }
        temp_struct["mine"].set(0)
        temp_struct["quarry"].set(0)
        temp_struct["mill"].set(0)
        temp_struct["farm"].set(0)
        temp_builds = {
            "granary": [0,0,0],
            "trading post": [0,0],
            "keep": [1,0],
            "library": 0,
            "port": [0,0]
        }
        self.structs = temp_struct
        self.builds = temp_builds

    def hmm(self,res,val):
        self.set_map[res].set(val)

    def use_ap(self):
        self.ap -= 1

    def update_res(self,resource,n):
        self.res[resource] += n
    def check_no_move(self):
        if (self.use_ap() == 0):
            return True
        else:
            return False




window = Tk()



window.title("Welcome to Island Conquest app")

window.geometry('950x550')
lbl = Label(window,text="Food",padx=True)
lbl.grid(column=1,row=0)
lbl = Label(window,text="Wood",padx=True)
lbl.grid(column=2,row=0)
lbl = Label(window,text="Stone",padx=True)
lbl.grid(column=3,row=0)
lbl = Label(window,text="Metal",padx=True)
lbl.grid(column=4,row=0)
lbl = Label(window,text="Gold",padx=True)
lbl.grid(column=5,row=0)
lbl = Label(window,text="Farms",padx=True)
lbl.grid(column=6,row=0)
lbl = Label(window,text="Mills",padx=True)
lbl.grid(column=7,row=0)
lbl = Label(window,text="Mines",padx=True)
lbl.grid(column=8,row=0)
lbl = Label(window,text="Quarries",padx=True)
lbl.grid(column=9,row=0)

lbl = Label(window, text="Archduke Brendt",padx=True,fg="blue",font="Century 16 bold",bg="light blue", anchor = "w", width = 15)
lbl.grid(column=0, row=1,sticky=W)
lbl = Label(window, text="Baroness Caitlin",padx=True,fg="DarkOrange2",font="Century 16 bold", bg = "yellow", anchor = "w", width = 15)
lbl.grid(column=0, row=2,sticky=W)
lbl = Label(window, text="Count Martin",padx=True,fg="red",font="Century 16 bold", bg = "pink", anchor = "w", width = 15)
lbl.grid(column=0, row=3,sticky=W)
lbl = Label(window, text="Prince Joel",padx=True,fg="green",font="Century 16 bold",bg="light green", anchor = "w", width = 15)
lbl.grid(column=0, row=4)

arch = Person("Brendt",{},{},5,{},{},5)
baron = Person("Caitlin",{},{},5,{},{},5)
count = Person("Martin",{},{},5,{},{},5)
prince = Person("Joel",{},{},5,{},{},5)

Players = {
    "Arch": arch,
    "Baron": baron,
    "Count": count,
    "Prince": prince
}

def display(per):
    for xx in per.set_map:
        print(xx.get())

printy = Button(window, text="Print", command = lambda : print(arch.res["food"].get(),arch.res["metal"].get()))
printy.grid(column=0,row = 0)





arch_spin_food = Spinbox(window, from_=0, to=1000, width=5, textvariable=arch.res["food"])
arch_spin_food.grid(column=1,row=1)
arch_spin_wood = Spinbox(window,from_=0, to=1000, width = 5, textvariable=arch.res["wood"])
arch_spin_wood.grid(column = 2, row =1)
arch_spin_stone = Spinbox(window,from_=0, to=1000, width = 5, textvariable=arch.res["stone"])
arch_spin_stone.grid(column = 3, row =1)
arch_spin_metal = Spinbox(window,from_=0, to=1000, width = 5, textvariable=arch.res["metal"])
arch_spin_metal.grid(column = 4, row =1)
arch_spin_gold = Spinbox(window,from_=0, to=1000, width = 5, textvariable=arch.res["gold"])
arch_spin_gold.grid(column = 5, row =1)
arch_spin_farms = Spinbox(window,from_=0,to=1000, width = 5, textvariable=arch.structs["farm"])
arch_spin_farms.grid(column=6, row = 1)
arch_spin_mills = Spinbox(window,from_=0,to=1000, width = 5, textvariable=arch.structs["mill"])
arch_spin_mills.grid(column=7, row = 1)
arch_spin_mines = Spinbox(window,from_=0,to=1000, width = 5, textvariable=arch.structs["mine"])
arch_spin_mines.grid(column=8, row = 1)
arch_spin_quarries = Spinbox(window,from_=0,to=1000, width = 5, textvariable=arch.structs["quarry"])
arch_spin_quarries.grid(column=9, row = 1)



baron_spin_food = Spinbox(window, from_=0, to=1000, width=5, textvariable=baron.res["food"])
baron_spin_food.grid(column=1,row=2)
baron_spin_wood = Spinbox(window,from_=0, to=1000, width = 5, textvariable=baron.res["wood"])
baron_spin_wood.grid(column = 2, row =2)
baron_spin_stone = Spinbox(window,from_=0, to=1000, width = 5, textvariable=baron.res["stone"])
baron_spin_stone.grid(column = 3, row =2)
baron_spin_metal = Spinbox(window,from_=0, to=1000, width = 5, textvariable=baron.res["metal"])
baron_spin_metal.grid(column = 4, row =2)
baron_spin_gold = Spinbox(window,from_=0, to=1000, width = 5, textvariable=baron.res["gold"])
baron_spin_gold.grid(column = 5, row =2)
baron_spin_farms = Spinbox(window,from_=0,to=1000, width = 5, textvariable=baron.structs["farm"])
baron_spin_farms.grid(column=6, row = 2)
baron_spin_mills = Spinbox(window,from_=0,to=1000, width = 5, textvariable=baron.structs["mill"])
baron_spin_mills.grid(column=7, row = 2)
baron_spin_mines = Spinbox(window,from_=0,to=1000, width = 5, textvariable=baron.structs["mine"])
baron_spin_mines.grid(column=8, row = 2)
baron_spin_quarries = Spinbox(window,from_=0,to=1000, width = 5, textvariable=baron.structs["quarry"])
baron_spin_quarries.grid(column=9, row = 2)

count_spin_food = Spinbox(window, from_=0, to=1000, width=5, textvariable=count.res["food"])
count_spin_food.grid(column=1,row=3)
count_spin_wood = Spinbox(window,from_=0, to=1000, width = 5, textvariable=count.res["wood"])
count_spin_wood.grid(column = 2, row =3)
count_spin_stone = Spinbox(window,from_=0, to=1000, width = 5, textvariable=count.res["stone"])
count_spin_stone.grid(column = 3, row =3)
count_spin_metal = Spinbox(window,from_=0, to=1000, width = 5, textvariable=count.res["metal"])
count_spin_metal.grid(column = 4, row =3)
count_spin_gold = Spinbox(window,from_=0, to=1000, width = 5, textvariable=count.res["gold"])
count_spin_gold.grid(column = 5, row =3)
count_spin_farms = Spinbox(window,from_=0,to=1000, width = 5, textvariable=count.structs["farm"])
count_spin_farms.grid(column=6, row = 3)
count_spin_mills = Spinbox(window,from_=0,to=1000, width = 5, textvariable=count.structs["mill"])
count_spin_mills.grid(column=7, row = 3)
count_spin_mines = Spinbox(window,from_=0,to=1000, width = 5, textvariable=count.structs["mine"])
count_spin_mines.grid(column=8, row = 3)
count_spin_quarries = Spinbox(window,from_=0,to=1000, width = 5, textvariable=count.structs["quarry"])
count_spin_quarries.grid(column=9, row = 3)

prince_spin_food = Spinbox(window, from_=0, to=1000, width=5, textvariable=prince.res["food"])
prince_spin_food.grid(column=1,row=4)
prince_spin_wood = Spinbox(window,from_=0, to=1000, width = 5, textvariable=prince.res["wood"])
prince_spin_wood.grid(column = 2, row =4)
prince_spin_stone = Spinbox(window,from_=0, to=1000, width = 5, textvariable=prince.res["stone"])
prince_spin_stone.grid(column = 3, row =4)
prince_spin_metal = Spinbox(window,from_=0, to=1000, width = 5, textvariable=prince.res["metal"])
prince_spin_metal.grid(column = 4, row =4)
prince_spin_gold = Spinbox(window,from_=0, to=1000, width = 5, textvariable=prince.res["gold"])
prince_spin_gold.grid(column = 5, row =4)
prince_spin_farms = Spinbox(window,from_=0,to=1000, width = 5, textvariable=prince.structs["farm"])
prince_spin_farms.grid(column=6, row = 4)
prince_spin_mills = Spinbox(window,from_=0,to=1000, width = 5, textvariable=prince.structs["mill"])
prince_spin_mills.grid(column=7, row = 4)
prince_spin_mines = Spinbox(window,from_=0,to=1000, width = 5, textvariable=prince.structs["mine"])
prince_spin_mines.grid(column=8, row = 4)
prince_spin_quarries = Spinbox(window,from_=0,to=1000, width = 5, textvariable=prince.structs["quarry"])
prince_spin_quarries.grid(column=9, row = 4)

#arch_txt = Entry(window, width=5)
#arch_txt.grid(column=1, row=0)


def show_turn(person):
    turn_label = Label(window,text = person.res["wood"].get())
    turn_label.grid(column = 1, row = 1)

turn = Button(window,text = "Take_turn", command = lambda : show_turn(arch))
turn.grid(column = 12,row = 1)




window.mainloop()

