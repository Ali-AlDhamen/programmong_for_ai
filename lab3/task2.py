import math

def convert_to_fahrenheit(c):
    return (9.0/5.0 * c + 32)

def convert_to_mile(km):
    return (0.6214 * km)

def convert_to_seconds(h):
    return (h * 3600)

def average_score(v1, v2, v3, v4):
    return ((v1 + v2 + v3 + v4)/4)

def distance_between_two_points(x1, y1, x2, y2):
    return (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))


def menu():
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Kilometers to Miles")
    print("3. Convert Hours to Seconds")
    print("4. Calculate the average score")
    print("5. Calculate the distance between two points")
    print("6. Quit")
    return int(input("Enter your choice: "))


def main():
    while True:
        match (menu()):
            case 1:
                c = float(input("Enter Celsius: "))
                print("Fahrenheit: ", convert_to_fahrenheit(c))
            case 2:
                km = float(input("Enter Kilometers: "))
                print("Miles: ", convert_to_mile(km))
            case 3:
                h = float(input("Enter Hours: "))
                print("Seconds: ", convert_to_seconds(h))
            case 4:
                v1, v2, v3, v4 = map(float, input("Enter 4 scores: ").split())
                print("Average score: ", average_score(v1, v2, v3, v4))
            case 5:
                x1, y1, x2, y2 = map(float, input("Enter 4 points: ").split())
                print("Distance: ", distance_between_two_points(x1, y1, x2, y2))
            case 6:
                print("Bye!")
                break
            case _:
                print("Invalid choice")
                break
            
            
if __name__ == "__main__":
    main()
        


