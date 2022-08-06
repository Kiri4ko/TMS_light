from random import randint


class Dice:

    def __init__(self, sides: int):
        self.random_side = str(randint(1, sides))

    def __repr__(self):
        return self.random_side


dice_1 = Dice(6)

print(dice_1)
