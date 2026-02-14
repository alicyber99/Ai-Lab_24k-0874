components = {'A': "Safe",'B': "Vulnerable",'C': "Safe",'D': "Vulnerable",'E': "Safe",'F': "Vulnerable",'G': "Safe",'H': "Safe",'I': "Vulnerable"}
print("Initial System State")
print(components)
print("\nSystem Scanning...")
vulnerable = []
for c in components:
    if components[c] == "Vulnerable":
        print(c, "is Vulnerable")
        vulnerable.append(c)
    else:
        print(c, "is Safe")
print("\nPatching Started...")
for c in vulnerable:
    components[c] = "Safe"
    print(c, "patched successfully")
print("\nFinal System State")
print(components)
