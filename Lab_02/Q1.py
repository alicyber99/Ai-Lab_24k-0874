class SecurityAgent:
    def __init__(self, agentId, name, status):
        self.agentId = agentId
        self.name = name
        self.status = status

    def showInfo(self):
        print("Agent ID: ",self.agentId)
        print("Name: ",self.name)
        print("Status: ", self.status)

class FirewallAgent(SecurityAgent):
    def monitorTraffic(self):
        print(self.name," is monitoring network traffic.")
        print("Suspicious traffic detected! Blocking the IP address.\n")

class MalwareDetectionAgent(SecurityAgent):
    def scanFiles(self):
        print(self.name," is scanning files for malware.")
        print("Malware found! Quarantining infected files.\n")

class AutomationAgent(SecurityAgent):
    def runAutomation(self):
        print(self.name," is running AI-based automation tasks.")
        print("System optimized and security patches updated.\n")

firewall = FirewallAgent(101, "Firewall Guard", "Active")
malware = MalwareDetectionAgent(102, "Malware Scanner", "Active")
automation = AutomationAgent(103, "Automation Bot", "Active")

print("Cybersecurity System Simulation\n")

firewall.showInfo()
firewall.monitorTraffic()

malware.showInfo()
malware.scanFiles()

automation.showInfo()
automation.runAutomation()
