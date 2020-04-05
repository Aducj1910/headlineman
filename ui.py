import random
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

military = 100 
entertainment = 100 
politics = 100
culture = 100 
economy = 100
rating = 0 
money = 15000

root = Tk()
root.title("Headline")
root.geometry('1440x720')
root.resizable(width=False, height=False)
button1 = tk.Button(root, text="Hello")

class Fakenews:

    def __init__(self, headline, mil, ent, pol, cul, eco, cost):
        self.headline = headline
        self.mil = mil
        self.ent = ent
        self.pol = pol
        self.cul = cul
        self.eco = eco
        self.cost = cost

    def implement(self):
        global military
        global entertainment
        global politics
        global culture
        global economy
        global money
        military = military + self.mil
        entertainment = entertainment + self.ent
        politics = politics + self.pol
        culture = culture + self.cul
        economy = economy + self.eco
        money = money - self.cost

        effect = abs(self.mil + self.ent + self.pol + self.cul + self.eco)
        n = random.randrange(6) 
        if n==0:
            moneyearned = effect*70
        elif n==1:
            moneyearned = effect*80
        elif n==2:
            moneyearned = effect*90
        elif n==3:
            moneyearned = effect*100
        elif n==4:
            moneyearned = effect*110
        elif n==5:
            moneyearned = effect*120

        money = money + moneyearned

class Realnews:

    def __init__(self, headline, mil, ent, pol, cul, eco):
        self.headline = headline
        self.mil = mil
        self.ent = ent
        self.pol = pol
        self.cul = cul
        self.eco = eco

    def implement(self):
        global military
        global entertainment
        global politics
        global culture
        global economy
        military = military + self.mil
        entertainment = entertainment + self.ent
        politics = politics + self.pol
        culture = culture + self.cul
        economy = economy + self.eco

goodrealnews = []
badrealnews = []
fakenewshead = []
nuetralnews = [] 

#10-15 --> $900 to $1000
#15-17 --> $1100 to $1200
#17-20 --> $1300 to $1500
#20-22 --> $1600 to $1900
#22-25 --> $2000 to $2400
#25-27 --> $2500 to $2900
#27-30 --> $3200+
#30+ --> NO

fake1 = Fakenews('Are your babies military spies?', -11, 0, -6, -6, 0, 2000)
fake2 = Fakenews('Ku Klux Klan member becomes first from the group to be elected to Senate', -5, 0, -10, -5, -5, 2500)
fake3 = Fakenews('All flights suspended worldwide', 2, -4, 0, -2, -8, 900)
fake4 = Fakenews('Eating plastic can prevent cancer', -1, -2, 0, -8, -4, 1000)
fake5 = Fakenews('USA has declared war on Canada', -6, 0, -9, 0, -4, 1200)
fake6 = Fakenews('All movies will now have to star at least one disabled lead', 0, -9, -2, -4, -1, 1100)
fake7 = Fakenews('World leaders accidentally swap nuclear codes at UN General Assembly', -8, -3, -8, 0, -6, 2600)
fake8 = Fakenews('Rugby banned for promoting violence', -1, -10, 0, -3, -1, 1100)
fake9 = Fakenews("National bank gambles away all of the national reserves on bet365.com", -2, -2, -5, -1, -11, 1800)
fake10 = Fakenews("Kim Jong-Un launches missile at South Korea as a prank", -8, 0, -6, -3, -2, 1500)

good1 = Realnews('Global oil rates plummet', 8, 0, 5, -3, 10)
good2 = Realnews('Stimulus package announced, markets rally', 5, 2, 3, 4, 14)
good3 = Realnews('Breakthrough in Hydrogen fusion technology', 4, 0, 5, 0, 10)
good4 = Realnews('Miracle drug to cure AIDS developed', 0, 5, 8, 5, 5)
good5 = Realnews('Global literacy rates reach all time high', -2, 3, 8, 8, 2)
good6 = Realnews('Anti - vaxxers no more', 1, 1, 4, 10, 5)
good7 = Realnews('Korean peninsula united!', -2, 5, 6, 4, 8)
good8 = Realnews('Crime rate at all time low', 4, 4, 5, 1, 2)
good9 = Realnews('China releases 120 politcal prisoners', -1, 0, 8, 5, 4)
good10 = Realnews('Hunger rates drop across Africa', 0, 1, 6, 9, 3 )

