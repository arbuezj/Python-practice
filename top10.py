# ------ FUNCTIONS ------

# Welcomes user and introduce the quiz
def  intro():
    # Ask the user their name 
    name = input("what's your name? ")

    # Greet the user and introduce the quiz?
    print("Welcome to this quiz,", name)
    print("")

def getLives():
    while True:
        lives =  input("How many change do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please chose a positive number")
        except:
            print("That wasn't a number  ")

def iscorrect(answer, list):
    if answer in list:
        return True
    else:
        return False
        

       
       

# ----- MAIN CODE ----- 

intro()
lives = getLives()

BIGEST_COUNTRIES_ANSWER = ("canada", "russia ")
score = 0
while lives  > 0:
    answer = input 

   if is correct

