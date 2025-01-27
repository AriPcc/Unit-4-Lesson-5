#*****************************************************************************

def main():
    name = ""

    # Print welcome message
    print("This program will ask for your name and then greet you. It will als"
           "o try to detect invalid names.")

    # Prompt user for their name
    name = input("\nPlease enter your name (letters and spaces only): ")

    # Test name for numbers/special characters (except spaces)
    if name.replace(" ", "").isalpha() == False:
        print("\nThat’s not your name! Be honest next time.\n")
    else:
        # Greet user and remove trailing spaces from their name
        print("\nGreetings, ", name.strip(), "!\n", sep="")
    
    # Print goodbye message
    print("See you later...")

main()