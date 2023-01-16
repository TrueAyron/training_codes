import argparse

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return kelvin

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Define the command-line interface
parser = argparse.ArgumentParser(description='Temperature converter')

# Define the arguments
parser.add_argument('temperature', type=float, help='Temperature to convert')
parser.add_argument('unit', choices=['C', 'F', 'K'], help='Unit of temperature')
parser.add_argument('-c', '--convert_to', choices=['C', 'F', 'K'], default='F', help='Unit to convert to')

# Parse the arguments
args = parser.parse_args()

# Convert the temperature
if args.unit == 'C':
    if args.convert_to == 'F':
        result = celsius_to_fahrenheit(args.temperature)
    elif args.convert_to == 'K':
        result = celsius_to_kelvin(args.temperature)
elif args.unit == 'F':
    if args.convert_to == 'C':
        result = fahrenheit_to_celsius(args.temperature)
    elif args.convert_to == 'K':
        result = fahrenheit_to_kelvin(args.temperature)
elif args.unit == 'K':
    if args.convert_to == 'C':
        result = kelvin_to_celsius(args.temperature)
    elif args.convert_to == 'F':
        result = kelvin_to_fahrenheit(args.temperature)

# Print the result
print(f'{args.temperature} {args.unit} is {result} {args.convert_to}')
