score = 0
QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"

# Ask the user thier name and save it 
name = input("what's your name?")
# Greet the user and the introduce the quiz
print("welcome to the quiz",name)

print("This quiz is about type of car")
# Ask the user a question 
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
elif answer == "":
    print(" you dont know ")
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c":
else:
    print ("Wrong!")
    print("The most expensive car is rolls-royce droptail it cost 30 million plus. You are incorrect")

#end the quiz
print("Well done{} thank you for playing thats end .Your final score was {} ".format (name,score))

