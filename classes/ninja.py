import random
phrases = { 'Michelangelo' : [" We’re lean, we’re green, and we’re mean! ", "Kowabunga DUUUUDES!!!!", "What language is that Mikey? Nitwit?", "Its Ninja time!" ,'BOOYAKASHA!'],
    'Donatello' : ['OH. FAB-O BOOOOTS','Hard feelings! MASSIVE HARD FEELINGS',"You're so cute but so mean! Why do I always go for your type?!",'Forgiveness Is Devine, But Never Pay Full Price For A Late Pizza','I Love Being A Turtle'],
}
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        print(phrases['Michelangelo'][random.randint(1,4)])
        prob= random.randint(1,9)
        if(prob%2==0):
            self.pirateDefend(pirate)
        else:
            pirate.health -= 0
        return self

    def pirateDefend (self, pirate):
        defend= random.randint(1,10)
        if(defend<=pirate.speed):
            pirate.health -= self.strength / 2
        else:
            pirate.health -= self.strength
        return self


class ninja_two(Ninja):
    def __init__(self, name):
        super().__init__(name)

    def show_stats( self ):
        super().show_stats()
        # print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        print(phrases['Donatello'][random.randint(1,4)])
        prob= random.randint(1,9)
        if(prob%2==0):
            self.pirateDefend(pirate)
        else:
            pirate.health -= 0
        return self

    def pirateDefend (self, pirate):
        super().pirateDefend(pirate)