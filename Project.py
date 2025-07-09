# 1 MADLIBS GAME

adjective = input ("Enter the adjective : ")
animal=input("Enter name of animal : ")
verb_past_tense=input("Enter Verb in past tense : ")
adjective2= input("Enter adjective2 :")
place=input("Enter the place name : ")
animal2=input("Enter next animal name : ")
adjective3= input("Enter the adjective : ")
verb=input("Enter the verb : ")
verb_past_tense2=input("Enter another Verb in past tense : ")
adjective4=input("Enter the another adjective : ")

print(f"I saw {adjective} {animal} jumping up and down in its tree."
f"IT {verb_past_tense} through the large tunnel that led to its {adjective2} {place}."  
f"I got some peanuts and passed them through the cage to a gigantic gray {animal2}"  
f"towering above my head. Feeding that animal made me hungry."  
f" I went to get a {adjective3} scoop of ice cream. It filled my stomach."  
f"Afterwards, I had to {verb} to catch our bus."  
f"When I got home, I {verb_past_tense2} my mom for a {adjective4} day at the zoo")



# 2 python calculator



operator=input("ENTER THE OPERATOR (+,-,*,/) : ")
num1=float(input("ENTER THE NUMBER 1 : "))
num2=float(input("ENTER THE NUMBER 2 : "))
if operator=="+":
    result=num1+num2
    print(round(result,2))

elif operator=="-":
    result=num1-num2
    print(round(result,2))

elif operator=="*":
    result=num1*num2
    print(round(result,2))
elif operator=="/":
    result=num1/num2
    print(round(result,2))
    
else:
    print("YOU ENTERED INVALID OPERATOR")



# 3 weight convertor

weight=float(input("ENTER YOUR WEIGHT : "))
unit=input("ENTER THE UNIT OF YOU ENTERED (K or L): ")

if unit=="K":
    weight=weight*2.205
    unit="lbs"
    print(f"your weight is : {weight}{unit}")

elif unit=="L":
    weight=weight/2.205
    unit="kgs"
    print(f"Your weight is : {weight}{unit}")

else:
    print("You Entered Invalid Unit") 


# 4 Temperature Convertor Program

temp = float(input("enter the Temperature : "))
unit =input("celsius or fahreheit(C or F)")

if unit=="C":
    temp=(temp*9)/5+32
    unit="°F"
    print(f"Temperature in Farenheit is :  {temp}{unit}")

elif unit=="F":
      temp=(temp-32)*5/9
      unit="°C"
      print(f"Temperature in Celsius is :  {temp}{unit}")

else:
     print(f"{unit} is invalid unit")

#5 validate user input exercise
#1. username is no more than 12 character
#2. user name not contain space
#3. username not contain digit

username=input("Enter the username : ")
if  len(username)>12:
    print("username should not more than 12 character")
elif not username.find(" ")==-1:
    print("username should not contain space")
elif not username.isalpha():
    print ("username  should not contain digit")
else:
    print(username)

#6 python compound interest calculator


principle=0
rate=0
time=0
while principle<=0:
   principle= float(input("Enter the principle amount : "))
   if principle<=0 :
    print(" principle cant be zero or negative")
    
while rate<=0:
   rate= float(input("Enter the  interest rate : "))
   if rate<=0 :
    print(" interest rate cannot be zero or negative")
    
while time<=0:
   time= int(input("Enter the time in years : "))
   if time<=0 :
    print(" time cannot be zero or negative")
    
total=principle*pow((1+rate/100),time)
print(f"balance after {time}year/s : ₹{total:,.2f}")




#7 Countdown timer


import time
my_time=int(input("Enter your time in seconds : "))
for x in range(my_time,0,-1):
    seconds=int(x%60)
    minutes=int((x/60)%60)
    hour=int(x/3600)
    print(f"{hour:021}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time up!")


#8 shopping cart program

