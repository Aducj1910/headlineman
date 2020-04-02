import random

military = 100 
entertainment = 100 
politics = 100
culture = 100 
economy = 100

class Fakenews:

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

good1 = Realnews('God is real', -50, 0, 6, 10, 5)
good2 = Realnews('World peace achieved', 5, 10, 6, 8, 15)
good3 = Realnews('Pandemic over', 5, 10, 4, 15, 25)
good4 = Realnews('Dogs can talk', 10, 20, -5, 15, 8)

bad1 = Realnews('War', -8, 0, -4, -3, -10)
bad2 = Realnews('Pandemic spreads', -3, -10, 3, -5, -15)
bad3 = Realnews('Pope is dead', 0, 0, -5, -8, -7)
bad4 = Realnews('Political crisis in Afghanistan', -10, 0, -20, -3, -15)

goodrealnews.append(good1)
goodrealnews.append(good2)
goodrealnews.append(good3)
goodrealnews.append(good4)

badrealnews.append(bad1)
badrealnews.append(bad2)
badrealnews.append(bad3)
badrealnews.append(bad4)

lengood = len(goodrealnews) 
lenbad = len(badrealnews)

i=0
while i==0:
    headlinename = input('Enter Headline Name ')
    inmil = int(input('Military Enter '))
    inent = int(input('Entertainment Enter '))
    inpol = int(input('Politics Enter '))
    incul = int(input('Culture Enter '))
    ineco = int(input('Economy Enter '))

    headlineinput = Fakenews(headlinename, inmil, inent, inpol, incul, ineco)
    headlineinput.implement()

    print("Military  " + str(military))
    print("Politics  " + str(politics))
    print("Economy " + str(economy))
    print("entertainment " + str(entertainment))
    print("culture " + str(culture))

    q=0
    y=0
    
    while q==0:
      x=random.randrange(lengood - 1)
      article1=goodrealnews[x]
      article1.implement
      print(article1.headline)
      y=y+1
      x=random.randrange(lenbad - 1)
      article2=badrealnews[x]
      article2.implement
      print(article2.headline)
      y=y+1
      if y>4:
        q=1

    print("Military  " + str(military))
    print("Politics  " + str(politics))
    print("Economy " + str(economy))
    print("entertainment " + str(entertainment))
    print("culture " + str(culture))
