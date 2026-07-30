patients = [
    {
        "Name": "John",
        "Age": 65,
        "Heart Rate": 110,
        "Oxygen Saturation": 92
    },
    {
        "Name": "Alice",
        "Age": 45,
        "Heart Rate": 80,
        "Oxygen Saturation": 98
    },
    {
        "Name": "Bob",
        "Age": 70,
        "Heart Rate": 95,
        "Oxygen Saturation": 93
    },
    {
        "Name": "David",
        "Age": 55,
        "Heart Rate": 120,
        "Oxygen Saturation": 97
    },
    {
        "Name": "Emma",
        "Age": 30,
        "Heart Rate": 75,
        "Oxygen Saturation": 99
    }
]
for patient in patients:
    heart_rate = patient["Heart Rate"]
    oxygen = patient["Oxygen Saturation"]
    if (heart_rate < 60 or heart_rate > 100) and oxygen < 95:
        patient["Status"] = "Critical"
    elif heart_rate < 60 or heart_rate > 100 or oxygen < 95:
        patient["Status"] = "Observation"
    else:
        patient["Status"] = "Normal"
print("----- ALL PATIENT DETAILS -----")
for patient in patients:
    print("\nName:", patient["Name"])
    print("Age:", patient["Age"])
    print("Heart Rate:", patient["Heart Rate"])
    print("Oxygen Saturation:", patient["Oxygen Saturation"])
    print("Status:", patient["Status"])
print("\n----- CRITICAL PATIENTS -----")
critical_patients = []
for patient in patients:
    if patient["Status"] == "Critical":
        critical_patients.append(patient)
        print(patient["Name"])
if len(critical_patients) > 0:
    total_age = 0
    for patient in critical_patients:
        total_age = total_age + patient["Age"]
    average_age = total_age / len(critical_patients)
    print("\nAverage age of critical patients:", average_age)
else:
    print("\nNo critical patients")


# Sort patients by oxygen saturation
sorted_patients = sorted(
    patients,
    key=lambda patient: patient["Oxygen Saturation"]
)

print("\n----- PATIENTS SORTED BY OXYGEN SATURATION -----")

for patient in sorted_patients:
    print(
        patient["Name"],
        "-",
        patient["Oxygen Saturation"]
    )
