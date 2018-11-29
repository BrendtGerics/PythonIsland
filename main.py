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
    turn = 1

    def __init__(self, name, res,army,ap,structs, builds, upgrades, sep,pat,mesgs):
        self.name = name
        self.mesgs = {}
        self.sep = BooleanVar()
        self.pat = BooleanVar()
        self.sep.set(False)
        self.pat.set(False)
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
        temp_struct["farm"].set(1)

        temp_upgrades = {
            "granary": IntVar(),
            "trading": IntVar(),
            "port": IntVar(),
            "wall": IntVar(),
            "library": BooleanVar(),
            "farm": BooleanVar(),
            "quarry": BooleanVar(),
            "mill": BooleanVar(),
            "mine": BooleanVar()
        }

        self.upgrades = temp_upgrades
        temp_builds = {
            "granary": IntVar(),
            "trading post": BooleanVar(),
            "keep": BooleanVar(),
            "library": BooleanVar(),
            "port": IntVar()
        }
        temp_builds["granary"].set(0)
        temp_builds["trading post"].set(False)
        temp_builds["keep"].set(True)
        temp_builds["library"].set(False)
        temp_builds["port"].set(False)

        self.structs = temp_struct
        self.builds = temp_builds

    def send_message(self,per):
        message = "Testing message"
        per.mesgs[self.name] = message

    def use_ap(self):
        self.ap -= 1

    def update_res(self,resource,n):
        self.res[resource] += n
    def check_no_move(self):
        if (self.use_ap() == 0):
            return True
        else:
            return False
    def take_turn(self):
        self.ap = 5
        if self.pat.get() == True:
            self.ap += 1
        if self.sep.get() == True:
            self.ap += 1

        f_level = 4
        if (self.upgrades["farm"].get() == False):
            self.res["food"].set(self.res["food"].get()+3*self.structs["farm"].get())
        if(self.upgrades["farm"].get() == True) :
            self.res["food"].set(self.res["food"].get() + f_level*self.structs["farm"].get())
        if (self.upgrades["mill"].get() == False):
            self.res["wood"].set(self.res["wood"].get()+2*self.structs["mill"].get())
        if (self.upgrades["mill"].get() == True) :
            self.res["wood"].set(self.res["wood"].get() + f_level*self.structs["mill"].get())
        if (self.upgrades["mine"].get() == False):
            self.res["metal"].set(self.res["metal"].get()+2*self.structs["mine"].get())
        if (self.upgrades["mill"].get() == True) :
            self.res["metal"].set(self.res["metal"].get() + f_level*self.structs["mine"].get())
        if (self.upgrades["quarry"].get() == False):
            self.res["stone"].set(self.res["stone"].get()+2*self.structs["quarry"].get())
        if (self.upgrades["quarry"].get() == True) :
            self.res["stone"].set(self.res["stone"].get() + f_level*self.structs["quarry"].get())

window = Tk()


#Title, nothing to say here.
window.title("Welcome to Island Conquest app")

#Set the window size
#window.geometry('1250x550')
window.state("zoomed")


# Resource Labels:
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
lbl = Label(window,text="Gran. Level",padx=True)
lbl.grid(column=10,row=0)
lbl = Label(window,text ="Wall Level", padx = True)
lbl.grid(column = 11, row = 0)
lbl = Label(window,text ="Trading Level", padx = True)
lbl.grid(column = 12, row = 0)
lbl = Label(window,text ="Port Level", padx = True)
lbl.grid(column = 13, row = 0)
lbl = Label(window,text ="Farm Upg", padx = True)
lbl.grid(column = 14, row = 0)
lbl = Label(window,text ="Mill Upg", padx = True)
lbl.grid(column = 15, row = 0)
lbl = Label(window,text ="Mine Upg", padx = True)
lbl.grid(column = 16, row = 0)
lbl = Label(window,text ="Quarry Upg", padx = True)
lbl.grid(column = 17, row = 0)


#Character Labels:
lbl = Label(window, text="Archduke Brendt",padx=True,fg="blue",font="Century 16 bold",bg="light blue", anchor = "w", width = 15)
lbl.grid(column=0, row=1,sticky=W)
lbl = Label(window, text="Baroness Caitlin",padx=True,fg="DarkOrange2",font="Century 16 bold", bg = "yellow", anchor = "w", width = 15)
lbl.grid(column=0, row=2,sticky=W)
lbl = Label(window, text="Count Martin",padx=True,fg="red",font="Century 16 bold", bg = "pink", anchor = "w", width = 15)
lbl.grid(column=0, row=3,sticky=W)
lbl = Label(window, text="Prince Joel",padx=True,fg="green",font="Century 16 bold",bg="light green", anchor = "w", width = 15)
lbl.grid(column=0, row=4)

arch = Person("Brendt",{},{},5,{},{},{}, False,False,{})
baron = Person("Caitlin",{},{},5,{},{},{}, False,False,{})
count = Person("Martin",{},{},5,{},{},{}, False,False,{})
prince = Person("Joel",{},{},5,{},{},{}, False,False,{})

arch.send_message(baron)

for xx in baron.mesgs:
    print(baron.mesgs[xx])



Players = {
    "Arch": arch,
    "Baron": baron,
    "Count": count,
    "Prince": prince
}

def display(per):
    lbl = Label(window,text = per.name)
    lbl.grid(column = 0, row = 18)
    lbl = Label(window, text="Send message:")
    lbl.grid(column = 0, row = 19)
    temp = StringVar()
    recip = Entry(window,textvariable=temp)
    recip.grid(column = 1,row =18)


    send_button = Button(window,text = "Send message", command = lambda : print("Hello"))