foods=[]
prices=[]
total=0
while True:
    food=input("Enter the food(q to quit) : ")
    if food=="q":
     break
    else:
       price=float(input("Enter the price of {food} :₹ "))
       foods.append(food)
       prices.append(price)

print("----- YOUR CART IS -----")

for food in foods:
   print(food,end=" ")
print()

for price in prices:
   total= total+price
print(f"Your total is ₹{total}") 

#9 2D collection NUMPAD

nump_pad=( (1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#") )
for num in nump_pad:
    for x in num:
        print(x,end=" ")
    print()  

#10 quiz game


questions=("How many elements in periodic table? : ",
           "which animal lays largest egg? : ",
           "what is most abudant gas in Earth atmosphere? : ",
           "How many bones are in human body? : ",
           "which planet in the solar system is hottest? : ")
options=(("A.112","B.100","C.221","D.118"),
         ("A.whale","B.crocodile","C.ostrich","D.lion"),
         ("A.nitrogen","B.oxygen","C.carbon","D.helium"),
         ("A.209","B.206","C.112","D.208"),
         ("A.Mercury","B.Venus","C.Mars","D.Earth"))
answers=("D","C","A","B","A")
guesses=[]
score=0
question_no=0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_no]:
        print(option)

    guess=input("Enter (A),(B),(C),(D): ").upper()
    guesses.append(guess)
    if guess==answers[question_no]:
        score+=1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_no]} is the correct answer")
    question_no+=1

print("--------RESULT---------")

        
print("answers: ", end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess,end="")
print()

print(f"YOur score is {score}/5") 

#11 concession stand programe

menu={"pizza":150,
      "popcorn":400,
      "puffsss":50,
      "soda":30
      }
cart=[]
total=0
print("-----------MENU-----------")
for key,value in menu.items():
 print(f"{key:10}:${value:.2f}")
 
print("----------------------")

while True:
 food=input("select an item(qto quit) : ").lower()
 if food == "q":
  break
 elif menu.get(food) is not None:
  cart.append(food)

print("-----------YOUR ORDER-----------")
for food in cart:
  total+=menu.get(food)
  print(food,end=" ")


print()
print(f"Total is :${total:.2f}")


#12 Number guessing game

import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True
print("python number guessing game")
print(f"select number between {lowest_num} and {highest_num}")

