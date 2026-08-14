from quiz_data import get_questions
import random, datetime

question_bank = get_questions()

print(question_bank)

random.shuffle(question_bank)
print("-" * 60)
print(" ")
print(question_bank)


questions_only = []
answers_only = []
user_responses = []

for question in question_bank:
   # print(question[0])
    questions_only.append(question[0])
    answers_only.append(question[1])

print(questions_only)
print(answers_only)


def ask(question):
    response = input(f"{question} :")
    return response



while True:
    for que in questions_only:
        answer = ask(que)
        user_responses.append(answer)

    break

correct = 0

incorrect = 0

for i in range(len(answers_only)):
        if user_responses[i] == answers_only[i]:
            print("Correct")
            correct += 1
        else:
            print("Incorect")
            incorrect += 1