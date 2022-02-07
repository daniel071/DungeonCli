from Game.Engine.DGEnemy import *
# Enemies for the DC game

Unidentified = Enemy("Unidentified", 25, 5, 10)
DarkWizard = Enemy("Dark Wizard", 5, 25, 40)
Spider = Enemy("Spider", 10, 4, 7)
GiantAnt = Enemy("Giant Ant", 25, 5, 15)
Rat = Enemy("Rat", 10, 1, 5)
Goblin = Enemy("Goblin", 20, 5, 10)
Snake = Enemy("Snake", 30, 10, 15)
Skeleton = Enemy("Skeleton", 30, 10, 15)

listCommon = [
    DarkWizard, Spider, GiantAnt, Rat, Goblin, Snake, Skeleton
]

listRare = [
    Unidentified
]

listAll = [listCommon, listRare]

