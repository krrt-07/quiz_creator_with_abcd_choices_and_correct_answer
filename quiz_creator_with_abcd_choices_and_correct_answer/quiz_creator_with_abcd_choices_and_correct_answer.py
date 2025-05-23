# make an infinite loop that will only stop if the user type "exit"
# make a txt file that will store the Questions and Answers.
with open("user_quiz.txt", "a") as file:
    question_number = 0

    while True:
        print("type (exit) if you want to stop adding question")

        # ask for a Questions.
        user_questions = input("Enter a Question: ")
        question_number += 1

        if user_questions == "exit":
            print("You typed 'exit'. Exiting the quiz creator.")
            break

        # ask for the possible answers in (A, B, C, D)
        choice_a = input("Enter a possible answer, A: ")
        choice_b = input("Enter a possible answer, B: ")
        choice_c = input("Enter a possible answer, C: ")
        choice_d = input("Enter a possible answer, D: ")

        # input the correct answer.
        correct_answer = input("Enter the correct answer(A, B, C, D): ")

    # add the question, possible answers, and the correct answer in a txt file.
        file.write(f"Question #{question_number}: {user_questions}\n")
        file.write(f"A. {choice_A}\n")
        file.write(f"B. {choice_B}\n")
        file.write(f"C. {choice_C}\n")
        file.write(f"D. {choice_D}\n")
        file.write(f"Correct Answer: {correct_answer}\n")
        file.write("\n") # add space to seperate the Questions.
