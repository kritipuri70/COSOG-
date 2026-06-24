temp = int(input("Enter the temperature:"))
humidity = int(input("Enter the humidity:"))
wind = int(input("Enter the wind:"))
risk = 0 

if temp >= 50:
    print(f"Temperature is {temp} degree , alert")
    risk = risk + 1

if humidity <= 15:
    print(f"Humidity is {humidity}, alert")
    risk = risk + 1

if wind >= 5:
    print(f"Wind is {wind}, alert")
    risk = risk + 1

print("RISK LEVEL")
if risk == 3:
    print("3, HIGH RISK ")
if risk == 2:
    print("2 , MEDIUM RISK ")
if risk == 1:
    print("1, LOW RISK")
