servers = {"s1": "Overloaded","s2": "Underloaded","s3": "Balanced","s4": "Overloaded","s5": "Underloaded"}
print("Initial Server Status:")
print(servers)
print("\nScanning Servers...")
overloaded = []
underloaded = []
for s in servers:
    if servers[s] == "Overloaded":
        print(s, "is Overloaded")
        overloaded.append(s)
    elif servers[s] == "Underloaded":
        print(s, "is Underloaded")
        underloaded.append(s)
    else:
        print(s, "is Balanced")
print("\nBalancing Load...")

for i in range(len(overloaded)):
    if i < len(underloaded):
        print("Moving load from", overloaded[i], "to", underloaded[i])
        servers[overloaded[i]] = "Balanced"
        servers[underloaded[i]] = "Balanced"
print("\nFinal Server Status:")
print(servers)
