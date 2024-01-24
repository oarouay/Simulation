import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import messagebox
import tkinter.font as TkFont

class card():
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace']
        
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck=[]
        e={
            "rank":"",
            "suit":"",
            "color":""
        }
        for i in self.suits:
            for j in self.ranks:
                e={}
                e['rank']=j
                e['suit']=i
                if (i in ['Hearts', 'Diamonds']):
                    e['color']="red"
                else:
                    e['color']="black"
                self.deck.append(e)
    def shuffle(self):
        nbr=[]
        deck_shuffled=[]
        while True:
            nb= random.randint(0, 51)
            if not(nb in nbr):
                deck_shuffled.append(self.deck[nb])
                nbr.append(nb)
            if(len(nbr)==52):
                break
        self.deck=deck_shuffled
    def draw(self):
        if(len(self.deck)>0):
            return self.deck.pop()
        else:
            self.__init__()
            self.shuffle() 

class sahara:
    def __init__(self):
        self.card = card()
        self.card.shuffle()

    def play_game(self):
        drawn_card = self.card.draw()
        if drawn_card['rank'] == 'Ace':
            return 10
        else:
            return 0 
class tunisian_twins:
    def __init__(self):
        self.card = card()
        self.card.shuffle()
        self.card1 = card()
        self.card.shuffle()
    def play_game(self):
        drawn_card = self.card.draw()
        drawn_card1 = self.card1.draw()
        if drawn_card['rank']== drawn_card1['rank'] and drawn_card['suit']== drawn_card1['suit'] and drawn_card['color']== drawn_card1['color']:
            return 50
        else:
            return 0
class medina_biggie:
    def __init__(self):
        self.card = card()
        self.card.shuffle()

    def play_game(self):
        drawn_card = self.card.draw()
        drawn_card1 = self.card.draw()
        if self.card.ranks.index(drawn_card['rank']) < self.card.ranks.index(drawn_card1['rank']):
            return 2
        else:
            return 0
