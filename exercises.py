from decimal import Decimal, getcontext

# 1. Hello World
print('Hello World')
name = input('What is your name? : ')
print(f'Hello {name}') 

# 2. Temperature Conversion
def convertToFahrenheit(degreesCelsius):
    fahrenheit = degreesCelsius * (9/5) + 32
    return fahrenheit

def convertToCelsius(degreesFahrenheit):
    celsius = (degreesFahrenheit - 32) * (5/9)
    return celsius

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001

print(convertToFahrenheit(43))

context = getcontext()
getcontext().prec = 3

# Decimal operations will now use the updated precision
result = Decimal('1.234567') + Decimal('2.34567')
print(result)  # Output: 3.58 (only 3 digits of precision)

# 3. Even and Odd Functions
def isEven(number):
    if number % 2 == 0:
        return True
    return False

def isOdd(number):
    if number % 2 != 0:
        return True
    return False


print(isOdd(8))
print(isEven(5))

# 4. Area, Perimeter, Volume, and Surface Area Functions
def area(length, width):
    return length * width

def perimeter(length, width):
    return (length + width) * 2

def volume(length, width, height):
    return length * width * height

def surface_area(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

print(surface_area(2, 3, 4))

# 5. Fizz Buzz
def fizzBuzz(upTo):
    for num in range(1, upTo + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz', end=' ')
        elif num % 3 == 0:
            print('Fizz', end=' ')
        elif num % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(f'{num}', end=" ")

fizzBuzz(21)