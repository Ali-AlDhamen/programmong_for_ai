import math

def area_of_circle(r):
    return (math.pi * r**2)

def area_of_square(s):
    return (s**2)

def area_of_sphere(r):
    return (4 * math.pi * r**2)

def menu():
    print("1. Area of circle")
    print("2. Area of square")
    print("3. Area of sphere")
    print("4. Quit")
    return int(input("Enter your choice: "))


def main():
    while True:
        match (menu()): 
            case 1:
                r = float(input("Enter radius: "))
                print("Area of circle: ", area_of_circle(r))
                
            case 2:
                s = float(input("Enter side: "))
                print("Area of square: ", area_of_square(s))
            
            case 3:
                r = float(input("Enter radius: "))
                print("Area of sphere: ", area_of_sphere(r))
                
            case 4:
                print("Bye!")
                break
            case _:
                print("Invalid choice") 
                break
            
            

if __name__ == "__main__":
    main()