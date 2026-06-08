def find_Current(v,r):
    return v / r
def find_Resistance(v,i):
    return v / i
def find_Voltage(i,r):
    return i * r
print("Ohm's Law Calculator")
print("v =", find_Voltage(0.5,10))
print("i =", find_Current(9,3))
print("r =", find_Resistance(12,2))
choice = input("what do you want to find? (1/2/3):")
if choice =="1":
     v = float(input("Enter Voltage (v):"))
     r = float(input("Enter Resistance(r):"))
     print("Current =",find_Current(v,r),"A")
elif choice == "2":
     v =float(input("Enter voltage (v):"))
     i =float(input("Enter Current (i):"))
     print("Resistance =",find_Resistance(v,i), "Ω")
elif choice == "3":
      i =float(input("Enter Current (i):"))
      r = float(input("Enter Resistance(r):"))
      print("Voltage =",find_Voltage(i,r), "V")
else:
      print("Invalid choice.")
