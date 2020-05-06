import random
import tkinter as tk
from tkinter import *

military=100
entertainment=100
globalpolitics=100
culture=100
economy=100

rating=0
money =0
Viewers=0

Msat=0 #-sat -- saturation
Esat=0
Gsat=0
Csat=0
Nsat=0

#M - Military
#E - Entertainment
#G - Global Politics
#C - Culture
#N - Economy

senmil=1
senent=1
senglopol=1
sencul=1
seneco=1
B=0.5

base=1000 # -- base money
preview=0 # -- views of previous articles

root = Tk()
root.geometry('1366x768')

class News:
    def __init__(self, headline, mil, ent, pol, cul, eco ,milsens ,entsens ,glopolsens ,culsens,ecosens,imgurl):
        self.headline = headline
        self.mil = mil
        self.ent = ent
        self.pol = pol
        self.cul = cul
        self.eco = eco
        self.imgurl = imgurl

    def implement(self):
        global military
        global entertainment
        global politics
        global culture
        global economy
        global senmil
        global senent
        global senglopol
        global sencul
        global seneco
        
        senmil=senmil+milsens
        senent=senent+entsens
        senglopol=senglopol+glopolsens
        sencul=sencul+culsens
        seneco=seneco+ecosens
        
        military = military + self.mil*senmil
        entertainment = entertainment + self.ent*senent
        globalpolitics = globalpolitics + self.pol*senglopol
        culture = culture + self.cul*sencul
        economy = economy + self.eco*seneco

    def image():
        return imgurl
    


class FakeNews:

    def __init__(self, headline, mil, ent, pol, cul, eco ,milsens ,entsens ,glopolsens ,culsens,ecosens,imgurl,P,cost,typex):
        self.headline = headline
        self.mil = mil
        self.ent = ent
        self.pol = pol
        self.cul = cul
        self.eco = eco
        self.imgurl = imgurl
        self.P=P
        self.milsens=milsens
        self.entsens=entsens
        self.glopolsens=glopolsens
        self.culsens=culsens
        self.ecosens=ecosens
        self.cost= cost
        self.typex=typex

    def implement(self):
        global military
        global entertainment
        global politics
        global culture
        global economy
        global senmil
        global senent
        global senglopol
        global sencul
        global seneco
        global B
        global money
        global Viewers
        global Msat
        global Esat
        global Gsat
        global Csat
        global Nsat
        global base 
        global preview

        senmil=senmil+self.milsens
        senent=senent+self.entsens
        senglopol=senglopol+self.glopolsens
        sencul=sencul+self.culsens
        seneco=seneco+self.ecosens

        military = military + self.mil*senmil
        entertainment = entertainment + self.ent*senent
        globalpolitics = globalpolitics + self.pol*senglopol
        culture = culture + self.cul*sencul
        economy = economy + self.eco*seneco
        B=B+self.p

        if typex=='M':
            Msat=Msat+Msat+2
            Viewers=base*senmil
            money=money-cost+viewers*.25

        if typex=='E':
            Esat=Esat+2
            Viewers=base*senent
            money=money-cost+viewers*.25

        if typex=='G':
            Gsat=Gsat+2
            Viewers=base*senglopol
            money=money-cost+viewers*.25

        if typex=='C':
            Csat=Csat+2
            Viewers=base*sencul
            money=money-cost+viewers*.25

        if typex=='N':
            Nsat=Nsat+2
            Viewers=base*seneco
            money=money-cost+viewers*.25

        base=base+.3*Viewers-.15*preview
        viewers=preview







    def image():
        return imgurl

class packet :
    def __init__(self, pack):
        self.pack=pack

    def add(self,headline1 ,headline2, headline3, headline4, headline5, headline6):
        self.pack.append(headline1)
        self.pack.append(headline2)
        self.pack.append(headline3)
        self.pack.append(headline4)
        self.pack.append(headline5)
        self.pack.append(headline6)

class timeline :
    def __init__(self,timeline):
        self.timeline=timeline()

    def add(pack):
        self.timeline.append(pack)

#Cost Ranges -
#HIGH - $8,000 - $10,000 
#MEDIUM - $5,000 - $8,000
#LOW - $2500 - $5000

#mil change - max(12), min(-15)
#ent change - max(10), min(-10)
#pol change - max(15), min(-15)
#cul change - max(10), min(-10)
#eco change - max(10), min(-10)

#News(headline, mil, ent, pol, cul, eco ,milsens ,entsens ,glopolsens ,culsens,ecosens,imgurl,P,cost,typex)

