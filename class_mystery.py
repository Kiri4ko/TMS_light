from random import shuffle


class Mystery:

    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.answer = answer
        self.choices = choices
        shuffle(self.choices)
        self.score = 0

    def start_quiz(self):
        print(self.question)
        for i in range(len(self.choices)):
            print(i + 1, self.choices[i], sep=". ")

        if self.choices[int(input("Enter the answer number - ")) - 1] == self.answer:
            print(True)
        else:
            self.score = 3
            print(False)


total_score = 3 * 3  # one correct answer - 3 points.

q_1 = Mystery(question="The capital of the United States?", answer="Washington",
              choices=["New York", "Washington", "Los Angeles", "Las Vegas"])
q_1.start_quiz()
total_score -= q_1.score

q_2 = Mystery("Who was the first man on the moon?", "Neil Armstrong",
              ["Elon Musk", "Richard Branson", "Dmitri Kirichko", "Neil Armstrong"])
q_2.start_quiz()
total_score -= q_2.score

q_3 = Mystery("Which curse is unforgivable?", "Crucio",
              ["Riddikulus", "Accio", "Confundo", "Crucio"])
q_3.start_quiz()
total_score -= q_3.score

print(f"Your total score: * {total_score} *")
