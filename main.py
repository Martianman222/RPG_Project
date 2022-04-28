import sys
# def main(args: list[str]) -> int:
#     # print(args)
enemies = {
    1 : "slime",
    2 : "skelton",
    3 : "goblin",
}

level = 1
import random 
enemy =  random.randint(1,3)
picknum = enemy
print(picknum)
enemy = enemies[enemy]
print("Enemy type:" , enemy)

def player_stats():
    print("Player Stats: ")
    player_health()
    player_armour()
    player_ap()

def player_health():
    max_health = 50
    print("Your health:" , max_health)

def player_armour():
    current_armour = 10
    print("Your armour strentgh:" , current_armour)

def player_ap():
    attack_points = 10
    print("Your damage:" , attack_points)


def enemydisplay():
    enemyhealth()
    enemyarmour() 
    enemyap() 
    
def enemyhealth():
    print("Enemys health:" , level * 10 * picknum)

def enemyarmour():
    print("Enemys armour:" , level * 5 * picknum)
    
def enemyap():
    print("Enemys attack points:" , level * 3 * picknum)

def playerattack():
    enemydisplay()

def tempname():  
    playerattack()

tempname()
player_stats()
#   if __name__ == "__main__":
#     error: int = main(sys.argv)
