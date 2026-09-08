from dataclasses import *
import random
import databaseManager as dm
from input import *

@dataclass
class Ticket:
    ticket_id: int
    ticket_name: str
    ticket_description: str
    ticket_state: str
    active: bool = False

def stateMachine(ticket: Ticket, new_state: str):
    state = ["Active", "In Progress", "Resolved", "Closed", "Unassigned"]

    # If asked to change the state of the ticket
    if ticket.active == True:
        if new_state in state:
            ticket.ticket_state = new_state
            print(f"Ticket {ticket.ticket_id} state changed to {new_state}.")
        else: 
            print(f"The ticket is not valid or active. Current ticket active status: {ticket.active}.")

    def askState():
        _state = input("Enter the state you want: ")
        return _state

def activateTicket(ticket: Ticket):
    ticket.active = True
    print(f"Ticket {ticket.ticket_id} is now active.")

def createTicket():
    _id = idGenerator(0, 1999)
    _name = t_getStr("Enter the name of the ticket: ")
    _desc = t_getStr("Enter the desc of the ticket: ")
    _state = "Unassigned"

    _ticket = Ticket(_id, _name, _desc, _state, False)
    dm.saveTicket(_ticket)

def idGenerator(initial, final):
    _id = random.randrange(initial, final)
    return _id
