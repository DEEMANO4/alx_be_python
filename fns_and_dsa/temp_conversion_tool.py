FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
ADDED_FACTOR = 32

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, ADDED_FACTOR
    celsius = (fahrenheit - ADDED_FACTOR) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR, ADDED_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + ADDED_FACTOR
    return fahrenheit

prompt_temperature = int(input("Enter the temperature to convert:"))
Celsius_or_Fahrenheit = input("Is this temperature in celsius or fahrenheit? (C/F):")

if Celsius_or_Fahrenheit == "C":
    Fahrenheit_result = convert_to_fahrenheit(prompt_temperature)
    print(f"{prompt_temperature}°C is {Fahrenheit_result}°F") 

elif Celsius_or_Fahrenheit == "F":
    Celsius_result = convert_to_celsius(prompt_temperature)
    print(f"{prompt_temperature}°F is {Celsius_result}°C")

else: 
    print(f"Invalid temperature. Please enter a numerical value.")


