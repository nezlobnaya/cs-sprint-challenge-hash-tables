#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

tickets = [
    Ticket("PIT",  "ORD" ),
    Ticket("XNA",  "CID" ),
    Ticket("SFO",  "BHM"),
    Ticket("FLG",  "XNA"),
    Ticket("NONE",  "LAX"),
    Ticket(  "LAX",  "SFO"),
    Ticket(  "CID",  "SLC"),
    Ticket(  "ORD",  "NONE"),
    Ticket(  "SLC",  "PIT"),
    Ticket(  "BHM",  "FLG")
]

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = [None] * length

    for i in range(length):

        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination

        if tickets[i].source not in cache:
            cache[tickets[i].source] = tickets[i].destination

    for x in range(length):
        
        if route[x - 1] is not None:
            route[x] = cache[route[x - 1]]
    return route

print(reconstruct_trip(tickets, 10))