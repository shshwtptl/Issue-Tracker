from dataclasses import *
from helper.input import *
from helper.basics import *
from logic.databaseManager import *
from logic.main import *

@dataclass
class command:
    name: str
    desc: str

commands = [
    command("Help", ">> Lists the base commands."),
    command("Create", ">> Initializes the create function for the Issue."),
]

def help():
    clear()
    print("This is help page.")

    for i in commands:
        print(i.name + " " + i.desc)

def create():
    clear()

    createTicket()

def login():
    clear()

    id = t_getInt("id: ")
    password = t_getStr("password: ")
    rank = t_getStr("rank: ")

    _login = loginID(id, password, rank)

    if _login == True:
        clear()
        print("Logged in Succesfully.")
        main()
    else:
        print("id or password is wrong.")

def start():
    clear()

    print("register or login?")
    _inp = getStr()

    if _inp == "register":
        createUser()
        start()
    elif _inp == "login":
        login()
    
def main():
    clear()
        
    print("Issue Tracking System")
    print("This is a basic recreation of a Issue-Ticket system, designed for IT workspaces.")
    print("Type 'help' for info on Use.")   

    inp = getStr()

    if inp == 'help':
        help()
    elif inp == "create":
        create()
    elif inp == "fetch":
        username = t_getStr("username")
        email = t_getStr("email")
        fetchUserID(username, email)

start()