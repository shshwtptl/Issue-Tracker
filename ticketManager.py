from dataclasses import *
from input import *
import main as m

@dataclass
class command:
    name: str
    desc: str

commands = [
    command("Help", ">> Lists the base commands."),
    command("Create", ">> Initializes the create function for the Issue."),
]

def checkInput():
    _inp = input()
    return _inp

def help():
    print("This is help page.")

    for i in commands:
        print(i.name + " " + i.desc)

def create():
    m.createTicket()

def main():
    
    print("Issue Tracking System")
    print("This is a basic recreation of a Issue-Ticket system, designed for IT workspaces.")
    print("Type 'help' for info on Use.")   

    inp = getStr()

    if inp == 'help':
        help()
    if inp == "create":
        create()



main()