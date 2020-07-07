# Total no of guess 9
# print no of guess left
# no of guess he/she took to finish
# if no. of attempts over it shows game over
print("****************Welcome to number guessing game.**************** "
      "\n********you have only 9 attempts to guess correct no.***********"
      " \n**************** Number is between 1 to 100*********************  ")

n = 13
i = 1
while(True):
    a = int(input("enter no : "))

    if i == 9 and a == n:
        print(f"\n whoo whoo, its your day buddy!!! your guess correctly on last attempt, no is {n}")
        break

    elif i == 9:
        print(f"\n game over!!!!!,{i} attempts are finish, better luck next time ")
        break

    elif a > n:
        print("\n your guess is higher then no")
        # print("no. is not higher then 100")
        print(f"{9-i} attempt left")
        print("Try again!!!")
        i = i + 1

    elif a < n:
        print("\n your guess is lesser then no")
        print(f"{9-i} attempt left")
        print("Try again!!!")
        i = i + 1

    elif a == n:
        print(f"\n congratulation you win, you took only {i} attempts")
        break

    else:
        print("something is wrong")
        break