# Kiwiland
Kiwiland Railroad service

Candidate: Quan-Ha Le. 
A.	How to setup
•	Python 3.7 for CentOS 7.5 on Amazon Web Services (AWS)
•	I am using the Python language version of JUnit by Kent Beck and Erich Gamma - that is the Python unit testing framework.
•	My GITHUB link for the Kiwiland Railroad is
https://github.com/lequanha/Kiwiland

The AMI that I used to deploy my CentOS ec2 instance is 
CentOS-7-x86_64-EBS-HVM-20180318_121109-877e76fd-a132-410c-9982-c70ca8e41d88-ami-f5cb0388.4 (ami-7d579d00)

From the above AMI, I installed Python 3.7 for CentOS 7.5, the steps please refer to the file inside my GITHUB:    Python3forCentOS.txt


B.	How to deploy
•	From inside your putty session, please make a GIT CLONE
# git clone https://github.com/lequanha/Kiwiland.git
 
•	Please use this statement to list the content
# ls -LRl

•	Please use the available MS Word and/or PDF files for your guidelines
QuanHaLe_documentation.doc
QuanHaLe_documentation.pdf

C.	How to execute
To run the 10 tests provided by Receptivti, please execute
# cd Kiwiland
# python3.7 -m unittest
######################################################
The route A-B-C has the distance of 9.0
.
The route A-D has the distance of 5.0
.
The route A-D-C has the distance of 13.0
.
The route A-E-B-C-D has the distance of 22.0
.
A-E-D: NO SUCH ROUTE
.
The number of possible trips from C to C with maximum of 3 stops are: 2
.
The number of possible trips from A to C with exact 4 stops are: 3
.
The shortest route from A to C is: ABC with distance 9.0
.
The shortest route from B to B is: BCEB with distance 9.0
.
The number of possible trips from C to C with maximum distance of 30 are: 7
.
----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
######################################################


The default test set’s outputs above are the tests required by Receptiviti company.
To run interactively, execute `python3.7 -i` in the ‘Kiwiland' directory.  You can then enter below commands
import src.railroad as rr
my_routes = rr.Railroad("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
my_routes.get_distance("A-B-C")
my_routes.get_distance("A-D")
my_routes.get_distance("A-D-C")
my_routes.get_distance("A-E-B-C-D")
my_routes.get_distance("A-E-D")
my_routes.get_number_of_possible_trips("C", "C", 3, my_routes.TripType.max_stops)
my_routes .get_number_of_possible_trips("A", "C", 4, my_routes.TripType.exact_stops)
 
my_routes.get_shortest_distance("A", "C")
my_routes.get_shortest_distance("B", "B")
my_routes.get_number_of_possible_trips_to_maximum_distance("C", "C", 30)

 
Other unit tests that I have also set up
•	This is to test Dijkstras’ Algorithm
# python3.7 -m unittest tests.dijkstrasmodule
 
•	This is to test the get_distance method
# python3.7 -m unittest tests.getdistancemodule
 

•	This is to test the get_number_of_possible_trips method and the get_number_of_possible_trips_to_maximum_distance method
# python3.7 -m unittest tests.gettripsnumbermodule

 
  

D.	Technical implementation

1.	I implement on Python the Dijkstra’s Algorithm
Dijkstra's Algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, railroad networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.
The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but I would like to apply the most common variant fixes each single node as the "start" node and finds shortest paths from the start node to all other reachable nodes in the graph, producing a shortest-path dictionary.
The source code for Dijkstra’s Algorithm is \Kiwiland\src\dijkstras.py
Let the node at which we are starting be called the start node. Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm will assign some initial distance values and will try to improve them step by step.
Step 1.	Create a set named visit_nodes and loop through all the nodes, initialize the visit_nodes with the start node only.
Step 2.	Loop through the unvisited nodes inside the visit_nodes set
Step 3.	          Take a next_node
Step 4.	          Append all neighbour nodes of the above next_node into the visit_nodes set and calculate or re- update the distances from the start node to each neighbour node.

Step 5.	          Store the minimum route inside the previous_nodes list
Step 6.	          Store the minimum distance inside the shortest_routes list
Step 7.	End Loop when you already visited all the visit_nodes  set and you have no more reachable nodes to add into the visit_nodes set.

2.	The Railroad Graph
The source code is \Kiwiland\src\railroad.py

3.	The Insight Global Test.
The source code is \Kiwiland\tests\test_receptiviti.py
I apply TestSuite and this is the default 10 tests required by Receptiviti company as belows
 
1. The distance of the route A-B-C.
2. The distance of the route A-D.
3. The distance of the route A-D-C.
4. The distance of the route A-E-B-C-D.
5. The distance of the route A-E-D.
6. The number of trips starting at C and ending at C with a maximum of 3 stops.
7. The number of trips starting at A and ending at C with exactly 4 stops.
8. The length of the shortest route (in terms of distance to travel) from A to C.
9. The length of the shortest route (in terms of distance to travel) from B to B.
10. The number of different routes from C to C with a distance of less than 30.

Test Input: Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
This input is stored inside this file \Kiwiland\tests\__init__.py, if you want to change the graph input of all tests, please change this line inside \Kiwiland\tests\__init__.py

Kiwiland = Railroad("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")

4.	The Dijkstra’s Algorithm Test
The source code is \Kiwiland\tests\dijkstrasmodule.py
I apply TestSuite and there are 5 tests to find the shortest routes by Dijkstra’s Algorithm.

5.	The Get Distance Test
The source code is \Kiwiland\tests\getdistancemodule.py
I apply TestSuite and there are 5 tests to find the distance of specific routes.

6.	The Get Number of Possible Trip Test
The source code is \Kiwiland\tests\gettripsnumbermodule.py
I apply TestSuite and there are 9 tests to find the number of possible trips from a departure_city to a destination_city.
