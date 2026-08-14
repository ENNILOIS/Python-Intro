print("*" * 60)
print("       RANDOM QUIZ GENERATOR")
print("*" * 60)

question_bank =[
    ("What is html?", "Hypertext Markup Language"),
    ("What is css?", "Cascading Style Sheet"),
    ("What is http?", "Hypertext Transfer Protocol"),
    ("what is api?", "Application Programming Interface"),
    ("What is   RAG?", "Retrieval-Augmented Generation")
]



def get_questions():
    return question_bank