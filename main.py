score = 0

# Ask the user thier name and save it 
name = input("what's your name?")
# Greet the user and the introduce the quiz
print("welcome to the quiz",name)

print("This quiz is about type of car")
# Ask the user a question 

answer = input("what is the most expinsive car ").lower()
# Tell them the correct answer 
if answer == "rolls-royce droptail".lower():
    print("The most expensive car is rolls-royce droptail it cost 30 million plus. You are correct!")
    score +=10
elif answer == "":
    print(" you dont know ")
  
else:
    print("The most expensive car is rolls-royce droptail it cost 30 million plus. You are incorrect")

#end the quiz
print("Well done{} thank you for playing thats end .Your final score was {} ".format (name,score))

