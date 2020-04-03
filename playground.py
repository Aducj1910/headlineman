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
fakenewshead = []
nuetralnews = [] 

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

good1 = Realnews('Global oil rate splummet', 8, 0, 5, -3, 10)
good2 = Realnews('Stimulus package announced, markets rally', 5, 2, 3, 4, 14)
good3 = Realnews('Breakthrough in Hydrogen fusion technology', 3, 0, 5, 0, 10)
good4 = Realnews('Miracle drug to cure AIDS developed', 0, 5, 8, 5, 5)
good5 = Realnews('Global literacy rates reach all time high', -2, 3, 8, 8, 2)

bad1 = Realnews('War in Syria shows no signs of stopping', -8, 0, -4, -3, -3)
bad2 = Realnews('Pandemic spreads', -3, -10, 3, -5, -9)
bad3 = Realnews('World leader assasinated', 1, -1, -6, -6, -6)
bad4 = Realnews('Political crisis in Afghanistan', 2, 0, -11, -3, -5)
bad5 = Realnews('Serial killer on the loose', 0, -2, -1, -9, -3)
bad6 = Realnews('Middle East blocks all trade with NATO', -2, 0, -4, -1, -12)
bad7 = Realnews('Wildfire in California spreads', 1, -7, -4, -5, -4)

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

badrealnews.append(bad1)
badrealnews.append(bad2)
badrealnews.append(bad3)
badrealnews.append(bad4)
badrealnews.append(bad5)
badrealnews.append(bad6)
badrealnews.append(bad7)

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


i=0
while i==0:

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
        
    print("Choose Which Article to publish")
    a1=random.randrange(len(fakenewshead))
    Print(fakenewshead[a1].headline + "  Press 1 to select") 
    a2=random.randrange(len(fakenewshead))
    Print(fakenewshead[a2].headline + "  Press 2 to select") 
    a3=random.randrange(len(fakenewshead))
    Print(fakenewshead[a3].headline + "  Press 3 to select") 

    val = int(input("Press 9 to quit"))
    if val == 1:
        fakenewshead[a1].implement()
    elif val == 2:
        fakenewshead[a2].implement()
    elif val == 3:
        fakenewshead[a3].implement()
    elif val == 9:
        q = 1