bad1 = Realnews('War in Syria shows no signs of stopping', -8, 0, -4, -3, -3)
bad2 = Realnews('Pandemic spreads', -3, -10, 3, -5, -9)
bad3 = Realnews('World leader assasinated', 1, -1, -6, -6, -6)
bad4 = Realnews('Political crisis in Afghanistan', 2, 0, -11, -3, -5)
bad5 = Realnews('Serial killer on the loose', 0, -2, -1, -9, -3)
bad6 = Realnews('Middle East blocks all trade with NATO', -2, 0, -4, -1, -12)
bad7 = Realnews('Wildfire in California spreads', 1, -7, -4, -5, -4)
bad8 = Realnews('Economist predicts impending recession', -1, -2, -4, 0, -9)

nuetral1= Realnews('Stalemate at Middle Eastern Front ', 3, 0, -5, -2,-3)
nuetral2= Realnews('Sweden wins global carpenter Olympics  ', 0, 2, 0, 3, 0)
nuetral3= Realnews('British Prime Minister meets Brazilian Envoy, talks Trade ', 0, 0, 3, 2, 4)
nuetral4= Realnews('Manchester United wins EFL League 1!!! ', 0, 3, 0, 2, 1)
nuetral5= Realnews('Elections held sucessfully in Brazil  ', 0, 0, 5, 2, 3)
nuetral6= Realnews('UN Security Council adds India as permanant member ', 5, 0, 5, 0, 3)
nuetral7= Realnews('Migrant crisis in Europe continues... ', 5, 0, -5, -10, -6)
nuetral8= Realnews('American Weapon manufacturers show record low profits, blame the hippies. ', -8, 3, 3, 0,-5)
nuetral9= Realnews('Veteran Actor passes away ', 0, -8, 0, -2, 0)
nuetral10= Realnews('Treaty Signed between East and West Korea ', -5, 0, 5, 2, 5)

goodrealnews.append(good1)
goodrealnews.append(good2)
goodrealnews.append(good3)
goodrealnews.append(good4)
goodrealnews.append(good5)
goodrealnews.append(good6)
goodrealnews.append(good7)
goodrealnews.append(good8)
goodrealnews.append(good9)
goodrealnews.append(good10)

badrealnews.append(bad1)
badrealnews.append(bad2)
badrealnews.append(bad3)
badrealnews.append(bad4)
badrealnews.append(bad5)
badrealnews.append(bad6)
badrealnews.append(bad7)
badrealnews.append(bad8)

nuetralnews.append(nuetral1)
nuetralnews.append(nuetral2)
nuetralnews.append(nuetral3)
nuetralnews.append(nuetral4)
nuetralnews.append(nuetral5)
nuetralnews.append(nuetral6)
nuetralnews.append(nuetral7)
nuetralnews.append(nuetral8)
nuetralnews.append(nuetral9)
nuetralnews.append(nuetral10)

fakenewshead.append(fake1)
fakenewshead.append(fake2)
fakenewshead.append(fake3)
fakenewshead.append(fake4)
fakenewshead.append(fake5)
fakenewshead.append(fake6)
fakenewshead.append(fake7)
fakenewshead.append(fake8)
fakenewshead.append(fake9)
fakenewshead.append(fake10)
p = 0
choice1but = tk.Button(root, text="test")
choice2but = tk.Button(root, text="test")
choice3but = tk.Button(root, text="test")
goodreallabel = tk.Label(root, text = "Ok")
badreallabel = tk.Label(root, text = "Ok")
nuetrallabel = tk.Label(root, text ="Ok")
nuetrallabel2 = tk.Label(root, text="Ok")

# greenimg = tk.PhotoImage(file="greenbut.png")
jeffpostimg = tk.PhotoImage(file="assets/JEFFPOST.png")
globalherald = tk.PhotoImage(file="assets/globalherald.png")

