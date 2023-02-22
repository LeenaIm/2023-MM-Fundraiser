# checks user response is yes / no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print()
            print("Please answer yes / no")
            print()


# Instructions - how to play game
def instructions():
    print()
    print("Instructions go here")
    print()


# If users want to see the instructions, display them
want_instructions = yes_no("Do you want to read the instruction? ")
if want_instructions == "yes":
    instructions()
