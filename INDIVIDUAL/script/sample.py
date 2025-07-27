# 1.	Implement a quiz with multiple-choice questions and scoring.

# Initial score
score = 0

# Storing questions in a list
quiz = [
    {
        # A dictionary has a key-value pair
        # {"Key": "value"}
        "question": "who is the president of Kenya?",
        "options": ['A. Ruto', 'B. Raila', 'C. Uhuru', 'D. Daniel'],
        "answer": "A",
    },
    {
        "question": "What is the Capital city of Uganda?",
        "options": ['A. Nairobi', 'B. Cairo', 'C. Kampala', 'D. Juja'],
        "answer": "C",
    }
]

# Loop throw the quiz list and manipulate it
for index, data in enumerate(quiz, 1):
    print(f"Question {index}. {data['question']}")
    for option in data['options']:
        print(option)

    # prompt the user for an answer
    answer = input("Enter your answer using (A/B/C/D): ").strip().upper()

    # Evaluate the answer
    if answer == data['answer']:
        print("Correct\n")
        score += 2
    else:
        print(f"Wrong answer, the correct answer is {data['answer']}\n")

    continue_choice = input("Do you want to continue (yes/no): ").lower()
    if continue_choice != "yes":
        print("Thanks for Participating!")
        break


# display Final score
print(f"Your Overall score is {score} points")