def whileloop():
    global p
    global choice1but
    global choice2but
    global choice3but
    global goodreallabel
    global badreallabel
    global nuetrallabel2
    global nuetrallabel
    q = 0
    y = 0
    while q ==0:
        if military<60 or politics<60 or economy<60 or entertainment<60 or culture<60:
            x = random.randrange(len(goodrealnews))
            article1 =  goodrealnews[x]
            article1.implement()
            goodreallabel = tk.Label(root, text = article1.headline, image=jeffpostimg, compound="center")
            goodreallabel.place(x=250*y, y=10,width=500, height=360)
            goodrealnews.remove(article1)
            y = y+1
        elif military>130 or politics>130 or economy>130 or entertainment>130 or culture>130:
            x = random.randrange(len(badrealnews))
            article2 = badrealnews[x]
            article2.implement()
            badreallabel = tk.Label(root, text = article2.headline, image=jeffpostimg, compound="center")
            badreallabel.place(x=250*y, y=10,width=500, height=360)
            badrealnews.remove(article2)
            y = y+1
        elif military<131 and military>59 or politics<131 and politics>59 or economy<131 and economy>59 or entertainment<131 and entertainment>59 or culture<131 and culture>59:
            x = random.randrange(len(nuetralnews))
            article3 = nuetralnews[x]
            article3.implement()
            nuetrallabel = tk.Label(root, text = article3.headline, image=jeffpostimg, compound="center")
            nuetrallabel.place(x=0, y=20,width=480, height=360)
            nuetralnews.remove(article3)
            y = y+1
            if y == 1:
                k = random.randrange(len(nuetralnews))
                article4 = nuetralnews[k]
                article4.implement()
                nuetrallabel2 = tk.Label(root, text = article4.headline, image=globalherald, compound="center")
                nuetrallabel2.place(x=480, y=20,width=480, height=360)
                nuetralnews.remove(article4)
                y = y+1
            if y == 2:
                xx = random.randrange(len(nuetralnews))
                article5 = nuetralnews[xx]
                article5.implement()
                nuetrallabel3 = tk.Label(root, text = article5.headline, image=jeffpostimg, compound="center")
                nuetrallabel3.place(x=960, y=20,width=480, height=360)
                nuetralnews.remove(article5)
                y = y+1
        if y>2:
            q = 1

    def fakechoice():
        global choice1but
        global choice2but
        global choice2but
        global choice3but
        global goodreallabel
        global badreallabel
        global nuetrallabel2
        global nuetrallabel
        global i
        global p
        a1=random.randrange(len(fakenewshead))
        a2=random.randrange(len(fakenewshead))
        a3=random.randrange(len(fakenewshead))
        def choice1():
            global p
            fakenewshead[a1].implement()
            fakenewshead.remove(fakenewshead[a1])
            p = 1
        def choice2():
            global p
            fakenewshead[a2].implement()
            fakenewshead.remove(fakenewshead[a2])
            p = 1
        def choice3():
            global p
            fakenewshead[a3].implement()
            fakenewshead.remove(fakenewshead[a3])
            p = 1
        # def testing():
        #     global p
        #     print(p)
        if a1 == a2 or a1 == a3 or a2 == a3:
            fakechoice()
        else: #1366x762
            choicelabel = tk.Label(root, text = "Choose which article to publish:")
            choicelabel.place(x=770, y=1000, width=200, height=25)
            choice1but = tk.Button(root, text=fakenewshead[a1].headline, width = 25, height= 25, compound="center", command=choice1)
            choice1but.place(x=140, y=500, width=400, height=25)
            choice2but = tk.Button(root, text=fakenewshead[a2].headline, width = 25, height= 25, command=choice2)
            choice2but.place(x=600, y=500, width=400, height=25)
            choice3but = tk.Button(root, text=fakenewshead[a3].headline, width = 25, height= 25, command=choice3)
            choice3but.place(x=1000, y=500, width=400, height=25)
            # test = tk.Button(root, text="Test", command = testing)
            # test.grid(row=4, column=1)
    def publish():
        global choice1but
        global choice2but
        global choice3but
        global goodreallabel
        global badreallabel
        global nuetrallabel2
        global nuetrallabel
        choice1but.destroy()
        choice2but.destroy()
        choice3but.destroy()
        
        root.after(500, whileloop)

    test = tk.Button(root, text="Publish", command = publish)
    test.grid(row=4, column=1)
  
    fakechoice()

root.after(500, whileloop)
root.mainloop()
