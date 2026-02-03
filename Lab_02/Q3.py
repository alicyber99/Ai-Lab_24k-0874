class ResponseAgent:
    def execute_response(self):
        print("Generic response action")

class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("Sending security alert notifications to admin.\n")

class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("Blocking malicious IP address and stopping attack.\n")

class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("Restoring system files and recovering services.\n")

agent1 = AlertAgent()
agent2 = BlockAgent()
agent3 = RecoverAgent()

agents = [agent1, agent2, agent3]
print("Automated Cybersecurity Response System\n")

for agent in agents:
    agent.execute_response()
