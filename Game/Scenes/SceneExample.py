import DGScene
import DGText
# example of how i want scenes to work, this code isn't actually doing anything right now

self = DGScene()

description = "basic room, it has a floor, walls, ceiling, a button and an exit door. It's quite cosy!"
tempProgressCommands = ["use exit", "exit", "door", "walk through door", "walk through exit"]
tempFunctionCommands = ["use button", "button", "press button"]

def tempFunction():
    #you pressed the button, nothing happens
    DGText.printScan(DGText.action + "You pressed the button.")
    DGText.printScan(DGText.rip + "Nothing happens. It had a very satisfying click.")
