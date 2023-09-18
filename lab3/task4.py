try:
    with open("lab3/output.txt", "w") as f:
        f.write("Hello World")
except IOError:
    print("Error writing to file")
finally:
    f.close()
    
