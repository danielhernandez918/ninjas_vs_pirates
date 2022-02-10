phrases = {'Jack': ['WhAt HapEneD tO aLL tHe RuM?!?!', 'If you were waiting for the opportune moment, that was it.', 'Why fight when you can negotiate?', 'Im going to send you to Davy Jones locker!', 'Nobody move! I dropped my brain.'],
    'DavyJones' : ['Did You Forget? Im A Heartless Wretch!', 'Ha! You Afraid To Get Wet?', 'Summon the Kracken!','Do You Fear Death?',"Did You Forget? I'm A Heartless Wretch!"]
}

import random
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")


    def attack ( self , ninja ):
        print(phrases['Jack'][random.randint(1,4)])
        prob= random.randint(1,9)
        if(prob%2==0):
            self.ninjaDodge(ninja)
        else:
            ninja.health -= 0
        return self

    def ninjaDodge (self, ninja):
        dodge= random.randint(1,10)
        if(dodge<=ninja.speed):
            ninja.health -=0
        else:
            ninja.health -= self.strength
        return self



class pirate_two(Pirate):
    def __init__(self, name):
        super().__init__(name)

    def show_stats( self ):
        super().show_stats()
        # print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")


    def attack ( self , ninja ):
        print(phrases['DavyJones'][random.randint(1,4)])
        prob= random.randint(1,9)
        if(prob%2==0):
            self.ninjaDodge(ninja)
        else:
            ninja.health -= 0
        return self

    def ninjaDodge (self, ninja):
        super().ninjaDodge(ninja)