disp_button = Button(window,text = "display", command = lambda :display(arch))
disp_button.grid(column = 18,row = 1)





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
arch_spin_granary_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = arch.upgrades["granary"])
arch_spin_granary_upgrade.grid(column = 10, row = 1)
arch_spin_walls_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = arch.upgrades["wall"])
arch_spin_walls_upgrade.grid(column = 11, row = 1)
arch_spin_trading_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = arch.upgrades["trading"])
arch_spin_trading_upgrade.grid(column = 12, row = 1)
arch_spin_port_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = arch.upgrades["port"])
arch_spin_port_upgrade.grid(column = 13, row = 1)
arch_spin_farm_upgrade = Checkbutton(window, variable = arch.upgrades["farm"])
arch_spin_farm_upgrade.grid(column = 14, row = 1)
arch_spin_mill_upgrade = Checkbutton(window, variable = arch.upgrades["mill"])
arch_spin_mill_upgrade.grid(column = 15, row = 1)
arch_spin_mine_upgrade = Checkbutton(window, variable = arch.upgrades["mine"])
arch_spin_mine_upgrade.grid(column = 16, row = 1)
arch_spin_quarry_upgrade = Checkbutton(window, variable = arch.upgrades["quarry"])
arch_spin_quarry_upgrade.grid(column = 17, row = 1)



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
baron_spin_granary_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = baron.upgrades["granary"])
baron_spin_granary_upgrade.grid(column = 10, row = 2)
baron_spin_walls_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = baron.upgrades["wall"])
baron_spin_walls_upgrade.grid(column = 11, row = 2)
baron_spin_trading_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = baron.upgrades["trading"])
baron_spin_trading_upgrade.grid(column = 12, row = 2)
baron_spin_port_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = baron.upgrades["port"])
baron_spin_port_upgrade.grid(column = 13, row = 2)
baron_spin_farm_upgrade = Checkbutton(window, variable = baron.upgrades["farm"])
baron_spin_farm_upgrade.grid(column = 14, row = 2)
baron_spin_mill_upgrade = Checkbutton(window, variable = baron.upgrades["mill"])
baron_spin_mill_upgrade.grid(column = 15, row = 2)
baron_spin_mine_upgrade = Checkbutton(window, variable = baron.upgrades["mine"])
baron_spin_mine_upgrade.grid(column = 16, row = 2)
baron_spin_quarry_upgrade = Checkbutton(window, variable = baron.upgrades["quarry"])
baron_spin_quarry_upgrade.grid(column = 17, row = 2)


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
count_spin_granary_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = count.upgrades["granary"])
count_spin_granary_upgrade.grid(column = 10, row = 3)
count_spin_walls_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = count.upgrades["wall"])
count_spin_walls_upgrade.grid(column = 11, row = 3)
count_spin_trading_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = count.upgrades["trading"])
count_spin_trading_upgrade.grid(column = 12, row = 3)
count_spin_port_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = count.upgrades["port"])
count_spin_port_upgrade.grid(column = 13, row = 3)
count_spin_farm_upgrade = Checkbutton(window, variable = count.upgrades["farm"])
count_spin_farm_upgrade.grid(column = 14, row = 3)
count_spin_mill_upgrade = Checkbutton(window, variable = count.upgrades["mill"])
count_spin_mill_upgrade.grid(column = 15, row = 3)
count_spin_mine_upgrade = Checkbutton(window, variable = count.upgrades["mine"])
count_spin_mine_upgrade.grid(column = 16, row = 3)
count_spin_quarry_upgrade = Checkbutton(window, variable = count.upgrades["quarry"])
count_spin_quarry_upgrade.grid(column = 17, row = 3)


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
prince_spin_granary_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = prince.upgrades["granary"])
prince_spin_granary_upgrade.grid(column = 10, row = 4)
prince_spin_walls_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = prince.upgrades["wall"])
prince_spin_walls_upgrade.grid(column = 11, row = 4)
prince_spin_trading_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = prince.upgrades["trading"])
prince_spin_trading_upgrade.grid(column = 12, row = 4)
prince_spin_port_upgrade = Spinbox(window,from_=0, to = 3, width = 5, textvariable = prince.upgrades["port"])
prince_spin_port_upgrade.grid(column = 13, row = 4)
prince_spin_farm_upgrade = Checkbutton(window, variable = prince.upgrades["farm"])
prince_spin_farm_upgrade.grid(column = 14, row = 4)
prince_spin_mill_upgrade = Checkbutton(window, variable = prince.upgrades["mill"])
prince_spin_mill_upgrade.grid(column = 15, row = 4)
prince_spin_mine_upgrade = Checkbutton(window, variable = prince.upgrades["mine"])
prince_spin_mine_upgrade.grid(column = 16, row = 4)
prince_spin_quarry_upgrade = Checkbutton(window, variable = prince.upgrades["quarry"])
prince_spin_quarry_upgrade.grid(column = 17, row = 4)

#arch_txt = Entry(window, width=5)
#arch_txt.grid(column=1, row=0)


def show_turn(person):
    turn_label = Label(window,text = person.res["wood"].get())
    turn_label.grid(column = 1, row = 1)

#turn = Button(window,text = "Take_turn", command = lambda : show_turn(arch))
#turn.grid(column = 12,row = 1)




window.mainloop()

