with open("flights.txt", "w") as f:
    f.write("payload=2.5, speed=20, time=20, energy=44.5\n")
    f.write("payload=0.5, speed=5, time=15, energy=24.5\n")
    f.write("payload=4.0, speed=12, time=25, energy=59.6\n")
with open("flights.txt", "r") as f:
    content = f.read()
    print(content)
