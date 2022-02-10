import random
from classes.ninja import Ninja, ninja_two
from classes.pirate import Pirate, pirate_two

michelangelo = Ninja("Michelanglo")

donatello = ninja_two("Donatello")

jack_sparrow = Pirate("Jack Sparrow")

davy_jones = pirate_two("Davy Jones")

phrases = { 'Michelangelo' : [" We’re lean, we’re green, and we’re mean! ", "Kowabunga DUUUUDES!!!!", "What language is that Mikey? Nitwit?", "Its Ninja time!" ,'BOOYAKASHA!'],
    'Jack': ['WhAt HapEneD tO aLL tHe RuM?!?!', 'If you were waiting for the opportune moment, that was it.', 'Why fight when you can negotiate?', 'Im going to send you to Davy Jones locker!', 'Nobody move! I dropped my brain.'],
    'Donatello' : ['OH. FAB-O BOOOOTS','Hard feelings! MASSIVE HARD FEELINGS',"You're so cute but so mean! Why do I always go for your type?!",'Forgiveness Is Devine, But Never Pay Full Price For A Late Pizza','I Love Being A Turtle'],
    'DavyJones' : ['Did You Forget? Im A Heartless Wretch!', 'Ha! You Afraid To Get Wet?', 'Summon the Kracken!','Do You Fear Death?',"Did You Forget? I'm A Heartless Wretch!"]
}


def battle_start(ninja, pirate):
    quote = random.randint(1,2)
    if(quote == 1):
        print("Michelangelo: You must be the worst Pirate I've ever seen")
        print("Jack Sparrow: But you have heard of me")
        battle_start_ninja(ninja)
        battle_start_pirate(pirate)
    if(quote == 2):
        print("Michelangelo: We're lean, we're green, and we're mean")
        print("Jack Sparrow: I'm Captain Jack Sparrow. The original. The only!")
        battle_start_ninja(ninja)
        battle_start_pirate(pirate)

def battle_start_ninja(ninja):
    pizza= random.randint(1,5)
    if(pizza>3):
        ninja.speed = ninja.speed + random.randint(1,3)
        print(f"Michelangelo's speed is now {ninja.speed}")

def battle_start_pirate(pirate):
    rum= random.randint(1,5)
    if(rum>3):
        pirate.strength = pirate.strength + random.randint(1,5)
        print(f"Jack Sparrows's strength is now {pirate.strength}")

def battle_end_pirate_death(pirate):
    if(pirate.health <= 0):
        print("Jack Sparrow: Your face is familier, have I threatened you before?")
        print("Michelangelo: Dude you are so predictable!!!")
def battle_end_ninja_death(ninja):
    if(ninja.health <= 0):
        print("Michelangelo: Whoa, whoa, whoa! Chill! ")
        print("Jack Sparrow: This is the day you will always remember as the day you almost caught Captain Jack Sparrow")

battle_start(michelangelo, jack_sparrow)
jack_sparrow.show_stats()
michelangelo.show_stats()
for x in range(26):
    michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()
battle_end_pirate_death(jack_sparrow)

# battle_start(donatello, davy_jones)
# donatello.show_stats()
# davy_jones.show_stats()
# for x in range(26):
#     donatello.attack(davy_jones)
# davy_jones.show_stats()
# battle_end_pirate_death(davy_jones)