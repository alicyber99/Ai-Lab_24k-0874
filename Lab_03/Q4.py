components = {'A': "Safe",'B': "Low",'C': "High",'D': "Low",'E': "Safe",'F': "High",'G': "Low",'H': "Safe",'I': "High"}
print("Initial System State:")
print(components)
print("\nSystem Scanning...")
for c in components:
    if components[c] == "Safe":
        print(c, "is Safe")
    else:
        print(c, "has", components[c], "Risk Vulnerability")
print("\nPatching Process Started...")
for c in components:
    if components[c] == "Low":
        components[c] = "Safe"
        print(c, "Low Risk patched")
    elif components[c] == "High":
        print(c, "High Risk - Premium Service Required")
print("\nFinal System State:")
print(components)
