print("Welcome to my quiz")

playing = input("Would you like to play? ")

if playing != "yes" :
    quit()
print ("Okay, let's play")
score = 0

answer1 = input("What is the capital of Macedonia? ").capitalize()
if answer1 == "Skopje" :
    print("You got it right! Congrats!")
    score+=5
else : 
    print("Wrong. The correct answer is Skopje")

answer2 = float(input("What is the half of 6/2? "))
if answer2 == 1.5 :
    print("You didn't get tricked. Congrats!")
    score+=5
else : 
    print("Unfortunately, that is wrong. The correct answer was 1.5")

answer3 = input("What is the most spoken language in the world in 2022? ").capitalize()
if answer3 == "English" :
    print("Exactly! With a total of 1.348 billion speakers, English is number one, not Mandarin Chinese!")
    score+=5
else : 
    print("Incorrect. The correct answer is English")

print("You got " + str(score) + " points")