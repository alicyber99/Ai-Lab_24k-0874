a) Apply Minimax
Step 1: MIN player (opponent) chooses minimum at each branch
Stop : min(6, 7) = 6
Go : min(2, 4) = 2
Turn : min(8, 3) = 3

Step 2: MAX player chooses maximum
MAX = max(6, 2, 3) = 6
Best action = STOP
b) Alpha-Beta Pruning 
We go left , right.
1. Start at root (MAX)
α = -∞, β = +∞
2. Explore STOP (MIN node)
α = -∞, β = +∞
Check children:
First value = 6 , β = 6
Second value = 7 , β = min(6,7) = 6
Return 6
Update root:
α = max(-∞, 6) = 6
3. Explore GO (MIN node)
α = 6, β = +∞
Check children:
First value = 2 → β = 2
Now: β (2) ≤ α (6) , PRUNE
Skip second value (4)
Return 2
4. Explore TURN (MIN node)
α = 6, β = +∞
Check children:
First value = 8 , β = 8
Second value = 3 , β = 3
Now: β (3) ≤ α (6) , (no more children anyway)
Return 3
Final decision at root:
max(6, 2, 3) = 6
Best action = STOP
c) Pruned Branches
Only one branch pruned:
In GO branch, value 4 is NOT evaluated 
d) Nodes NOT evaluated
Total leaf nodes = 6
Evaluated = 5
Pruned = 1
Answer: 1 node not evaluated
