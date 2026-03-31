#Variables:
#position of city  in the tour (0 to 9, for 10 cities)
#Domains:
#Each variable can take any city index from 0 to 9
#Constraints:
#All-different constraint: Each city must appear exactly once in the tour.
#Tour closure: After visiting the last city, return to the starting city.
#Distance minimization: The sum of distances between consecutive cities (including return to start) should be minimized.

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

distance_matrix = [
    [0, 29, 20, 21, 16, 31, 100, 12, 4, 31],
    [29, 0, 15, 29, 28, 40, 72, 21, 29, 41],
    [20, 15, 0, 15, 14, 25, 81, 9, 23, 27],
    [21, 29, 15, 0, 4, 12, 92, 12, 25, 13],
    [16, 28, 14, 4, 0, 16, 94, 9, 20, 16],
    [31, 40, 25, 12, 16, 0, 95, 24, 36, 3],
    [100, 72, 81, 92, 94, 95, 0, 90, 101, 99],
    [12, 21, 9, 12, 9, 24, 90, 0, 15, 25],
    [4, 29, 23, 25, 20, 36, 101, 15, 0, 35],
    [31, 41, 27, 13, 16, 3, 99, 25, 35, 0]
]

def solve_tsp(distance_matrix):
    n = len(distance_matrix)
    manager = pywrapcp.RoutingIndexManager(n, 1, 0)  

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        index = routing.Start(0)
        path = []
        total_distance = 0
        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            path.append(node)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        path.append(manager.IndexToNode(index)) 
        return path, total_distance
    else:
        return None, None


# Output
#Optimal Path: [0, 8, 2, 7, 4, 3, 5, 9, 1, 6, 0]
#Total Distance: 253

