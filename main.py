from dataclasses import *
import random
import databaseManager as dm
from input import *
import user as u

@dataclass
class Ticket:
    ID: int
    NAME: str
    DESC: str
    STATE: str
    TYPE: str
    ACTIVE: bool

def stateMachine(ticket: Ticket, new_state: str):
    state = ["Active", "In Progress", "Resolved", "Closed", "Unassigned"]

    # If asked to change the state of the ticket
    if ticket.ACTIVE == True:
        if new_state in state:
            ticket.STATE = new_state
            print(f"Ticket {ticket.ID} state changed to {new_state}.")
        else: 
            print(f"The ticket is not valid or active. Current ticket active status: {ticket.ACTIVE}.")

    def askState():
        _state = input("Enter the state you want: ")
        return _state

def activateTicket(ticket: Ticket):
    ticket.ACTIVE = True
    print(f"Ticket {ticket.ID} is now active.")

def createTicket():
    _id = idGenerator(0, 1999)
    _name = t_getStr("Enter the name of the ticket: ")
    _desc = t_getStr("Enter the desc of the ticket: ")
    _type = t_getStr("Enter the type of the ticket: ")
    _state = "Unassigned"
    
    _ticket = Ticket(_id, _name, _desc, _state, _type, False)
    dm.saveTicket(_ticket)

def idGenerator(initial, final):
    _id = random.randrange(initial, final)
    return _id

def deleteTicket():
    inp = t_getStr("Enter the ticket ID to delete: ")

def createUser():
    uid = dm.generateID("user")
    name = t_getStr("Enter your username: ")
    email = t_getStr("Enter your email: ")
    passHash = t_getStr("Pass: ")
    _rank = t_getStr("Rank: ")

    _u = u.user(uid, name, email, passHash, _rank, True)
    dm.saveUser(_u)
    dm.saveID(uid, "user")