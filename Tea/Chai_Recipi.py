import time

kettle = [
    "Water",
    "Milk",
    "Tea Leaves",
    "Sugar",
    "Ginger"
    
]

print(">>> Hey Dear, wait... tea is boiling")
time.sleep(0.5)


for kettle in range(5, 0, -1):
    print(f"⏳ Boiling...{kettle}")
    time.sleep(1)

print("\n☕✨ Chai Ready Hai!")