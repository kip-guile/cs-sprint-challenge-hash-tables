#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    trip = {}
    route = [None] * length

    for ticket in tickets:
        trip[ticket.source] = ticket.destination

    nextStop = trip['NONE']

    for cur in range(0, length):
        route[cur] = nextStop
        nextStop = trip[nextStop]

    return route
