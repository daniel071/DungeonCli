import Game.Engine.DGScene as DGScene
import Game.Engine.DGText as DGText
# example of how i want scenes to work, this code isn't actually doing anything right now


description = "basic room, it has a floor, walls, ceiling, a button and an exit door. It's quite cosy!"
tempProgressCommand = ["use exit", "exit", "door", "walk through door", "walk through exit"]
tempFunctionCommand = ["use button", "button", "press button"]

def startScene():
    #there is a button in this room
    DGText.printScan(DGText.action + "A very basic room, you notice there is a button in this room.")
    DGText.printScan(DGText.action + "You can press it.")

def tempFunction():
    #you pressed the button, nothing happens
    DGText.printScan(DGText.action + "You pressed the button.")
    DGText.printScan(DGText.rip + "Nothing happens. It had a very satisfying click.")
