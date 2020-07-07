# winning pattern

# snake water snake
# snake gun gun

# water snake snake
# water gun water

# gun snake gun
# gun water water

import random

opt = ['snake', 'water', 'gun']
i = 0
cpu = 0
player = 0
r = 10
f = 0
iv = 0
print(opt)
while i < 10:
    c = random.choice(opt)
    user = input("choose symbol according to your choice: \n"
                 "s = snake\n"
                 "w = water\n"
                 "g = gun\n")
    if user == "s" or "S":
        if c == "snake":
            print("cpu: {}  and player: snake".format(c))
            print("Foul play!!! ")
            f = f + 1
            i = i + 1
            print(i)
        elif c == "water":
            print("cpu: {}  and player: snake".format(c))
            print("congratulation !!!! you win ")
            player = player + 1
            i = i + 1
            print(i)
        elif c == "gun":
            print("cpu: {}  and player: snake".format(c))
            print("Sorry!!!! bad luck ")
            cpu = cpu + 1
            i = i + 1
            print(i)
    elif user == "w" or "W":
        if c == "snake":
            print("cpu: {}  and player: water".format(c))
            print("Sorry!!!! bad luck ")
            cpu = cpu + 1
            i = i + 1
            print(i)
        elif c == "water":
            print("cpu: {}  and player: water".format(c))
            print("foul play ")
            f = f + 1
            i = i + 1
            print(i)
        elif c == "gun":
            print("cpu: {}  and player: water".format(c))
            print("congratulation !!!! you win ")
            player = player + 1
            i = i + 1
            print(i)
    elif user == "g" or "G":
        if c == "snake":
            print("cpu: {}  and player: gun".format(c))
            print("congratulation !!!! you win ")
            player = player + 1
            i = i + 1
            print(i)
        elif c == "water":
            print("cpu: {}  and player: gun".format(c))
            print("Sorry !!!! bad luck ")
            cpu = cpu + 1
            i = i + 1
            print(i)
        elif c == "gun":
            print("cpu: {}  and player: gun".format(c))
            print("foul play ")
            f = f + 1
            i = i + 1
            print(i)

    else:
        print("invalid option")
        iv = iv + 1
        i = i + 1
        print(i)

print('******Final Results******\n'
      'Foul play : {}\n'
      'CPU : {}\n'
      'Player: {}\n'
      'Invalid option: {} '.format(f, cpu, player, iv))
if cpu > player:
    print("WINNER IS CPU")
elif cpu == player:
    print("MATCH DRAW, BOTH HAVE SAME SCORE")
elif player == cpu:
    print("WINNER IS PLAYER")
else:
    print("invalid")
