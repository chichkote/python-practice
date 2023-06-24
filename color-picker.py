color = input("Select a color (red, purple, blue, green, yellow, pink): ")

if color == "red":
    print("\033[91mThis is red color\033[0m")
elif color == "purple":
    print("\033[95mThis is purple color\033[0m")    
elif color == "blue":
    print("\033[94mThis is blue color\033[0m")
elif color == "green":
    print("\033[92mThis is green color\033[0m")
elif color == "yellow":
    print("\033[93mThis is yellow color\033[0m")
elif color == "pink":
    print("\033[38;5;198mThis is pink color\033[0m")
else:
    print("\033[97mselected color is not available, so printing in white\033[0m")