# Import the Question class from the Question module
from Question import Question

# List of prompts for the questions
questions_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
# Create a list of Question objects using the Question class and provided prompts and answers.
questions_given = [
    # From the class Question we hvae prompt and answer and below we gave the prompt and the anwer
    # starting with the first question at the 0 digit
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "b")
]
# Define a function run_test that takes a list of Question objects as a parameter.

def run_test(question):
    # Initialize a variable 'score' to keep track of the correct answers.
    score = 0
    for question in questions_given:
        answer = input(question.prompt).strip()  # Remove leading and trailing whitespace
        if answer.lower() == question.answer:
            #Increment by 1
            score += 1
    print("You got " + str(score) + "/" + str(len(questions_given)) + " correct")

run_test(questions_given)
