# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

filehandle = open("questions.txt", "w")

number_questions = input("Number of questions for your quiz: ")
filehandle.write(number_questions + "\n")

for n in range(int(number_questions)):
    print()

    question_number = str(n + 1)

    filehandle.write(input("Please enter question " + question_number + ": ") + "\n")

    filehandle.write(input("What is option A for  question " + question_number + ": ") + "\n")
    filehandle.write(input("What is option B for  question " + question_number + ": ") + "\n") 
    filehandle.write(input("What is option C for  question " + question_number + ": ") + "\n")
    filehandle.write(input("What is option D for  question " + question_number + ": ") + "\n")

    filehandle.write(input("What is the letter of the correct answer for question " + question_number + ": ") + "\n")

filehandle.close()
