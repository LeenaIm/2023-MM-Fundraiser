# If they say yes, output 'Let's get started...'
# If they say no, output '*** How To Play ***'
# If the answer is invalid, 'Please answer yes / no'
def yes_no (question) :

    valid = False
    while not valid:
        response = input (question) .lower()

        if response == "yes" or response == "y" :
            response = "yes"
            return response

        elif response == "no" or response == "n" :
            response = "no"
            return response

        else:
            print ()
            print ("Please answer yes / no")
            print ()

# Instructions - how to play game
def instructions() :
    print ()

played_before = yes_no ("Have you played the game before? ")
if played_before == "no":
    instructions ()