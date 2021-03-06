'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''
try:
    temp = int(input("Please enter the current temperature in Celsius:"))
except ValueError as err:
    print("Sorry, you need to re-enter...", err)

temp_F = temp * 1.8 + 32
print(f"{temp} degrees celsius = {temp_F} degrees fahrenheit")