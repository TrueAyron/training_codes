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

# Usage examples
print(celsius_to_fahrenheit(0)) # 32.0
print(celsius_to_kelvin(0)) # 273.15
print(fahrenheit_to_celsius(32)) # 0.0
print(fahrenheit_to_kelvin(32)) # 273.15
print(kelvin_to_celsius(273.15)) # 0.0
print(kelvin_to_fahrenheit(273.15)) # 32.0
