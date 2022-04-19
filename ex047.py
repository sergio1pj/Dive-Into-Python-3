import random

'''
for i in range(5):
    print(random.randint(10, 20))
'''

'''
members = ['Sergio', 'João', 'Maria', 'Pedro']
leader = random.choice(members)
print(leader)
'''
class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return random.randint(1, self.sides)

dice1 = Dice(6)
print(dice1.roll_dice())