def annual_salary(salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative")
    
    
    return (salary * 12)

def main():
    try:
        salary = float(input("Enter salary: "))
        print("Annual salary: ", annual_salary(salary))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()