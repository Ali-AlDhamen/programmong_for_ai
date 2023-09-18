try:
    with open("output.txt", "w") as f:
        f.write("Hello World")
except IOError:
    print("Error writing to file")
finally:
    f.close()
    
