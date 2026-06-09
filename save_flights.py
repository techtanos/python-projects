
def save_flight(flights, filename):
    with open(filename, "w") as f:
        for flight in flights:
            f.write(f"{flight['payload']}, {flight['time']}, {flight['speed']}\n")
flights = [
    {"payload": 2.5, "time": 20, "speed": 10},
    {"payload": 0.5, "time": 15, "speed": 5},
]
save_flight(flights, "drone_data.txt")
print("Done")
def load_flights(filename):
    flights = []
    with open(filename, "r") as f:
         for line in f:
             parts = line.strip().split(",")
             flight = {"payload": float(parts[0]), "time": float(parts[1]), "speed": float(parts[2])}
             flights.append(flight)
    return flights
loaded = load_flights("drone_data.txt")
print(loaded)
