import sys
from .dijkstras import Dijkstras
from enum import Enum


class Railroad:
    """
    Receives the city-to-city railroad and their distances such as "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" 
    
    The Dijkstras dictionary is 
     {'A': {'B': 5.0, 'C': 9.0, 'D': 1.0, 'E': 3.0},
     'B': {'B': 9.0, 'C': 4.0, 'D': 12.0, 'E': 6.0},
     'C': {'B': 5.0, 'C': 9.0, 'D': 8.0, 'E': 2.0},
     'D': {'B': 5.0, 'C': 8.0, 'D': 16.0, 'E': 2.0},
     'E': {'B': 3.0, 'C': 7.0, 'D': 15.0, 'E': 9.0}}

    and installation of methods for  
    - shortest routes,
    - the distance of specific routes,
    - the number of routes from one city to another with a max number of stops,
    - the number of routes from one city to another with an exact number of stops,
    - the number of routes from one city to another with less than a specified distance.

    """

    TripType = Enum('TripType', 'exact_stops max_stops')

    def __init__(self, graph):
        self.graph = self.convert_graph_to_dictionary(graph)
        self.dijkstras = Dijkstras(self.graph)


    """This method convert_graph_to_dictionary converts the 'graph' string to a dictionary."""
    def convert_graph_to_dictionary(self, graph):
        graph_dictionary = {}
        connection_list = [x.strip() for x in graph.split(',')]
        for connection in connection_list:
            departure_city = connection[0]
            next_city = connection[1]
            distance = float(connection[2:])

            if departure_city not in graph_dictionary:
                graph_dictionary[departure_city] = {}

            graph_dictionary[departure_city][next_city] = distance
        return graph_dictionary


    """This method get_shortest_distance uses Dijkstras algorithm."""
    def get_shortest_distance(self, departure_city, destination_city):
        return self.dijkstras.get_distance(departure_city, destination_city)


    """This method calculates distance for a specific route such as "A-B-C" """
    def get_distance(self, route):
        if route == "":
            print("\n" + route + ": NO SUCH ROUTE")
            return "NO SUCH ROUTE"

        route_cities = route.split('-')
        current_city = route_cities[0]
        total_distance = 0
        # Loop through cities on the route to sum up the distances.
        for i in range(1, len(route_cities)):
            next_city = route_cities[i]
            if current_city in self.graph and next_city in self.graph[current_city]:
                total_distance += self.graph[current_city][next_city]
            else:
                print("\n" + route + ": NO SUCH ROUTE")
                return "NO SUCH ROUTE"
            current_city = next_city

        print("\nThe route " + route + " has the distance of " + str(total_distance))
        return total_distance


    """
    This method gets the number of possible trips from departure_city to destination_city.
    The callback argument is used defaulty = 1 to print out the details when done.
    """
    def get_number_of_possible_trips(self, departure_city, destination_city, num_stops, trip_type, callback=1):
        trip_number = 0
        if num_stops == 0:
            if (callback == 1):
                if (trip_type == self.TripType.max_stops):
                    print("\nThe number of possible trips from " + departure_city + " to " + destination_city + " with maximum of " + str(num_stops) + " stops are: " + str(trip_number))
                else:
                    print("\nThe number of possible trips from " + departure_city + " to " + destination_city + " with exact " + str(num_stops) + " stops are: " + str(trip_number))
            return 0

        # loop through all connections from departure_city
        for next_city in self.graph[departure_city]:
            if next_city == destination_city and (trip_type == self.TripType.max_stops or num_stops == 1):
                trip_number += 1

            trip_number += self.get_number_of_possible_trips(next_city, destination_city, num_stops - 1, trip_type, 0)
        
        if (callback == 1):
            if (trip_type == self.TripType.max_stops):
                print("\nThe number of possible trips from " + departure_city + " to " + destination_city + " with maximum of " + str(num_stops) + " stops are: " + str(trip_number))
            else:
                print("\nThe number of possible trips from " + departure_city + " to " + destination_city + " with exact " + str(num_stops) + " stops are: " + str(trip_number))

        return trip_number


    """This method gets the number of possible trips from departure_city to destination_city of less than max_distance.
    The callback argument is used defaulty = 1 to print out the details when done."""
    def get_number_of_possible_trips_to_maximum_distance(self, departure_city, destination_city, max_distance, callback=1):
        trip_number = 0
        # iterate through all connections from departure_city
        for next_city, distance_to_next in self.graph[departure_city].items():
            if next_city == destination_city and distance_to_next < max_distance:
                trip_number += 1
            if distance_to_next < max_distance:
                trip_number += self.get_number_of_possible_trips_to_maximum_distance(next_city, destination_city, max_distance - distance_to_next, 0)

        if (callback == 1):
            print("\nThe number of possible trips from " + departure_city + " to " + destination_city + " with maximum distance of " + str(max_distance) + " are: " + str(trip_number))

        return trip_number


