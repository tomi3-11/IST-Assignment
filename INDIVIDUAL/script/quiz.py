# Initial score for the user
score = 0

# Storing All the questions in a list
quiz = [
    {
	'question': "What is the capital city of Kenya?",
	'options': ["A. Kampala", "B. Cairo", "C.Arusha", "D. Nairobi"],
	'answer': "D"
    },
    {
	'question': "Which language is used for web development?",
	'options': ["A. Python", "B. HTML", "C. C++", "D. Java"],
	'answer': "B",
    },
	{
		# More questions to be added 
	}
]

# looping through all the quizes and displaying them to the user in order until done. 
for i, data in enumerate(quiz, 1):
    print(f"Question {i}. {data['question']}")
    for option in data['options']:
	    print(option)

    # Prompting user for an answer
    answer = input("Enter the correct Answer (A/B/C/D): ").strip().upper()

    # Evaluating Users' answers 
    if answer == data['answer']:
	    print("Correct Answer\n")
	    score += 1 # increasing or awarding user with 1 point for each correct answer
    else:
	    print(f"Wrong answer, the answer is {data['answer']}\n")

    # asking the user whether he or she wants to continue answer questions
    continue_choice = input("Do you want to continue (yes/no)?  ").lower()
    
    # Evaluating users choice.
    if continue_choice != "yes":
	    print("Thanks for Participating!!")
	    break

# Printing the final score
print(f"Your final score is: {score}/{len(quiz)}")
