from random import shuffle


class Mystery:

    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.answer = answer
        self.choices = choices
        shuffle(self.choices)

    def l_choices(self):
        for i in range(len(self.choices)):
            self.choices.insert(i, f"{i + 1}. {self.choices[i]}")
            self.choices.pop(i + 1)
        return self.choices

    def check(self):
        return self.choices[int(input("Enter the answer number - ")) - 1][3:] == self.answer

    def __repr__(self):
        return "\n" + self.question + "\n" + "\n".join(self.l_choices()) + "\n"


q_1 = Mystery(question="The capital of the United States?", answer="Washington",
              choices=["New York", "Washington", "Los Angeles", "Las Vegas"])

q_2 = Mystery("Who was the first man on the moon?", "Neil Armstrong",
              ["Elon Musk", "Richard Branson", "Dmitri Kirichko", "Neil Armstrong"])

q_3 = Mystery("Which curse is unforgivable?", "Crucio",
              ["Riddikulus", "Accio", "Confundo", "Crucio"])


print(q_1, q_2, q_3)
print(q_1.check(), q_2.check(), q_3.check())
