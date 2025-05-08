# 🧠 Python Quiz System

This project is a complete quiz system using Python. It includes:

1. `quiz_creator_with_abcd_choices_and_correct_answer.py` – to create and store quiz questions  
2. `quiz_program_that_reads_output_and_checks_answers.py` – to load the questions, quiz the user, and check answers using a GUI

---

## 📁 File Overview

| File Name                                                       | Description                                 |
|------------------------------------------------------------------|---------------------------------------------|
| `quiz_creator_with_abcd_choices_and_correct_answer.py`           | Terminal program to create quiz questions   |
| `user_quiz.txt`                                                  | Stores all questions and answers            |
| `quiz_program_that_reads_output_and_checks_answers.py`           | GUI program that runs the quiz              |

---

## ✏️ 1. Quiz Creator

**Filename:** `quiz_creator_with_abcd_choices_and_correct_answer.py`  
This script lets you create your own multiple-choice quiz. You can:
- Input a question
- Add 4 choices (A, B, C, D)
- Set the correct answer
- Repeat until you type `exit`

### 📝 Output Format (in `user_quiz.txt`):
Question #1: What is 2 + 2?
A. 3
B. 4
C. 5
D. 22
Correct Answer: B


---

## 🧠 2. Quiz Reader

**Filename:** `quiz_program_that_reads_output_and_checks_answers.py`  
This is a GUI-based program using `tkinter` that:
- Loads questions from `user_quiz.txt`
- Randomly displays one question at a time
- Lets the user click answers (A, B, C, D)
- Shows if the answer is correct or wrong
- Tracks the score and shows the final result

---

## 🔗 How It Works

1. **Create quiz questions** using the Creator program  
   → Saved automatically to `user_quiz.txt`  
2. **Run the Reader program** to take the quiz  
   → Loads and uses the same file to quiz the user

---

## 🚀 How to Run

### Run the Quiz Creator (Terminal):
```bash
python quiz_creator_with_abcd_choices_and_correct_answer.py
 
