def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print("{} degrees Celsius is equal to {} degrees Fahrenheit".format(celsius, fahrenheit))


fahrenheit = 77
celsius = fahrenheit_to_celsius(fahrenheit)
print("{} degrees Fahrenheit is equal to {} degrees Celsius".format(fahrenheit, celsius))
