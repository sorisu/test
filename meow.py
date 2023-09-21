#-----Juicy part of the program------#

def main():
    userinput = int(input("How many times should the cat meow? ")) #Requests user input and only accepts integers.
    meow(userinput) #calls meow() and passes the user input.


#-----Function Definition Space-----#

#meow() function definition
def meow(n):
    for i in range(n): #Loops through n-times. n is dynamic, set by the user input defined in main()
        print("meow")


#-----------Call main()------------#
main()
