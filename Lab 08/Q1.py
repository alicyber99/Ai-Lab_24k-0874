class Environment:
    def __init__(self):
        self.payoff = {
            "Zone A": [3, 5],
            "Zone B": [2, 9]
        }

    def thief_move(self, zone):
        print(f"\n[Environment] Thief analyzing Robot's move: {zone}")
        
        values = self.payoff[zone]
        min_value = float('inf')
        best_option = ""

        for i, val in enumerate(values):
            print(f"   Thief Option {i+1} ,Payoff: {val}")
            
            if val < min_value:
                min_value = val
                best_option = f"Option {i+1}"

        print(f"   Thief selects {best_option} with value {min_value}")
        return min_value


class Agent:
    def __init__(self, env):
        self.env = env

    def minimax(self):
        print("GAME START\n")
        
        best_value = float('-inf')
        best_move = ""

        for zone in self.env.payoff:
            print(f"[Agent] Robot chooses: {zone}")
            
            value = self.env.thief_move(zone)
            
            print(f"   Result after thief move: {value}\n")

            if value > best_value:
                best_value = value
                best_move = zone

        print("FINAL DECISION")
        print(f"Best Move (Robot): {best_move}")
        print(f"Final Outcome Value: {best_value}")

env = Environment()
robot = Agent(env)

robot.minimax()

