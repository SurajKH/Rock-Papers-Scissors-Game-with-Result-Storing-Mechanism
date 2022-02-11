import random as rd
import csv
from datetime import datetime

# we have considered the importing of random,csv and datetime module over here

# initially we have setup the user and computer score to 0 over here
user_score = 0
computer_score = 0

list1 = []
# we have considered the empty list over here
while True:
    user = input("Enter R(Rock)/P(Paper)/S(Scissor) or Q(Quit):")

    if user == "Q":
        print("Program is terminated")
        if user_score > computer_score:
            # now we consider storing the result onto the csv file
            res = "User"
            f = open('Results.csv', 'a')
            writer_obj = csv.writer(f)
            list1.append(f"The Winner Between User and Computer is {res} at {datetime.now()}")
            writer_obj.writerow(list1)
            print("User is the final Winner!!!")

        elif computer_score > user_score:
            # now we consider storing the result onto the csv file
            res = "Computer"
            f = open('Results.csv', 'a')
            writer_obj = csv.writer(f)
            list1.append(f"The Winner Between User and Computer is {res} at {datetime.now()}")
            writer_obj.writerow(list1)
            print("Computer is the final Winner!!!")
        else:
            res = "Computer"
            f = open('Results.csv', 'a')
            writer_obj = csv.writer(f)
            list1.append(f"Its a draw between Computer and User at {datetime.now()}")
            writer_obj.writerow(list1)
            print("Its a Draw!!!!")

        quit()

    # we have created a list of options for the user
    option_list = ["R", "P", "S", "Q"]
    # now we utilize the random numbers for selecting the options within the list
    rand_num = rd.randint(0, 2)
    computer = option_list[rand_num]

    # calculates the scores for both computer and user scores based on the conditions over here
    if computer == "S" and user == "R":
        print("User wins!!!")
        user_score = user_score + 1

    elif computer == "P" and user == "R":
        print("User wins!!!")
        user_score = user_score + 1

    elif computer == "R" and user == "P":
        print("User wins!!!")
        user_score = user_score + 1
    else:
        print("Computer wins!!!")
        computer_score = computer_score + 1

    # we consider printing the score for both user and computer over here
    print("The current user score is ", str(user_score))
    print("The current computer score is", str(computer_score))
