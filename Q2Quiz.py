# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

inFile = open("questions.txt", "r")

score = 0
number_questions = int(inFile.readline())

for n in range(int(number_questions)): #it'll read all 6 lines at a time
    print("Question " + str(n + 1) + ": " + inFile.readline() + "option A: " + inFile.readline() + "option B: " + inFile.readline()
    + "option C: " + inFile.readline() + "option D: " + inFile.readline())

    rightAnswer = inFile.readline()

    userAnswer = input("Please enter your answer: ")

    if userAnswer == rightAnswer[0]:
        score += 1

    print()

print(str(score / number_questions * 100) + "%")
inFile.close()
