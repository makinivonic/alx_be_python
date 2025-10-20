FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# def convert_to_celcius(fahrenheit):
#     result = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
#     return result

convert_to_celcius  = lambda fahrenheit : (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
convert_to_fahrenheit = lambda celcius : (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input('Enter the temperature to convert: '))
metric = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()

if metric == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
elif metric == "F":
    result = convert_to_celcius(temperature)
    print(f"{temperature}°F is {result}°C")
else:
    print("Invalid temperature metric was provided.")