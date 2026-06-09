def calculate_energy(payload, flight_time, speed):
    return payload * 5 + flight_time * 1.2 + speed * 0.8
flights = [
    {"payload": 2.5, "time": 20, "speed": 10},
    {"payload": 0.5, "time": 15, "speed": 5},
    {"payload": 4.0, "time": 25, "speed": 12},
]
for i, flight in enumerate(flights):
    energy = calculate_energy(flight["payload"], flight["time"], flight["speed"])
    print(f"Flight {i+1}: payload={flight['payload']}kg, time={flight['time']}min, speed={flight['speed']}m/s")
    print(f" Energy consumed: {energy} wh")
    print()
