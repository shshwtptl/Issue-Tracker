import json
from dataclasses import *
def saveTicket(ticket, filename="tickets.json"):
    try:
        with open(filename, "r") as file:
            tickets = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tickets = []

    tickets.append(asdict(ticket))

    with open(filename, "w") as file:
        json.dump(tickets, file, indent=4)
