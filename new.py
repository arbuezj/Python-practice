import random

score = 0
QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["Way to go!", "Keep it up!","Fantastic!"]
BAD_COMMENTS =  ["Keep trying!", "Maybe next time!", "Dont give up "]
QUESTION = ["What car is the most expensive car?",
            "who is the goat in nba?",
             "who is mvp last year in basketball"]
OPTION =  [["Lamborgini", "honda civic","pajero sport","Rolys royce "],
            ["Lebron james" ,"stephen curry" , "michael jordan","jordan clarckson"],
             [" Giannis Antetokoumpo" ,"lebron james","bronny jamess","seth curry "]]
SHORT_OPTIONS = ["a" "b" "c" "d"]
ANSWER = [3,2,0]

play = "yes" 

# Ask the user thier name and save it 
name = input("what's your name?")
# Greet the user and the introduce the quiz
print("welcome to the quiz",name)

print("This quiz is about type of car") 
# Check number of question attempts
while True:
    try: 
        tries = input("how many attemps do you want at each question? 1-4")
        tries = int (tries)
        break
    except:
        print("That's not a number ")


# Ask the user a question 
while play == "yes" :
    question= "What is the most expinsive car?"
    a = "lamborgini"
    b = "Honda Civic"
    c = "Pajero Sport"
    d = "Rolls-royce droptail"

    

    answer = input(QUESTION_FORMAT.format(question , a, b, c ,d)).lower()
    # Tell them the correct answer 
    if answer == d.lower() or answer == "d":
        print("The most expensive car is rolls-royce droptail it cost 30 million plus. You are correct!")
        score +=10
        print(random.choice(GOOD_COMMENTS))
    elif answer == "":
        print(" you dont know ")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c":
        print (" that's not a option")
    else:
        print ("Wrong!")
        print (random.choice(BAD_COMMENTS))
        print("The most expensive car is rolls-royce droptail it cost 30 million plus. You are incorrect")

    #end the quiz
    print("Well done{} thank you for playing thats end .Your final score was {} ".format (name,score))
    
    #replay 
    play = input("do you want to play agin?").lower()

