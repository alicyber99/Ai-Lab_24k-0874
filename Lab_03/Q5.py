deliveries = [
    {"room": 101, "medicine": "Panadol"},
    {"room": 102, "medicine": "Vitamin A"},
    {"room": 103, "medicine": "Antibiotic"},
    {"room": 104, "medicine": "Vitamin C"},
    {"room": 105, "medicine": "Painkiller"},
    {"room": 106, "medicine": "Heart Medicine"},
    {"room": 107, "medicine": "Cough Syrup"}
]
print("Hospital Delivery Robot Starting...\n")

for d in deliveries:
    print("Moving to Medicine Storage...")
    print("Picking up", d["medicine"])
    print("Moving to Patient Room", d["room"])
    print("Scanning Patient ID...")
    print("ID Verified")
    print("Delivering", d["medicine"], "to Room", d["room"])
    if d["medicine"] in ["Insulin", "Antibiotic", "Heart Medicine"]:
        print("Alert: Notify nurse about", d["medicine"], "delivery!")
    print("Delivery Completed\n")
print("All deliveries completed successfully.")
