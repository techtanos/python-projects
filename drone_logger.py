def calculate_energy(payload, speed, time):
    return payload * 5 + speed * 0.8 + time * 1.2
def save_flight(flight, filename):
    with open(filename, "a") as f:
        f.write(f"{flight['payload']},{flight['time']},{flight['speed']},{flight['energy']}\n")
def show_flights(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())
while True:
    print("\n1. log a flight")
    print("2. show all flights")
    print("3. Quit")
    choice = input("choose:")
    if choice == "1":
        payload = float(input("Payload (kg):"))
        speed = float(input("Speed (m/s):"))
        time = float(input("Time (min):"))
        energy = calculate_energy(payload, speed, time)
        flight = {"payload": payload, "time": time, "speed": speed, "energy": energy}
        save_flight(flight, "drone_og.txt")
        print(f"Flight logged. Energy used: {energy} wh")
    elif choice == "2":
        show_flights("drone_log.txt")
    elif choice == "3":
        break