class desert_hearts:
    def __init__(self):
        self.card = card()
        self.card.shuffle()

    def play_game(self):
        s=0
        drawn_card = self.card.draw()
        drawn_card1 = self.card.draw()
        drawn_card2 = self.card.draw()
        q=['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        if(drawn_card['suit']=='Hearts'):
            s=s+1
        if(drawn_card1['suit']=='Hearts'):
            s=s+1
        if(drawn_card2['suit']=='Hearts'):
            s=s+1
        return s 
class oasis_runny:
    def __init__(self):
        self.card = card()
        self.card.shuffle()
    
    def play_game(self):
        t = []
        for i in range(5):
            t.append(self.card.draw())
        for i in range(3):  # Loop through the first three cards
            if (self.card.ranks.index(t[i + 1]['rank']) == self.card.ranks.index(t[i]['rank']) + 1 and
                    self.card.ranks.index(t[i + 2]['rank']) == self.card.ranks.index(t[i]['rank']) + 2):
                return 5
        return 0
class chibani:
    def __init__(self):
        self.card = card()
        self.card.shuffle()

    def play_game(self):
        s=0
        drawn_card = self.card.draw()
        drawn_card1 = self.card.draw()
        drawn_card2 = self.card.draw()
        drawn_card3 = self.card.draw()
        if(drawn_card['rank']=='King'):
            s=s+1
        if(drawn_card1['rank']=='King'):
            s=s+1
        if(drawn_card2['rank']=='King'):
            s=s+1
        if(drawn_card3['rank']=='King'):
            s=s+1
        if s>1 :
            return 50
        else:
            return 0
def ouss(x):
    a={}
    s1,s2,s3,s4,s5,s6=0,0,0,0,0,0
    for i in range(int(x)):
        c=sahara()
        s1=s1+c.play_game()
        c=tunisian_twins()
        s2=s2+c.play_game()
        c=medina_biggie()
        s3=s3+c.play_game()
        c=desert_hearts()
        s4=s4+c.play_game()
        c=oasis_runny()
        s5=s5+c.play_game()
        c=chibani()
        s6=s6+c.play_game()
    x=int(x)
    a['sahara']=float(s1/x)
    a['tunisian_twins']=float(s2/x)
    a['medina_biggie']=float(s3/x)
    a['desert_hearts']=float(s4/x)
    a['oasis_runny']=float(s5/x)
    a['chibani']=float(s6/x)

    return a
def chart():
    ax1.clear() 
    a=ouss(sim.get())
    refill(a)
    plt.xticks(range(len(a)), a.keys(), rotation=15)
    random.seed(int(seed.get()))
    ax1.set_title("Top Money Losers: Game Performance Report")
    ax1.set_xlabel("Games")
    ax1.set_ylabel("Wins")
    global y
    y = a.values()
    ax1.bar(a.keys(), y)
    canvas1.draw()
    max=0
    m=""
    for key, value in a.items():
        if(value>max):
            max=value
            m=key


    messagebox.showinfo("Best game", m)


"""interface"""


def fill():
    my_game['columns'] = ('Game Name', 'Amount of Money Earned', 'Probability of Winning')
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Game Name",anchor=CENTER, width=150)
    my_game.column("Amount of Money Earned",anchor=CENTER,width=150)
    my_game.column("Probability of Winning",anchor=CENTER,width=150)

    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("Game Name",text="Game Name",anchor=CENTER)
    my_game.heading("Amount of Money Earned",text="Amount of Money Earned",anchor=CENTER)
    my_game.heading("Probability of Winning",text="Probability of Winning",anchor=CENTER)
    my_game.insert(parent='',index='end',iid=0,text='',
    values=('sahara','0','0'))
    my_game.insert(parent='',index='end',iid=1,text='',
    values=('tunisian_twins','0','0'))
    my_game.insert(parent='',index='end',iid=2,text='',
    values=('medina_biggie','0','0'))
    my_game.insert(parent='',index='end',iid=3,text='',
    values=('desert_hearts','0','0'))
    my_game.insert(parent='',index='end',iid=4,text='',
    values=('oasis_runny','0','0'))
    my_game.insert(parent='',index='end',iid=5,text='',
    values=('chibani','0','0'))
def modify_treeview(game_name, new_wins, new_simulation_results):
    for item in my_game.get_children():
        values = my_game.item(item, 'values')
        if values[0] == game_name:
            my_game.item(item, values=(game_name, new_wins, new_simulation_results))
    my_game.update()

def refill(a):

    modify_treeview('sahara',int(a['sahara']*int(sim.get())),a['sahara'])
    modify_treeview('tunisian_twins',int(a['tunisian_twins']*int(sim.get())),a['tunisian_twins'])
    modify_treeview('medina_biggie',int(a['medina_biggie']*int(sim.get())),a['medina_biggie'])
    modify_treeview('desert_hearts',int(a['desert_hearts']*int(sim.get())),a['desert_hearts'])
    modify_treeview('oasis_runny',int(a['oasis_runny']*int(sim.get())),a['oasis_runny'])
    modify_treeview('chibani',int(a['chibani']*int(sim.get())),a['chibani'])
a={}
plt.rcParams["axes.prop_cycle"] = plt.cycler(
color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])
root = tk.Tk()
root.title("Dashboard")
root.state('zoomed')
fig1, ax1 = plt.subplots()
y= a.values()
ax1.bar(a.keys(), y)
ax1.set_title("Top Money Losers: Game Performance Report")
ax1.set_xlabel("Games")
ax1.set_ylabel("Wins")
side_frame = tk.Frame(root, bg="#4C2A85")
side_frame.pack(side="left", fill="y")
font = TkFont.Font(family="Casino 3D Filled Marquee", size=80)
font1 = TkFont.Font(family="BlackChancery", size=20)
label = tk.Label(side_frame, text="Casino", bg="#4C2A85", fg="#FFF",font=font)
label.pack(pady=50, padx=20)
seed = tk.Entry(side_frame)
label1 = tk.Label(side_frame, text="number of simulation :", bg="#4C2A85", fg="#FFF",font=font1)
label1.pack(pady=10, padx=20)
sim = tk.Entry(side_frame)
sim.pack(pady=20, padx=20)
label2 = tk.Label(side_frame, text="seed :", bg="#4C2A85", fg="#FFF", font=font1)
label2.pack(pady=10, padx=20)
charts_frame = tk.Frame(root)
charts_frame.pack()
upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)
label3 = tk.Label(upper_frame, text="Monte Carlo simulation :",  font=font1)
label3.pack(pady=10, padx=20)
table_frame = tk.Frame(root)
table_frame.pack()

lower_frame = tk.Frame(table_frame)
lower_frame.pack(fill="both", expand=True)
label4 = tk.Label(lower_frame, text="Results :", fg="#000", font=font1)
label4.pack(pady=10, padx=20)
#################################################################table

my_game = ttk.Treeview(table_frame)
my_game.pack()

###################################################################3abi
fill()

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
button = tk.Button(side_frame, text="submit",font=font1,command=chart)
seed.pack(pady=20, padx=20)
button.pack(pady=20, padx=20)
root.mainloop()