KoreasReal1=News("Tensions rise as Kim Jong Un cancels talks with US foreign sec.",10,0,-8,0,-5,.2,0,0,0,0,"image address not found")
KoreasReal2=News("Trump furious as Kim Jong Un shruggs of new sanctions",4,0,-9,0,-5,.05,0,.05,0,.1,"image address not found")
BritainReal1=News("Manchester City in deep financial trouble as oil mogul decides to pull out",0,3,0,2,-1,-.1,.2,0,.1,0,"image address not found")
KoreasFake1=FakeNews("Trump calls Kim Jong but gets rickrolled, orders 7th fleet to set sail to Japan",12,0,-12,0,-2,.3,0,0,0,0,"image address not found",.8,10000,"M")
KoreasFake2=FakeNews("America and N.Korea make up as leaders bond over love for junk food",-18,2,15,3,7,-.2,0,0,0,.1 ,"image address not found",.2,8000, "M")
BritainFake1=FakeNews("Both manchester teams decide to unite under the name Manchester City United",0,3,0,2,-1,-.1,.2,0,.1,0,"image address not found",5,7000, "E")

initiator = packet([])

initiator.add(KoreasReal1,KoreasReal2,BritainReal1,KoreasFake1,KoreasFake2,BritainFake1)

#News(headline, mil, ent, pol, cul, eco ,milsens ,entsens ,glopolsens ,culsens,ecosens,imgurl,P,cost,typex)

KoreasRealY1=News("Unverified source instigates escalation, starts militarization chain reaction between US and N. Korea",12,0,-3,0,2,0,.1,0,0,0,"image address not found")
KoreasRealY2=News("Doomsaday clock moves closer to midnight due to impending threat of nuclear war",6,-4,-10,-2,-10,-.1,-.2,.2,0,.3,"image address not found") 
EntertainmentRealY3=News("New Bond movie in the works",0,9,3,6,4,0,.2,0,0,0,"image address not found") 
KoreasFakeY1=FakeNews("Trump and Kim kiss and make up at the last moment",-18,5,15,5,10,-.5,.1,-.2,0,.2,"image address not found",.3,8000, "M")
KoreasFakeY2=FakeNews("US decides to launch pre-emtive strike wih payload including lewd images of Kim Jong Un",9,0,-5,0,-2,.2,0,0,0,0,"image address not found",.7,6000, "M")
EntertainmentFakeY3=FakeNews("Transgender asexual muslim Chinese black woman beeing considered for the role of Bond",-3,9,0,3,3,-.3,.2,0,0,0,"image address not found",5,8000, "E")

escalate = packet([])

escalate.add(KoreasRealY1, KoreasRealY2, EntertainmentRealY3, KoreasFake1, KoreasFake2, EntertainmentFakeY3)

#News(headline, mil, ent, pol, cul, eco ,milsens ,entsens ,glopolsens ,culsens,ecosens,imgurl,P,cost,typex)

KoreasRealN1 = News("USA eases DEFCON level another notch as North Korean relations improve", -2, 1, 7,2, 7,-.25, 0, .1, 0, .05, "image address not found")
KoreasRealN2 = News("North Korean says they will work with the White House to reduce tension on the peninsula", -2, 2, 6,3, 5,-.25, 0, .1, 0, 0, "image address not found")
CulturalRealN3 = News("Anti-vaxxer movement supported by prominent world leader", 0, -1, -3, 6, -4, 0, 0, -.05, .2, .05, "image address not found")
KoreasFakeN1 = FakeNews("Kim Jong Un sends Trump another love letter for the sixth straight day", -1, 2, 3, 2, 4, 0, 0, .05, -.05, .05, "image address not found", .2, 5500, "P") 
KoreasFakeN2 = FakeNews("White House creates official Kim Jong Un parody account", 4, 4, -1, 4, 0, .15, .1, 0, 0, .05, "image address not found", .65, 6200, "P") 
CulutralFakeN3 = FakeNews("Pineapple on pizza is now an official crime in 92 countries", 1, 3, 0, -4, -1, 0, -0.5, 0, 0.1, 0, "image address not found",5, 3500, "C")

#TKINTER GUI

labkorea1 = tk.Label(root, text=(initiator.pack[0]).headline)
labkorea1.place(x=0,y=0)
labkorea2 = tk.Label(root, text=(initiator.pack[1]).headline)
labkorea2.place(x=455, y=0)
labbritain1 = tk.Label(root, text=(initiator.pack[2]).headline)
labbritain1.place(x=910, y=0)

# def multifunction(*args):
#     for function in args:
#         function

def newspublish():
    global labkorea1
    global labkorea2
    global labbritain1
    global publishbutton
    labkorea1.destroy()
    labkorea2.destroy()
    labbritain1.destroy()
    fakekorea1 = tk.Button(root, text=(initiator.pack[3]).headline)
    fakekorea1.place(x=0,y=0)
    fakekorea2 = tk.Button(root, text=(initiator.pack[4]).headline)
    fakekorea2.place(x=455,y=0)
    fakebritain1 = tk.Button(root, text=(initiator.pack[5]).headline)
    fakebritain1.place(x=910,y=0)
    publishbutton.destroy()

    instructlabel = tk.Label(root, text="Click on Article to Publish")
    instructlabel.place(x=630, y=100)


# cb = lambda: multifunction(labkorea1.destroy(), labkorea2.destroy(), labbritain1.destroy())

publishbutton = tk.Button(root, text="Go to publish", command=newspublish)
publishbutton.place(x=630, y=100)

root.mainloop()
