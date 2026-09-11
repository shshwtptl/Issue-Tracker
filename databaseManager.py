import json
from dataclasses import *
import main as m
import user as u

id_u_filename = "userID.json"
id_t_filename = "ticketID.json"

db_u_filename = "users.json"
db_t_filename = "ticekts.json"

def saveTicket(ticket: m.Ticket):
    try:
        with open(db_t_filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}


    category = ticket.TYPE.upper()

    if category not in data:
        data[category] = []

    ticket_data = {
        "ticket_id": ticket.ID,
        "ticket_name": ticket.NAME,
        "ticket_desc": ticket.DESC,
        "ticket_state": ticket.STATE,
        "ticket_type": ticket.TYPE,
        "ticker_active_status": ticket.ACTIVE
    }

    data[category].append(ticket_data)

    with open(db_t_filename, "w") as file:
        json.dump(data, file, indent=4)

def saveUser(user: u.user):
    try:
        with open(db_u_filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}


    category = user.RANK.upper()

    if category not in data:
        data[category] = []

    user_data = {
        "user_id": user.UNIQUE_ID,
        "user_name": user.USERNAME,
        "user_email": user.EMAIL,
        "user_pass": user.PASS,
        "user_active": user.ACTIVE
    }

    data[category].append(user_data)

    with open(db_u_filename, "w") as file:
        json.dump(data, file, indent=4)

def saveID(id, type):
    filename: str
    isNull = True

    if(type=="user"):
        filename = id_u_filename
        isNull = False
    elif(type=="ticket"):
        filename = id_t_filename
        isNull = False
    else:
        print("type unavailable")
        isNull = True
        
    if (not isNull):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

    data.append(id)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def generateID(type: str):
    if(type=="user"):
        filename = id_u_filename
        isNull = False
    elif(type=="ticket"):
        filename = id_t_filename
        isNull = False
    else:
        print("type unavailable")
        isNull = True

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if not data:
        return 1

    return max(data) + 1