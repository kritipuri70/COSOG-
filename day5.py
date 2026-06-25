temp=int(input("Enter temperature  "))
humidity=int(input("Enter humidity   "))
if(temp>=50):
    if(humidity<=25):
        print("There is a risk of fire")
else:
    print("There is no risk of fire")