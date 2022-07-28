import random


class Dice:
    sides = 6

    def get_dice(self):
        self.random_side = random.randint(1, self.sides)
        return self.random_side


dice_1 = Dice()
dice_2 = Dice()

print(dice_1.get_dice(), dice_2.get_dice())
