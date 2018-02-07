'''

Given a series of plane tickets, each showing a departure airport and destination,
print the itinerary for the given trip.

Trip is one way, no round trips.  Assumption is that input is valid, and no
plane tickets are missing.

FROM->TO

Input:
SFO->NYC
HYD->HKG
NYC->LON
LON->HYD

Output:
SFO
NYC
LON
HYD
HKG

Print output to console

{SFO: [NYC],
HYD: [HKG],
NYC: [LON]....}

Check for data that is in keys, but not values of dict:

use a conditional that uses dict.keys() method and dict.values() method

loop through keys - for each key, is it in values? if not it is the starting travel destination

Loop starting at this special key, print key, then look up the value of 1st key print that, then continue the process until you reach an item that is not listed as a key.
'''


def print_itinerary(travel_tickets):
    """Print itinerary for trip given series of plane tickets.

    Parameters: travel_tickets is a list of tuples.  Index 0 of each tuple will
    be departure airport, index 1 will be destination from current ticket.

    Returns: None - prints travel points in sequence."""

    travel_points = {}

    # create dictionary of start and end points for fast lookup
    # start points are keys, end points are values
    for ticket in travel_tickets:

        start_point = ticket[0]
        end_point = ticket[1]

        if start_point not in travel_points:
            travel_points[start_point] = end_point

    current = None

    # search for first airport in trip
    # if airport code is a start point, but not end point, it is first in trip
    for airport in travel_points:

        if airport not in travel_points.values():
            current = airport

    # print each airport code in sequence of trip
    # stop looping when airport reached that is an end point but not start point
    while True:

        print current

        if current in travel_points.keys():
            current = travel_points[current]

        else:
            break


print_itinerary([('SFO', 'NYC'), ('HYD', 'HKG'), ('NYC', 'LON'), ('LON', 'HYD')])
