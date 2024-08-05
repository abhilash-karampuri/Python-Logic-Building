#Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter the number corresponding to the conversion you want: ").strip()
    
    if choice in ['1', '2', '3', '4', '5', '6']:
        temperature = float(input("Enter the temperature value: "))
        
        if choice == '1':
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is equal to {result:.2f} Fahrenheit")
        elif choice == '2':
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is equal to {result:.2f} Celsius")
        elif choice == '3':
            result = celsius_to_kelvin(temperature)
            print(f"{temperature} Celsius is equal to {result:.2f} Kelvin")
        elif choice == '4':
            result = kelvin_to_celsius(temperature)
            print(f"{temperature} Kelvin is equal to {result:.2f} Celsius")
        elif choice == '5':
            result = fahrenheit_to_kelvin(temperature)
            print(f"{temperature} Fahrenheit is equal to {result:.2f} Kelvin")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} Kelvin is equal to {result:.2f} Fahrenheit")
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
