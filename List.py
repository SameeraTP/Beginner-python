# Fruits=['apple',"orange","grape","banana"]
# print(Fruits[0])

# Fruits.append("pomegranate")
# print(Fruits)

# Fruits.extend(["kiwi","avacado"])
# print(Fruits)

import random

# print("Who's Pay the Bill?")
# friends=["Jina","Annie","Georgy","Max","Simon"]

# #option 1
# print(random.choice(friends))

# #option 2
# random_name=random.randint(0,4)
# print(friends[random_name])

#ROCK, PAPER, SCISSORS
game=["ROCK","PAPER","SCISSORS"]
rps=int(input("what do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS:\n"))
if rps>2:
    print("invalid")
    exit()
print(f'you choose {game[rps]}')
computer_choose=random.randint(0,2)
print(f'computer choose {game[computer_choose]}')

if rps==computer_choose:
    print("it's a tally")
elif rps==0 and computer_choose==2:
    print("you Won")
elif rps==0 and computer_choose==1:
    print("computer Won")
elif rps==1 and computer_choose==0:
    print("you Won")
elif rps==1 and computer_choose==2:
    print("computer Won")
elif rps==2 and computer_choose==1:
    print("you Won")
elif rps==2 and computer_choose==0:
    print("computer Won")
