# Temperature  conversion

temp = float(input("enter the temperature value :"))
unit = input("enter the unit (c for celsius and F for Fahrenheit:)")

if unit == 'C' or unit == 'c':
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif unit == 'F' or unit == 'f':
    celsius = (temp - 32) * 5/9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid unit! Please enter C or F.")