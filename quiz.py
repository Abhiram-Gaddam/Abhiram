import random

def shuffle_questions(questions):
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question['options'])
def start_quiz(questions):
    shuffle_questions(questions)
    score = 0
    for i in range(3):
        question = questions[i]
        print(f"Q{i + 1}: {question['question']}")
        
        # Print each option
        for j in range(len(question['options'])):
            print(f"  {j + 1}. {question['options'][j]}")
        
        # Get user's answer
        answer = input("Your answer (1/2/3/4): ")
        
        # Check if the answer is correct
        selected_option = question['options'][int(answer) - 1]
        if selected_option == question['answer']:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")
    
    print(f"Your final score is {score} out of {len(questions)}.")


if __name__ == "__main__":
    questions = [
        {
            "question": "What is the output of print(2 + 3)?",
            "options": ["2", "5", "23", "None of the above"],
            "answer": "5"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": [".java", ".py", ".txt", ".cpp"],
            "answer": ".py"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "define", "func"],
            "answer": "def"
        },
        {
            "question": "How do you insert comments in Python code?",
            "options": ["//", "/*", "#", "--"],
            "answer": "#"
        },
        {
            "question": "What will be the output of print('Hello'[1])?",
            "options": ["H", "e", "l", "o"],
            "answer": "e"
        },
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["6", "8", "9", "12"],
            "answer": "8"
        },
        {
            "question": "How do you create a dictionary in Python?",
            "options": ["{}", "[]", "()", "<>"],
            "answer": "{}"
        },
        {
            "question": "Which of the following is used to handle exceptions in Python?",
            "options": ["try", "except", "catch", "All of the above"],
            "answer": "All of the above"
        },
        {
            "question": "What is the output of the following code?\n```python\na = [1, 2, 3]\na.append(4)\nprint(a)\n```",
            "options": ["[1, 2, 3, 4]", "[4, 1, 2, 3]", "[1, 2, 3]", "[1, 2, 3, 4, 4]"],
            "answer": "[1, 2, 3, 4]"
        },
        {
            "question": "What is the output of print(len('Hello World'))?",
            "options": ["10", "11", "12", "13"],
            "answer": "11"
        },
        {
            "question": "What does the split() method do in Python?",
            "options": ["Joins two strings", "Splits a string into a list", "Replaces a substring", "None of the above"],
            "answer": "Splits a string into a list"
        },
        {
            "question": "How do you write a list comprehension to create a list of squares of numbers from 0 to 4?",
            "options": ["[x*x for x in range(5)]", "[x^2 for x in range(5)]", "[x**2 for x in range(4)]", "[x^2 for x in range(4)]"],
            "answer": "[x*x for x in range(5)]"
        },
        {
            "question": "What will be the output of the following code?\n```python\ndef func(x):\n    return x + 1\nprint(func(2))\n```",
            "options": ["1", "2", "3", "4"],
            "answer": "3"
        },
        {
            "question": "How do you create a class in Python?",
            "options": ["class ClassName:", "def ClassName:", "new ClassName:", "class ClassName():"],
            "answer": "class ClassName:"
        },
        {
            "question": "What is the correct syntax to import a module named 'math'?",
            "options": ["import.math", "import math", "math.import", "import-math"],
            "answer": "import math"
        }
    ]
    start_quiz(questions)