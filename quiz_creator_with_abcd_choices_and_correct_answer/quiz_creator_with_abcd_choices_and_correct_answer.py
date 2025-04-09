# make an infinite loop that will only stop if the user type "exit"
while True:
    print("type (exit) if you want to stop adding question")
    # ask for a Questions.
    user_questions = input("Enter a Question: ")
    # ask for the possible answers in (A, B, C, D)
    choice_A = input("Enter a possible answer, A: ")
    choice_B = input("Enter a possible answer, B: ")
    choice_C = input("Enter a possible answer, C: ")
    choice_D = input("Enter a possible answer, D: ")
    # input the correct answer.

# add the question, possible answers, and the correct answer in a txt file.
# use the loop if the user wants to add another questions and stop if the user type "exit"
    if user_questions == "exit":
        print("You typed 'exit'. Exiting the quiz creator.")
        break