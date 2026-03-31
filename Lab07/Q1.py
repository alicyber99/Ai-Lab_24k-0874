#CSP Definition
#Variables:
#robot position at each step
#Domain:
#All valid grid cells 
#Constraints:
#Move only diagonally 
#Stay inside grid
#Avoid obstacles
#Reach target (4,4)
#Minimize total cost//

from ortools.sat.python import cp_model
import math


n = 5


start = (1, 1)
target = (4,4)
obstacles = [(2, 2)]

model = cp_model.CpModel()

steps = 10
x = [model.NewIntVar(0, n-1, f"x{i}") for i in range(steps)]
y = [model.NewIntVar(0, n-1, f"y{i}") for i in range(steps)]

model.Add(x[0] == start[0])
model.Add(y[0] == start[1])


for i in range(steps-1):
    dx = model.NewIntVar(-1, 1, f"dx{i}")
    dy = model.NewIntVar(-1, 1, f"dy{i}")

    model.Add(x[i+1] == x[i] + dx)
    model.Add(y[i+1] == y[i] + dy)

    
    model.AddAbsEquality(model.NewIntVar(1,1,f"abs_dx{i}"), dx)
    model.AddAbsEquality(model.NewIntVar(1,1,f"abs_dy{i}"), dy)


for i in range(steps):
    for ox, oy in obstacles:
        model.AddForbiddenAssignments([x[i], y[i]], [(ox, oy)])


reached = []
for i in range(steps):
    r = model.NewBoolVar(f"reach{i}")
    model.Add(x[i] == target[0]).OnlyEnforceIf(r)
    model.Add(y[i] == target[1]).OnlyEnforceIf(r)
    reached.append(r)

model.Add(sum(reached) >= 1)


solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = 5

status = solver.Solve(model)


if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
    print("Path:")
    for i in range(steps):
        px = solver.Value(x[i])
        py = solver.Value(y[i])
        print((px, py), end=" ")

        if (px, py) == target:
            break
else:
    print("No solution found")



#import math

#start = (1, 1)
#target = (4, 4)

#x, y = start
#path = [(x, y)]

#while (x, y) != target:
   # x += 1
   # y += 1
   # path.append((x, y))

#steps = len(path) - 1
#cost = steps * math.sqrt(2)

#print("Shortest Path:", path)
#print("Total Cost:", cost)


#output : Shortest Path: [(1,1), (2,2), (3,3), (4,4)]
#Total Cost: 4.2426
