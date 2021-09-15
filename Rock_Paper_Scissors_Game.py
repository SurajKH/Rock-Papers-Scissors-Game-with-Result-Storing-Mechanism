import random as rd

user_score = 0
computer_score = 0

while True:
    user = input("Enter R(Rock)/P(Paper)/S(Scissor) or Q(Quit):")

    if user == "Q":
        print("Program is terminated")
        if user_score>computer_score:
            print("User is the final Winner!!!")
        elif computer_score>user_score:
            print("Computer is the final Winner!!!")
        else:
            print("Its a Draw!!!!")

        quit()

    # we have created a list of options for the user
    option_list = ["R", "P", "S", "Q"]
    # now we utilize the random numbers for selecting the options within the list
    rand_num = rd.randint(0, 2)
    computer = option_list[rand_num]

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
        computer_score=computer_score+1

    print("The current user score is ",str(user_score))
    print("The current computer score is",str(computer_score))
