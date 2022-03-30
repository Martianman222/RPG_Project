slime = 1
skelton = 2
goblin = 3

def randomnum():
    import random
    picknum = random.randint(1,3)
    print(picknum)
    if picknum == 1:
        print("slime")
    elif picknum == 2:
        print("skelton")
    elif picknum == 3:
        print("goblin")

randomnum()