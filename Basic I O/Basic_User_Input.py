import re
    
def get_temperature():
    while True:
        temperature = input("Enter temperature with unit (C or F):\n")
        temperature_patter = r"-?\d+(\.\d+)?\s*[cCfF]$"

        if re.match(temperature_patter, temperature):
            return temperature.strip()
        else:
            print("Please provide a valid tempreture with unit (C or F):\n")


def to_Fahrenheit(value):
    return value * 9 / 5 + 32

def to_Celsius(value):
    return (value - 32) * 5 / 9


temperature = get_temperature()
value = float(temperature[0:-1])
unit = temperature[-1]

if unit.lower() == "c":
    converted_value = to_Fahrenheit(value)
    print(f"{value} C in Fahrenheit is: {converted_value} F")
else:
    converted_value = to_Celsius(value)
    print(f"{value} F in Celsius is: {converted_value} C")
