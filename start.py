temp=int(input("Enter the  temperature "))
humidity=int(input("Enter the humidity "))
wind_speed=int(input("Enter the wind speed "))
threshold_temp=50
threshold_humidity=15
threshold_wind_speed=5
if (temp>threshold_temp and humidity>threshold_humidity and wind_speed>threshold_wind_speed):
    print("The risk level is 3")
elif (temp>threshold_temp and humidity>threshold_humidity):
        print("The risk level is 2")
else:
    print("The risk level is 1")