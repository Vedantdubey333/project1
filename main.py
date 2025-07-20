# Program to develop a game of rock ,paper and scissor
# rock : -1 , paper:0,scissor:1
import random
computer = random.choice([-1,0,1])
user = input("Enter your choice : ")
userMaunal = {'r' : -1,'p':0,'s':1}
youChoice = userMaunal[user]
l = {1 : "Scissor",0:"Paper",-1:"Rock"}
print(f"Yours Choce : {l[youChoice]}")
print(f"Computer Choice : {l[computer]}")
# if(computer == youChoice): 
#     print("It is a Draw.")
# elif(computer == -1 and youChoice == 0):   #computer - you  = -1
#     print("!!You Win!!")
# elif(computer == 0 and youChoice == 1):    #computer - you = -1
#     print("!!You Win!!")
# elif(computer == 1 and youChoice == -1):     #computer - you  = 2 
#     print("!!You Win!!")
# elif(computer == 0 and youChoice == -1):   #computer - you = 1
#     print("!!You lose!!")
# elif(computer == 1 and youChoice == 0):     #computer - you  = 1
#     print("!!You lose!!")
# elif(computer == -1 and youChoice == 1):   #computer - you  = -2
#     print("!!You lose!!")
# else:
#     print("There is a problem")
''' using a logic see
when you lose : at -1 and 2
when you win : at 1 and -2 '''
if(computer == youChoice):
    print("Its a Draw.")
else:
    if((computer-youChoice)== -1 or (computer-youChoice)==2):
        print("!!You Win!!")
    elif((computer-youChoice)==1 or (computer-youChoice)==-2):
        print("!!You Lose!!")