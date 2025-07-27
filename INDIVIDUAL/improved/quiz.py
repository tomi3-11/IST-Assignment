"""
Individual project assignment.
Task: Implement a quiz with multiple-choice questions and scoring.

Author: Thomas Wotoro Joseph ID: 674609
Date: 12th/july/2025

The program displays a question with it's corresponding multiple choice (A, B, C, D) and asks the user for an answer then evaluates the user's answer. if correct, displays a correct confirmation and gives the user a +1 score, if not correct no reward and displays the wrong message.

Understanding the problem:
The problem is to write a program with the following specifications:
    1. Store questions with multiple choices.
    2. prompt the user for an answer
    3. Analyzing the user's answer where correct or wrong
        i. if correct, "Display a 'correct' message and add +1 score"
        ii. if not correct, "Display a 'wrong' message and no reward"
    4. Displays user's overall scores.
"""

import json

def main():
    questions = load_questions("questions.json")
    quiz(questions)
    
    
def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
    
def quiz(questions):
    # Initializing the function that performs the quiz operations
    score = 0 # initial user score
    
    for index, data in enumerate(questions, 1):
        print(f"Question {index}, {data["question"]}")
        for option in data["options"]:
            print(option)
            
        answer = input("Answer: ").upper().strip()
        if answer == data["answer"]:
            score += 1
            print("Correct answer")
        else:
            print(f"Wrong answer. The correct answer is {data["answer"]}")
            
        continue_choice = input("Do you want to continue? (yes/no): ").lower().strip() 
        if continue_choice != 'yes':
            break
            
    print(f"You score {score} out of {len(questions)}") 
    
    
if __name__ == "__main__":
    main()
    
"""
2. Algorithm
    1. Start
    2. REMARK: Importing module json
    3. REMARK: Defining a function
    4. define function load_questions with parameter filename.
    5. Read from questions.json file and load questions
    6. define function quiz with parameter questions
    7. REMARK: Initialization
    8. set the score = 0
    9. REMARK: Looping through the questions 
    10. for each positions, questions in questions, display the questions.
    11. for each option in questions, display the option
    12. REMARK: request data or data entry, score
    13. Ask the user for th answer
    14. REMARK: Check and analyze the answer
    15. if answer correct, report correct then increase score by one.
    16. if answer wrong, report wrong.
    17. REMARK: Defining the main function.
    18. REMARK: Initialization 
    19. set questions = load_questions("questions.json")
    20. REMARK: Calling the function
    21. Call the quiz function, quiz(questions)
    22. Stop
""" 
    
   
"""
1. Pseudocode

BEGIN
    Importing the json module.
    COMMENT: Initializing the function for loading questions from the file "questions.json" in the same directory, (e.g. def load_questions(filename) )
    Reading from questions.json file and loading it to the work space.
    COMMENT: Initializing the quiz function to manage the logic. (e.g. def quiz(questions))
    COMMENT: Initializing a variable for score
    score = 0 COMMENT: Setting the score to zero
    COMMENT: Looping through the questions from the questions.json file
    for index, data in enumerate(questions, 1): DISPLAY data['questions] 
    COMMENT: Looping through the multiple choice
    for option in data["options"]: DISPLAY the option.
    COMMENT: Request the user for an answer
    INPUT answer: COMMENT: Ask the user for the answer to the question displayed.
    COMMENT: Check or analyze the answer
    If answer == data['answer']: DISPLAY "Correct"
    score += 1 COMMENT: Increase the count of score by one for every correct answer.
    Else: DISPLAY "Wrong"
    COMMENT: display users overall score.
    DISPLAY: "You have scored 4/10 "
    COMMENT: Initializing the main function to call the quiz and load_questions functions. (e.g. def main():)
    COMMENT: Initializing a variable to store the questions and calling the load_question function.
    questions = load_question("questions.json")
    COMMENT: calling the quiz function with using the questions variable 
    quiz(questions)
END
    
    
    
3. Flow Chart
URL: https://app.diagrams.net/?src=about
"""