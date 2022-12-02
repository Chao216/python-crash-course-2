try:
    with open("google.txt") as file_1:
        content = file_1.read()
except FileNotFoundError:
    print(f"\nSorry, we cannot find such a file")
        
    
