from random import randint


class Dice:

    def __init__(self, sides: int):
        self.sides = sides

    def get_dice(self):
        self.random_side = randint(1, self.sides)
        print(self.random_side)


dice_1 = Dice(6)
dice_1.get_dice()
