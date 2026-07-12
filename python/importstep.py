# If you run script.py directly (e.g., by executing python script.py in the terminal), __name__ will be "__main__", 
# so the main() function will be called, and you'll see "This is the main function." printed.

# If you import script.py into another script (e.g., import script), __name__ in script.py will be "script", 
# so the main() function won't be called automatically.

# This pattern is useful for organizing code and separating functionality. It allows you to define functions and classes in a module while ensuring
#  that certain code only runs when the module is executed as a script, not when it is imported elsewhere.

def main():
    print("This is the main function.")

if __name__ == "__main__":
    main()