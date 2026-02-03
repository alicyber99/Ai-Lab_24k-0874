class Threat:
    def __init__(self, threatId, name, severity):
        self.threatId = threatId
        self.name = name
        self.severity = severity

    def showDetails(self):
        print("Threat ID:", self.threatId)
        print("Name:", self.name)
        print("Severity:", self.severity)

class PhishingThreat(Threat):
    def analyzeEmail(self):
        print("Analyzing suspicious email content.")
        print("Phishing link detected and blocked.\n")

class RansomwareThreat(Threat):
    def scanFiles(self):
        print("Scanning system files for ransomware activity.")
        print("Encrypted files detected. System isolated.\n")

class BotnetThreat(Threat):
    def detectTraffic(self):
        print("Monitoring network traffic for botnet signals.")
        print("Botnet communication stopped.\n")

t1 = PhishingThreat(301, "Email Phishing", "High")
t2 = RansomwareThreat(302, "File Ransomware", "Critical")
t3 = BotnetThreat(303, "Network Botnet", "Medium")

print("AI Threat Intelligence System\n")

t1.showDetails()
t1.analyzeEmail()

t2.showDetails()
t2.scanFiles()

t3.showDetails()
t3.detectTraffic()