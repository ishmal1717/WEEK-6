days = ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")

index = int(input("Enter index (0-6): "))

if 0 <= index <= 6:
    print("Day:", days[index])
else:
    print("Invalid index")