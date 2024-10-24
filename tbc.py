#tbcy.py
#charecter class and fight function
#CS 120
Import tbc

def main():
    player = tbc.Character()
    player.name = "Hero"
    player.hitPoints = 20
    player.hitChance = 40
    player.maxDamage = 10
    player.armor = 2

    monster = tbc.Character("Monster", 30, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()
    