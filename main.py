# Purpose: To display the questions to the user from the Question class.
# Author: Areesha Tariq
# 12/11/2023

import question    # importing the question module

# main function
def main():
    file = open("questions.txt", 'r')   # opening file in read mode
    questions = []    # initializing variables
    score = 0

    # loop to read through the file & store it to their variables
    for something in range(5):
        ques = file.readline().rstrip('\n')
        opt1 = file.readline().rstrip('\n')
        opt2 = file.readline().rstrip('\n')
        opt3 = file.readline().rstrip('\n')
        opt4 = file.readline().rstrip('\n')
        answer = file.readline().rstrip('\n')
        temp = question.Question(ques, opt1, opt2, opt3, opt4, answer)   # creating a Question object
        questions.append(temp)    # appening the object to the list

    file.close()   # closing the file

    # Looping through the questions list
    for q in questions:
        print(q)   # prints questions & answer choices
        response = int(input("Enter your choice (1-4): ")) # gets user answer
        ans = int(q.get_answer())  # getting correct answer using the method

        # checking users respose
        if response == ans:
            print("Correct\n")
            score += 1 # Adding 1 to score for correct answers
        else:
            print(f"Sorry - correct choice is {ans}\n")

    # Displaying final score & comment
    print(f"You scored {score} out of {len(questions)}")
    if score >= 4:
        print("Great!")
    else:
        print("Review material")

main() # calling main function
