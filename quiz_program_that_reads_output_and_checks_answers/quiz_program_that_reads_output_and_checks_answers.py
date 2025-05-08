# open the text file from Quiz Creator in read mode.
def load_questions(filename="user_quiz.txt"):
    with open(filename, "r") as file:
        content = file.read().strip().split("\n\n")

    quiz_questions = []
    for question_block in content:
        question_lines = question_block.strip().split("\n")
        
# make a condition that will get the questions and answers from the text file.
# Skip empty or malformed question blocks (must have at least 6 lines)
# make the Quiz App.
# make the sizes for the window.
# make it randomize the questions.
# set the user score and current question index to 0.
# Create the question label.
# Create the choice buttons (A, B, C, D)
# Feedback label for correct/incorrect answer.
# Next button to go to the next question.
# Score label to show the user score.
# Show the first question.
# start the main program condition.

