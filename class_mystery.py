from random import shuffle


class Mystery:
    points = 0

    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.__answer = answer
        self.choices = choices
        shuffle(self.choices)
        self.list_choices()

    def list_choices(self):
        for i in range(len(self.choices)):
            self.choices.insert(i, f"{i + 1}. {self.choices[i]}")
            self.choices.pop(i + 1)

    @property
    def check(self):
        if self.choices[int(input("Enter the answer number - ")) - 1][3:] == self.__answer:
            Mystery.points += 1
            return True
        else:
            return False

    def __repr__(self):
        return "\n" + self.question + "\n" + "\n".join(self.choices) + "\n" + f"Your points --> {Mystery.points}"


q_1 = Mystery(question="The capital of The United States?", answer="Washington",
              choices=["New York", "Washington", "Los Angeles", "Las Vegas"])

q_2 = Mystery("Who was the first man on the moon?", "Neil Armstrong",
              ["Elon Musk", "Richard Branson", "Dmitri Kirichko", "Neil Armstrong"])

q_3 = Mystery("Which curse is unforgivable?", "Crucio",
              ["Riddikulus", "Accio", "Confundo", "Crucio"])

print(q_1)
print(q_1.check)
print(q_2)
print(q_2.check)
print(q_3)
print(q_3.check)
print(f"Final score --> {Mystery.points} points")
