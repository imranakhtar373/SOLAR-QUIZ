# python quiz 
#questions
questions = ("1. which planet have maximum number of moons?: ",
            "2. which planet named as Lucifer?: ",
            "3. which is the brightest and hottest planet in the Solar System?: ",
            "4. which planet has the shortest day?: ",
            "5. which planet own the moons (Phobos and Deimos)?: ",
            "6. what is the other name for (Orion Constellation)?: ",
            "7. what is the number of known satellites of Jupiter?: ",
            "8. which is the brightest star in solar system?: ",
            "9. Which is the brightest star in the Orion Constellation?: ",
            "10. what is the name of planet that orbits star outside of our solar system?: ")


# options of the upper questions
options = (("A. Saturn", "B. Venus", "C. Mercury", "D. Pluto"),
            ("A. Neptune", "B. Venus", "C. Jupiter", "D. Uranus"),
            ("A. Venus", "B. Saturn", "C. Sun", "D. Mars"),
            ("A. Earth", "B. Neptune", "C. Jupiter", "D. Uranus"),
            ("A. Saturn", "B. Jupiter", "C. Venus", "D. Mars"),
            ("A. Hunter", "B. Taurus", "C. Ursa", "D. Oeneus"),
            ("A. 96", "B. 80", "C. 79", "D.104"),
            ("A. Antares", "B. Arcturus", "C. Canopus", "D. Sirius"),
            ("A. Zeta", "B. Delta", "C. Rigel", "D. Epsilon"),
            ("A. Outerplanets", "B. Exoplanet", "C. Gas giant", "D. Comits"))

# correct answers
answers = ("A", "B", "A", "C", "D", "A", "B", "D", "C", "B")

guesses = []

score = 0 

question_num = 0 


# for displaying the questios with options and answer.



for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    

# for user (guessing the right answer)
    


    guess = input ("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT :)")
    else :
        print("INCORRECT :(")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("-----------------------")
print("       RESULTS         ")
print("-----------------------")


#for correct answers.
print("answer: " , end ="")
for answer in answers:
    print(answer , end=" ")


# for guesses.
print("guesses: " , end="")
for guess in guesses:
    print(guess, end=" ")
print()


# for correct score
score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")