while is_running:
    guess=input("enter your guess : ")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess>highest_num and guess<lowest_num:
            print("value entered is out of range")
            print(f" Please select number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("too low! Try again")
        elif guess>answer:
            print("too high! Try again")
        else:
            print("Your guess was correct")
            print(f"number of guesses: {guesses}")
            


    else:
        print("invalid guess")
        print(f" Please select number between {lowest_num} and {highest_num}")



#13 rock,papper,scissor

import random
options=("rock","paper","scissor")

Running=True
while Running:
    player=None
    computer=random.choice(options)
    while player not in options:

     player=input("enter a choice(rock,paper,scissor): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player==computer:
     print("its a Tie")
    elif player=="rock" and computer=="scissor":
     print("You Win")
    elif player=="scissor" and computer=="paper":
     print("You Win")
    elif player=="paper" and computer=="rock":
     print("You Win")
    else:
     print("you lose!")

    play_again=input("play again(y/n): ").lower()
    if not play_again=="y":
      Running= False

print("Thanks for playing!")

#14 Banking program

def show_balance():
    print("********************************")

    print(f"Your balance is: ${balance:.2f}")

    print("********************************")
def deposit():
    print("********************************")
    amount=float(input("Enter the amount to  deposit: "))
    
    if amount<0:
        print("********************************")
        print("thats not a valid amount")
        print("********************************")
        return 0
    else:
       
       print("********************************")
       print("Deposited successfully")
       return amount
def withdraw():
     print("********************************")
     amount=float(input("Enter the amount to  withdraw : "))
     
     if amount>balance:
         print("********************************")
         print("insufficient fund")
         print("********************************")
         return 0
     elif amount<0:
         print("********************************")
         print("amount must be greater than 0")
         print("********************************")
         return 0
     else:
         
         print("********************************")
         print("withdraw successfully")
         return amount    
balance=0
is_running=True

while is_running:
    print("********************************")
   
    print("Banking Program")

    print("********************************")

    print("1.Show Balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.Exit")

    choice= input("Enter your choice(1-4): ")

    if choice=="1":
        show_balance()
    elif choice=="2":
        balance += deposit()
    elif choice=="3":
       balance -= withdraw()
    elif choice=="4":
        is_running=False
    else:
        print("You entered invalid choice")

    
print("********************************")
print("Thank YOU ! Have a Nice day")



#15 slot machine program
import random
def spin_row():
    symbols = ['🍒',' 🍉',' 🍋', '🔔',' ⭐']
    results=[]
    for symbole in range(3):
        results.append(random.choice(symbols))
    return results



def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")
def get_payout(row,bet):
    if row[0]== row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*8
        elif row[0]=='⭐':
            return bet*10
    return 0

def main():
    balance=100
    print("*************************")
    print("welcome to python slots")
    print("symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance>0:
        print(f"current balance: ${balance}")

        bet=input("place your bet amount: ")

        if not bet.isdigit():
            print("please enter valid number")
            continue
        bet=int(bet)

        if bet>balance:
            print("insufficient funds")
            continue
        if bet<=0:
            print("bet must be greater than 0")
            continue
        balance -= bet

        row =spin_row()
        print("spinninggg........")
        print_row(row)


        payout=get_payout(row,bet)

        if payout>0:
            print(f"you won ${payout}")
        else:
            print("sorry you lose this round")

        balance+=payout

        play_again= input(" do you want to play again(y/n):").upper()

        if play_again =='Y':
            continue
        else:
            break

    print("************************************************")
    print(f"Game over ! Your final balance is $ {balance}")
    print("************************************************")

if __name__ == '__main__':
    main()

#16 Encryption program

import random
import string

chars=string.punctuation + string.ascii_letters+string.digits
chars=list(chars)
keys=chars.copy()

random.shuffle(keys)
#print(f"chars:{chars}")
#print(f"keys:{keys}")

#encrypt
plain_text= input("Enter a message to encrypt: ")
cipher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=keys[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#decrypt
cipher_text= input("Enter a message to decrypt: ")
plain_text=""

for letter in cipher_text:
    index=keys.index(letter)
    plain_text+=chars[index]

print(f"original message: {cipher_text}")
print(f"encrypted message: {plain_text}")

#17hangman program


import random
words = [
    "apple", "tiger", "chair", "snake", "phone", "cloud", "robot", "pizza", "green", "bread",
    "pumpkin", "blanket", "diamond", "android", "printer", "monitor", "battery", "cookies", "octopus", "picture",
    "astronaut", "algorithm", "butterfly", "microwave", "telescope", "umbrella", "elephant", "adventure", "javascript", "submarine",
    "juxtapose", "xylophone", "labyrinth", "zeppelin", "avalanche", "encryption", "paradoxical", "questionnaire", "hyperspace", "encyclopedia",
    "python", "variable", "function", "compiler", "database", "internet", "software", "hardware", "terminal", "algorithm"
]
hangman_art = {0:("  ",
                  "  ",
                  "  "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " |  ",
                  "   "),
               3:(" o ",
                  "/|  ",
                  "   "),
               4:(" o ",
                  "/|\\  ",
                  "   "),
               5:(" o ",
                  "/|\\  ",
                  "/  "),
               6:(" o ",
                  "/|\\  ",
                  "/ \\  ")}

def display_man(wrong_guesses):
    print("*******************************") 
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*******************************") 
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running= True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                  hint[i] =guess
        else:
            wrong_guesses+=1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOIU WIN!")
            is_running=False
        elif wrong_guesses>= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running=False



if __name__=="__main__":
    main()
