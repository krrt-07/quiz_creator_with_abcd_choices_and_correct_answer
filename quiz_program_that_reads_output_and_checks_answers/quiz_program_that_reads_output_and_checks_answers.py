# make the Quiz App.
# make it randomize the questions.
import tkinter as tk
import random 

# open the text file from Quiz Creator in read mode.
def load_questions(filename="user_quiz.txt"):
    with open(filename, "r") as file:
        content = file.read().strip().split("\n\n")

    quiz_questions = []
    for question_block in content:
        question_lines = question_block.strip().split("\n")

        # Skip empty or malformed question blocks (must have at least 6 lines)
        if len(question_lines) < 6:
            print(f"Skipping invalid question block: {question_block}")
            continue

# make a condition that will get the questions and answers from the text file.
        try:
            # Extract question text, answer choices, and the correct answer
            question_text = question_lines[0].split(": ", 1)[1]
            answer_choices = {
                "A": question_lines[1][3:],
                "B": question_lines[2][3:],
                "C": question_lines[3][3:],
                "D": question_lines[4][3:]
            }
            correct_answer = question_lines[5].split(": ")[1].strip().upper()
            
            # Append the question details to the list
            quiz_questions.append({
                "question": question_text,
                "choices": answer_choices,
                "correct": correct_answer
            })
        except IndexError:
            # If there's an issue with the formatting of the question block, skip it
            print(f"Error processing question block: {question_block}")
            continue

    return quiz_questions

# Create the GUI quiz app
class QuizApp:
    # make the sizes for the window.
    def __init__(self, master):
        self.master = master
        master.title("Quiz App")
        master.geometry("500x400")
        master.resizable(False, False)

         # Load and shuffle the questions
        self.quiz_questions = load_questions()
        random.shuffle(self.quiz_questions)

        # set the user score and current question index to 0.
        self.current_question_index = 0
        self.score = 0

        # Create the question label.
        self.question_label = tk.Label(master, text="", font=("Arial", 16), wraplength=480, justify="left")
        self.question_label.pack(pady=20)

        # Create the choice buttons (A, B, C, D)
        self.choice_buttons = {}
        for choice in ["A", "B", "C", "D"]:
            button = tk.Button(master, text="", width=40, font=("Arial", 12),
                               command=lambda selected_choice=choice: self.check_answer(selected_choice))
            button.pack(pady=5)
            self.choice_buttons[choice] = button

        # Feedback label for correct/incorrect answer.
        self.feedback_label = tk.Label(master, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=10)      

        # Next button to go to the next question.
        self.next_button = tk.Button(master, text="Next Question", font=("Arial", 12), command=self.next_question)
        self.next_button.pack(pady=10)   
        
        # Score label to show the user score.
        self.score_label = tk.Label(master, text=f"Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        # Show the first question.
        self.show_question()
        
# start the main program condition.
    def show_question(self):
        if self.current_question_index < len(self.quiz_questions):
            question = self.quiz_questions[self.current_question_index]
            self.question_label.config(text=f"Q: {question['question']}")
            for choice_key in question['choices']:
                self.choice_buttons[choice_key].config(text=f"{choice_key}. {question['choices'][choice_key]}", state=tk.NORMAL)
            self.feedback_label.config(text="")
            # disable the nest button until the users answer the question.
            self.next_button.config(state=tk.DISABLED)

        # if there are no more questions, show the final score.
        else:
            self.question_label.config(text="🎉 Quiz Finished!")
            for button in self.choice_buttons.values():
                button.config(state=tk.DISABLED)
            self.feedback_label.config(text=f"Final Score: {self.score}/{len(self.quiz_questions)}")
            self.next_button.config(state=tk.DISABLED)

    # make a function that will go to the next question.
    def check_answer(self, selected_choice):
        question = self.quiz_questions[self.current_question_index]
        for button in self.choice_buttons.values():
            button.config(state=tk.DISABLED)

        # make a condition that will check if answer is correct or not and show the feedback.
        if selected_choice == question["correct"]:
            self.score += 1
            self.feedback_label.config(text="✅ Tama! Good job!", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Mali. Tamang sagot: {question['correct']}", fg="red")
        # Enable the "Next Question" button after answering
        self.score_label.config(text=f"Score: {self.score}")
        self.next_button.config(state=tk.NORMAL)  

    # show the next question and update the score label until there are no more questions.
    def next_question(self):
        self.current_question_index += 1
        self.show_question()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()