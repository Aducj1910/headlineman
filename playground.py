import random

military = 100 
entertainment = 100 
politics = 100
culture = 100 
economy = 100
rating = 0 
money = 15000

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
fakenews = []

fake1 = Fakenews('Are your babies military spies?', -11, 0, -6, -6, 0)
fake2 = Fakenews('Ku Klux Klan member becomes first from the group to be elected to Senate', -5, 0, -10, -5, -5)
fake3 = Fakenews('All flights suspended worldwide', 2, -4, 0, -2, -8)
fake4 = Fakenews('Eating plastic can prevent cancer', -1, -2, 0, -8, -4)
fake5 = Fakenews('USA has declared war on Canada', -6, 0, -9, 0, -4)
fake6 = Fakenews('All movies will now have to star at least one disabled lead', 0, -9, -2, -4, -1)
fake7 = Fakenews('World leaders accidentally swap nuclear codes at UN General Assembly', -8, -3, -8, 0, -6)
fake8 = Fakenews('Rugby banned for promoting violence', -1, -10, 0, -3, -1)
fake9 = Fakenews("National bank gambles away all of the national reserves on bet365.com", 0, -2, -6, -1, -11)
fake10 = Fakenews("Kim Jong-Un launches missile at South Korea as a prank", -8, 0, -6, -3, -2)

good1 = Realnews('God is real', -50, 0, 6, 10, 5)
good2 = Realnews('World peace achieved', 5, 10, 6, 8, 15)
good3 = Realnews('Pandemic over', 5, 10, 4, 15, 25)
good4 = Realnews('Dogs can talk', 10, 20, -5, 15, 8)

bad1 = Realnews('War in Syria shows no signs of stopping', -8, 0, -4, -3, -3)
bad2 = Realnews('Pandemic spreads', -3, -10, 3, -5, -9)
bad3 = Realnews('World leader assasinated', 1, -1, -6, -6, -6)
bad4 = Realnews('Political crisis in Afghanistan', 2, 0, -11, -3, -5)
bad5 = Realnews('Serial killer on the loose', 0, -2, -1, -9, -3)
bad6 = Realnews('Middle East blocks all trade with NATO', -2, 0, -4, -1, -12)
bad7 = Realnews('Wildfire in California spreads', 1, -7, -4, -5, -4)

goodrealnews.append(good1)
goodrealnews.append(good2)
goodrealnews.append(good3)
goodrealnews.append(good4)

badrealnews.append(bad1)
badrealnews.append(bad2)
badrealnews.append(bad3)
badrealnews.append(bad4)

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
       x=random.randrange(len(goodrealnews))
       article1=goodrealnews[x]
       article1.implement()
       print(article1.headline)
       goodrealnews.remove(article1)
       y=2
       x=random.randrange(len(badrealnews))
       article2=badrealnews[x]
       article2.implement()
       print(article2.headline)
       badrealnews.remove(article2)
       if y>1:
        q=1

    print("Military  " + str(military))
    print("Politics  " + str(politics))
    print("Economy " + str(economy))
    print("entertainment " + str(entertainment))
    print("culture " + str(culture))
