import json
from dataclasses import *
import main as m
def saveTicket(ticket: m.Ticket, filename="tickets.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}


    category = ticket.ticket_type.upper()

    if category not in data:
        data[category] = []

    ticket_data = {
        "ticket_id": ticket.ticket_id,
        "ticket_name": ticket.ticket_name,
        "ticket_desc": ticket.ticket_description,
        "ticket_state": ticket.ticket_state,
        "ticket_type": ticket.ticket_type,
        "ticker_active_status": ticket.active
    }

    data[category].append(ticket_data)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
