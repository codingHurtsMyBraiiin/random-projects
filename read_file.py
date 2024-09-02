# r = Read
# a = Append
# w = Write
# x = Create


with open("_____") as file:

    total_lines = 0
    for i in file:
        total_lines += 1

    file.seek(0) #Resets pointer to the beginning

    print(f"Total Lines: {total_lines}")
    print(file.read())
    
    file.seek(2)
    print(file)
